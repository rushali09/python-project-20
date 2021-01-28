import turtle


class Move:
    def __init__(self, segment):
        self.segment = segment
    for seg_num in range(len(segment)-1, 0, -1):
        new_pace = segment[seg_num-1].xcor()
        new_pii = segment[seg_num-1].ycor()
        segment[seg_num].goto(new_pace, new_pii)
        segment[0].forward(20)
