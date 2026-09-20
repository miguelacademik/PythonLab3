 **How encapsulation and generalization helped us break down the drawing process for this scene?**
 
 Instead of writing a long script full of raw t.forward()/left() calls, the code hides those pen movements inside
functions with more meaningful names and fucntions.

For example the draw_square, draw_circle, draw_polygon encapsulated how to draw those shapes so the caller does not
need to think the angles or the turtle mechanics at all.
The jump(t, x, y) encapsulate the pen-up-down move sequence. Anywhere else in hte code we just say "jump here or there"
instead of repeating three lines of turtle positioning.
draw_jack encapsulated an entire face by calling the lower-level part functions. From outside, draw_jack(t, x, y, radius)
looks like stand alone action, even though internally  it is five calls doing coordinate math.

By using parameters one single function handles many others. Instead of a functions that draws one specific pumpkin,
draw_pumpking(t, x, y, radius) takes position and size as parameters, so the code produces pumpkins of any size, 
anywhere on the screen, and always keeping the same proportions.

Together, they built a complex scene from a small reusable, readable function instead of one giant script.