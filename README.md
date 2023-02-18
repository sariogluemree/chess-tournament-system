# chess-tournament-system
The International Chess Federation (FIDE) has requested the development of a program based on rules similar to the Swiss System pairing rules, to make pairings in each round and to display the success rankings and cross-table at the end of the tournament for use in individual chess tournaments. For this, the following information will be entered into the program for each player participating in the tournament:

License number (LNo): An odd unique integer greater than 0 (entering 0 or a negative value will indicate that there is no other player.)
Name-Surname: They should be used in uppercase and compatible with Turkish in the program (assume that only 29 letters and the space character in Turkish will be entered).
International (FIDE) rating (ELO): An integer of 0, 1000 or more (0 if there is no ELO rating)
National rating (UKD): An integer of 0, 1000 or more (0 if there is no UKD rating)
At the beginning of the tournament, all players' scores (referred to as Points hereafter) are 0. Players are ranked according to the following criteria for pairing purposes at the beginning and before each round (priority of criteria decreases downwards):
Points (descending order)
ELO (descending order)
UKD (descending order)
Name-Surname (Alphabetic order compatible with Turkish)
LNo (ascending order)
At the beginning, a starting ranking list is created by ranking all players as described above, and players are given a starting serial number (BSNo) starting from 1 for use in pairings. The starting ranking list is displayed as follows:
BSNo LNo Name-Surname ELO UKD
Later, the number of rounds in the tournament and the color (b/w) of the first player in the first round according to the starting ranking are entered into the program. In the first round, those with an odd BSNo take this color, and those with an even BSNo take the other color. The number of rounds cannot be less than the number found by rounding up the logarithm of the number of players to base 2 and cannot be greater than one less than the number of players.
The general rules of the Swiss System are as follows:

There is no elimination, all players play in all rounds.
Two players can only play once.
Two players paired with each other should have the same score or as little difference as possible between their scores.
If the number of players is odd, the lowest player in the ranking list before the round is not paired, passes that round (BYE), and gets no color and 1 point.
A player who has previously scored without playing in any round, either because their opponent did not come or because they passed that round, cannot pass the round again in that round.
If possible, players take the opposite color of the previous round. If possible, players take black and white equally.
No player can get the same color three times in a row. A player with the same color twice in a row gets the opposite color in the next round.
