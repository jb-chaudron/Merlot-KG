from spacy.matcher import Matcher 
from spacy.tokens import Span
def get_relation(sent):

    doc = nlp(sent)

    # Matcher class object 
    matcher = Matcher(nlp.vocab)


    #define the pattern 
    pattern = [{'DEP':'ROOT'}, {'DEP':'prep','OP':"?"},{'DEP':'agent','OP':"?"},  {'POS':'ADJ','OP':"?"}] 

    matcher.add("matching_1", [pattern],on_match=None) 

    matches = matcher(doc)
    k = len(matches) - 1
    if k < 0:
        return "ciao"
    else:
        span = doc[matches[k][1]:matches[k][2]] 
        return(span.lemma_)
        
def get_ent(docc):
    ent = [x.text for x in docc.ents]
    obj = [x.text for x in docc if "obj" in x.dep_]
    subj = [x.text for x in docc if "subj" in x.dep_]
    """print(ent)
    print([x for x in docc])
    print(obj)
    print("SUBJ",subj)
    print([x for x in ent if (not x.text in subj)])"""
    
    print("SUBJ",subj)
    print("OBJ",obj)
    out = set(ent).union(obj)
    print(out)
    print(set(subj))
    return subj, out

from Levenshtein import ratio
def NER_ext(phrases):
    NE = [[j for j in i.ents] for i in phrases]
    uni_NE, count_NE = np.unique(reduce(lambda a,b: a+b, [[y.text for y in x] for x in NE]),return_counts=True)
    
    return uni_NE,count_NE

def synonyme(entite):
    
    ratio_list = np.array([[i,j,ratio(i,j)] for i,j in itr.product(entite,entite) if (not i==j) and((len(i) > 6) or (len(j) > 6))])
    
    mask_best = np.where(ratio_list[:,2].astype(float) <0.8, False, True )
    
    return ratio_list[mask_best]
    """
    df_in = pd.DataFrame(0,index=entite,columns=entite)
    for i,j in itr.product(df_in.index,df_in.columns):
        if i == j:
            continue
        df_in.loc[i,j] = ratio(i,j)
    
    max_list = []
    for i in dff.sort_index(key=lambda x : dff.loc[x,:].max(),ascending=False).index:
        j = list(dff.columns[dff[i]==dff[i].max()])[0]
        max_list += [[i,j,dff.loc[i,j]]]"""
