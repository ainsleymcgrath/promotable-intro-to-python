# Ainsley's (Hopefully) Splendid Introduction to Python for First-Timers

I was lucky enough to be invited to be a guest lecturer for Chicago's newest tech-educator, [Promotable](promotable.io). The contents of this repo were used for a highly-interactive, two-session course on using Python for analytics. The students had spent several weeks learning about SQL and analytics, so given that their background was similar to mine when I got started coding, I thought it would be a good intro to try and give them _The Intro To Programming That I Wish I Had_.

## The Intro To Programming That I Wish I Had

My actual intro to programming was a trial by fire in R, which I'm not _entirely_ against to be fair. (But that's another rant.)

```R
df <- read.csv('foo.csv')
```

*"Alright, now we've got a dataframe! Let's go ahead and make a library call for dplyr..."* said my ecology professor. What? `df`? Quotes? What does the dot mean? (Often nothing, unfortunately. 😑) Suffering ensued.

We made it through somehow and I became fluent in the subregional R dialect of "life-scientist" before moving on to SQL, Python, JS, Java, and C#. A year or so of ham-fisted copy/paste code that I often couldn't explain in English passed.

By this time, I had read up. [YDKJS](https://github.com/getify/You-Dont-Know-JS), [Thoughful Machine Learning](http://shop.oreilly.com/product/0636920039082.do), and [The Impostor's Handbook](https://bigmachine.io/products/the-imposters-handbook/) get big shouts out here. I read this *excellent* [article](https://zedshaw.com/2015/06/16/early-vs-beginning-coders/) from Zed Shaw, where he made a phenomenal point about how little sense code tends to make until people learn to read a 3rd or 4th language. At that point, you realize that everything is just an *abstraction*. 

To choose a simple example, JavaScript calls them objects. In Python they're dicts. Java and C# each have One Million Different Kinds of Hash Tables. At the end of the day, they're all abstractions that let us express compartmentalized logic, easy-access storage, etc. Same metaphors different languages.

That's where I wish I had started. Having spent quite a bit of time in tutorial hell, I saw that a lot of people disagree with me. Vocab words and "expressiveness" aren't top-priority for someone trying to learn a new skill fast, but is faster better? At this point I risk writing a book, so I'll get to my actual point:

### The Point

I put together this admittedly brief intro to Python and Pandas by first laying the groundwork of programming with the ideas of abstraction and expressiveness before *anything else*. Dynamic / interactive languages leave sooo much room for doing stuff without knowing what the stuff is, and that hurts new devs in the long run. Especially given my ambitiously short time with these students, getting them literate in the English words we use to talk about Python was tantamount.

I haven't gotten enough distance from this experience yet to draw firm conclusions, but I *did* see a lot of clicks in the room. This heuristic, definition-first approach, however, did work exceedingly well during a [lecture](https://docs.google.com/presentation/d/1mV12xtjXyCZfaextUTnNkR3w4dW3Ssdg9iWY45MoIyM/edit#slide=id.p) I did in 2017 on analytics and communication. I hope to expand this approach as I continue finding opportunities to educate.