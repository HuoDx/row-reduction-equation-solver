Row Reduction Equation Solver
===

**This is a tutorial for BIGINNER/INTERMEDIATE high school Python leaners and math learners**

In math class we have learned how to solve systems of equations using row reductions. By multiplying and adding/subtracting the rows, we can easily eliminate variables. (it's just all about factors!) 

However that's kind of "humane" to me - this method of row reduction is supposed to be an algorithm, but it seems that what we have learned on class still involves some human intuition (sth like "little inspiration on how to solve such as finding some subtle values"). Besides, we have only learned how to do the 3x3 system of equations, but it seems that it has the potential to be easily expanded to a larger scale (with more variables).  

So I came up with this idea to program this using Python. After having a conversation with Mr. Peter (our math teacher), I got confirmed that this is doable and got some very helpful suggestions from him. So then quickly I wrote this little program to do it.

Hopefully this can act as a little demonstration of the row reduction process in a more "general" way (as it is a computer algorithm). Also for some of my friends who just started to code in Python, this could show you how to program in Python ;D

What you can learn:

- Math:
  - How to do row reduction to solve a system of equations
- Coding:
  - How to program in Python
  - The concept of divide and conquer
  - Application of recursion
  - Some coding techniques (don't use them in actual projects! They are not that readable!)

So here let me briefly go through again about the row reduction process:

The key idea of solving a system of equations is **eliminating terms**. Row reduction introduces a simple but general method: eliminating variables by making the factors of them the same and then subtract the two rows. By doing so, we obtain a new row of equation with one variable eliminated. 

Notice that as I mentioned above, we need two equations to eliminate one variable. That is to say, we can say that it is the relationship of two equations eliminates that one variable. Bearing this in mind, let's then see how many relationships do we have if we are given n equations (in a system): we can then arrive to  $ n \cdot (n-1) $ easily.

Well, this is (apparently) because for each equation, it can has a relationship with the rest n-1 equations, each time eliminating one variable. Therefore, for an equation, it can be used to eliminate a variable for a maximum of n-1 equations. Therefore, after doing so, we arrive at a new smaller system of equation that has exactly one variable and equation less.

Then we can repeat the exact same process over and over again, eventually arriving to one variable with one remaining equation. Then, by simple division, we can obtain that value. 

After we started to have the first initial value, we can therefore get one variable more by applying the value into the system of equation that we used to derive the one remaining equation - a system with only two variables. As we know one of the two, we can obtain the other. After that we can repeat this process of applying values and getting variables solved for all variables.

Now I will talk a little about the coding part.

For the above description, we break a problem to smaller pieces and conquer the problem using the exact same method we use to conquer the pieces, until the piece itself is simplified enough that we can directly get solutions. This concept of solving problems is called **divide and conquer**. As for the code implementation, recursion is being used to implement the divide and conquer method. For further understanding, see the code.

Besides, I used some Python tricks to make the code easier to program, though it introduces additional complexity in computation and can be very confusing. Here is an example of that:

```Python 
if not False in [0 == e for e in reduced_row[:-1]]:
	# do something
	pass
```

where `reduced_row` is a list that contains a few numbers. 

As you can see, the code itself looks terrible indeed, but it does do the job in one line. Just to mention, the statements within the if statement is executed if all values in `reduced_row` is `0`.

Other things are easier to understand: see the code - there are a lot of comments.



Finally, I hope this project could be of at least some help to you!