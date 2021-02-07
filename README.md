# DESCRIPTION: 

Algorithm to draw Hasse diagram of the given relations in ”input.txt”.
Your code should meet the following requirements, standards and accomplish the given tasks.

• Read the relations from the text file ”input.txt”.

• Determine each relation in ”input.txt” whether it is reflexive, symmetric, anti-symmetric and transitive
with your algorithm from HW2.

• In order to draw Hasse diagram, each relation must be POSET. Hence, the relation obeys the following
rules:
– Reflexivity

– Anti-symmetric

– Transitivity

If the relation is not a POSET, your algorithm is responsible to CONVERT it to POSET.
– If the relation is not reflexive, add new pairs to make the relation reflexive.

– If the relation is symmetric, remove some pairs which make the relation symmetric. For instance, if the relation has (a, b) and (b, a), remove one of them
randomly.

– If the relation is not transitive, add new pairs which would make the relation transitive.

• After the relation becomes POSET, your algorithm should obtain Hasse diagram of the relation and write
the diagram with the following format.

– In ”output.txt”, each new Hasse diagram starts with ”n”.

– The relation is (a, a), (a, b), (a, e), (b, b), (b, e), (c, c), (c, d), (d, d), (e, e)

– The relation is already a POSET so we don’t need to add or remove any pairs.

– After ”n”, write the POSET in the next line as it is shown in ”exampleoutput.txt”.

– Since the relation is POSET, it becomes (a, b), (b, e), (c, d) after removing reflexive and transitive
pairs.

– The following lines give each pair of Hasse diagram.
