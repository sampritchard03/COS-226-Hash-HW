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

