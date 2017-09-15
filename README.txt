A basic calculator that doesn't use numbers. Intead, all numbers are represented by nested tuples.
For example, 0 is (), 1 is ((),), 2 is (((),),) and so on. Even internally only tuples are used.
Some functions, like add() and mul(), can take any number of arguments (at least one) or a single container.
A container is a tuple which contains at least two number-type tuples and nothing else.
A container which only contains a single number-type tuple is actually that numbers successor (increment).
The functions gen() and rev() convert between integers and tuple numbers, and are exempt from the "tuples only" rule.
