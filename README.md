Trial 0 - Default Python Hash:
    -- Movies By Title Hash Statistics -- 
    Wasted Space: 7079
    Collisions: 3388
    Construction time (ns): 29478500

    -- Movies By Quote Hash Statistics -- 
    Wasted Space: 5566
    Collisions: 5457
    Construction time (ns): 18916100

Trial 1 - Linked List Poor Hash:

    Optimization: No optimization, tried a function known to be
    a poor hash function, just adding the character ascii codes.

    This approach was chosen because it's the first solution that
    comes to mind, but as such has problems: words that contain the same letters ("odor" and "door") will have the same hash value, so collisions are expected. Since this is using
    a linked list, more wasted space is also expected.

    -- Movies By Title Hash Statistics -- 
    Wasted Space: 11244
    Collisions: 28458
    Construction time (ns): 31876100

    -- Movies By Quote Hash Statistics -- 
    Wasted Space: 12277
    Collisions: 56049
    Construction time (ns): 38680700

Trial 2 - Linked List Better Hash:

    Optimization: Left shift each character, making it so that the letter order is accounted for.
    Less collisions/wasted space is expected.

    -- Movies By Title Hash Statistics -- 
    Wasted Space: 7982
    Collisions: 7978
    Construction time (ns): 38093600

    -- Movies By Quote Hash Statistics -- 
    Wasted Space: 7105
    Collisions: 12484
    Construction time (ns): 230938600

Trial 3 - Linear Poor Hash:

    Optimization: Switch from linked list to linear list. Trying the poor hash function from Trial 1.

    Zero wasted space is expected in all cases because the list has the same length as the file containing the movies, so it should be 1:1. The reason there is wasted space is because any duplicate keys are replaced. This is also true for the linked list implementation. I chose not to handle this to highlight these duplicate key cases.

    -- Movies By Title Hash Statistics -- 
    Wasted Space: 3691
    Collisions: 54250752
    Construction time (ns): 4540318300

    -- Movies By Quote Hash Statistics -- 
    Wasted Space: 109
    Collisions: 91702029
    Construction time (ns): 6599335400

Trial 4 - Linear Better Hash:

    Optimization: Switch to same function from Trial 2, but with linear list.

    -- Movies By Title Hash Statistics -- 
    Wasted Space: 3691
    Collisions: 22253
    Construction time (ns): 35765100

    -- Movies By Quote Hash Statistics -- 
    Wasted Space: 109
    Collisions: 398475
    Construction time (ns): 269297200

Trial 5 - Linear Better Hash with Modulo:

    Optimization: Modulo the current hash function by a reasonably sized odd number. This is to prevent the number from blowing up too large, hopefully reducing construction time.

    I chose the linear list case for this trial. Could have gone with a linked list as well, both trials 4 and 2 performed very similarly to each other. 

    -- Movies By Title Hash Statistics -- 
    Wasted Space: 3691
    Collisions: 18592
    Construction time (ns): 42007600

    -- Movies By Quote Hash Statistics -- 
    Wasted Space: 109
    Collisions: 883904
    Construction time (ns): 161344200



Compressed statistics:

        W.S.     Coll.       C.T.
    
T1     11244      28458     31876100
Q1     12277      56049     38680700
T2      7982       7978     38093600
Q2      7105      12484    230938600
T3      3691   54250752   4540318300
Q3       109   91702029   6599335400
T4      3691      22253     35765100
Q4       109     398475    269297200
T5      3691      18834     36564000
Q5       109     495813    106699100


The poor hash function was tested in trials 1 and 3 against a linked list and linear list respectively. The better hash function was tested in trials 2 and 4, and the final hash function was tested in trial 5 against a linear list.

Trial 1 resulted in nearly double the wasted space as in trial 2. This is because in the linked list case, when the hash function returns the same value for 2 different keys, those go into the same bucket, wasting space. If there was no wasted space in the linked list, each pair would be in a different bucket. This disparity does not appear across trials 3 and 4, because the linear list does not have buckets.

The poor hash function resulted in more than double the collisions for the linked list case, and several orders of magnitude more collisions in the linear list case. The reason why the poor function has more collisions is because words that contain the same letters will result in the same hash value, causing more collisions. The collisions are so much higher in the linear case because as the list fills up more and more, each new value has to walk further and further to find an open space from its hash index as the table fills up.

Construction time was lowest in trial 1. This is because the main limiting factor is the speed of the hash function itself. The poor hash function ends up running much faster than either improved version. Of course, for trial 3, this doesn't matter because the limiting factor for construction time ends up being the massive number of collisions as the list fills up.

The attempt to optimize construction time by introducing that modulo was successful for the movie quotes case only. This is because the quotes are much longer than the titles, so in Q4 the running total becomes longer than 64 bits more often, resulting in the computer having to use more resources to do the calculations. Since the titles are short, this optimization ends up actually hurting T5, because the new modulo ends up causing more overlap between hash values.