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
