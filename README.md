# chess-tournament-system
RULES
For use in individual chess tournaments, the International Chess Federation (FIDE)
in each round, based on rules similar to the Swiss System matchmaking rules established by
to make matches, view the ranking and crosstab at the end of the tournament
a program is to be developed. For this, first of all, for each player participating in the tournament
The following information will be entered into the program:
  * License number (LNo): a unique integer greater than 0 (0 or a negative value)
  Entering it will indicate that there are no other players.)
  * Name-surname: in the program, all of them are capitalized and in harmony with Turkish.
  should be used (assume that only 29 letters and spaces in Turkish will be entered).
  * International (FIDE) strength score (ELO): 0, 1000 or greater integer (ELO score)
  otherwise 0)
  * National strength score (UKD): 0, 1000 or greater integer (0 if there is no UKD score)
At the start of the tournament, all players' tournament points (hereinafter referred to as Points)
will be mentioned) is 0. At the start and before each round, players must match the following
they are sorted by criteria (criteria decreasing in priority):
  1. Score (from largest to smallest)
  2. ELO (from largest to smallest)
  3. UKD (from largest to smallest)
  4. Name-surname (in alphabetical order compatible with Turkish)
  5. LNo (from smallest to largest)
Initially, all players are sorted as described above, with an initial ranking list.
are created and according to this list, players are offered to use in matchmaking, starting with 1
a starting sequence number (BSNo) is given. The initial ranking list created is as follows:
displayed as:
BSNo LNo Name-Surname ELO UKD
---- ----- ------------ ---- ----
Then, according to the number of rounds in the tournament and the starting order, the color of the first player in the first round
(b/s) is entered into the program. In the first round, those with an odd BSNo get this color, and those with an even BSNo get the other color. Type
number; of the base 2 logarithm of the number of players to the nearest integer upwards
It cannot be less than the number found by rounding and more than 1 less than the number of players.
The general rules of the Swiss System are as follows:
  * There is no elimination, all players play in all rounds.
  * Two players can play each other only once.
  * Two players paired with each other, with equal points or the difference in points between them as much as possible.
  should be less.
  * If the number of players is odd, the lowest player in the ranking made before the round is not matched in that round,
  skips a round (BYE passes that round), has no color and gets 1 point.
  * Points without playing in the previous rounds, either because the opponent did not come or because he skipped a round.
  A player who has taken the title cannot be circumvented in that round.
  * If possible, players take the opposite color of their color in the previous round. If possible,
  Players get equal numbers of black and white colors.
  * No player can take the same color three times in a row. A player can choose one color more than the other.
  It may take more than 2 times too.
  * Lap jumps are not taken into account in the color calculation.
Before each round, the players are lined up as previously stated, starting with the first player.
in turn, each unpaired player is placed on the tables, with a suitable opponent
numbers (MNo) start from 1). For this, within the framework of the general rules above, the following
method is followed (as a result of following the steps given below, the pairings will go smoothly.
You can assume it can be done in the following way):
  0. If the number of players is odd, go round to the lowest ranked player whose status complies with the round skip rule
  1. The following priority within the group of players with the same score as the opposing searched player
  Search for competitors in order:
  1.1. In the previous round, the opposing wanted player is given the opposite color of the color he took in the previous round.
  the closest player in the standings will get the opposite color of the color he has taken.
  1.2. In the previous round, the opposing wanted player is given the opposite color of the color he took in the previous round.
  will get the same color as the color he bought (if it is not against the color rules), the closest in the ranking
  actor
  1.3. By giving the opposing sought-after player the same color as the one received in the previous round (in accordance with the color rules).
  (unless it is contrary) will take the opposite color of the color taken in the previous round,
  actor
  2. If no suitable opponent is found, 1.1, 1.2 and 1.3 over a subgroup of players
  repeat your steps in order
  3. Repeat step 2 until a suitable opponent is found
After all matchmaking is complete, the matchmaking list for that round is as follows:
is displayed (if there is a lap player, it is indicated at the end and BYE is written in front of it):
    Whites Blacks
  MNo BSNo LNo Score - Score LNo BSNo
  --- ---- ----- ---- ---- ----- ----
The result of each match played in this round is then entered into the program with the following numbers (0-5):
  0: draw, ie match result ½ - ½
  1: white is the winner, so the result is 1 - 0
  2: black is the winner, so the match result is 0 - 1
  3: black did not come to the match, ie the result of the match + - -
  4: white did not come to the match, so the result of the match - - +
  5: neither player came to the match, ie match result - - -
Players' points at the end of the tournament are determined by adding up the points they have earned in the matches.
1 point is awarded for a win, 0.5 points for a draw, and 0 points for a loss. rival
The player who does not show up or skips the round gets 1 point, the player who doesn't come to the match gets 0 points. Tournament
the following tiebreak criteria to determine the ranking of players who score tied at the end
is applied (criteria decrementing in priority):
  * Buchholz-1 from the bottom (BH-1): Other than the 1 opponent with the lowest score, his opponents
  sum of points
  * Buchholz-2 from under (BH-2): Other than the 2 lowest scoring opponents,
  sum of points
  * Sonneborn Berger (SB): The points scored by the defeated opponents and the draw
  the sum of half of the opponents' points
  * Number of Wins (GS): The number of matches won by playing and the opponent did not come
When calculating BH-1, BH-2 and SB points, unplayed matches (either round skip or opponent's
for each round remaining to the points the player himself has earned up to that round, for
The score found by adding 0.5 points is taken into account.
After all rounds have been completed, the players' points and the tiebreak mentioned above
Final ranking list with sequence numbers (SNo) starting from 1, taking into account the criteria
is created and displayed as follows:
  SNo BSNo LNo Name-Surname ELO UKD Point BH-1 BH-2 SB GS
  --- ---- ----- ------------ ---- ---- ---- ---- ---- ----
Finally, the crosstab showing the matches played by all players, in order of starting
sequentially displayed as follows:
  BSNo SNo LNo Name-Surname ELO UKD 1st Round ... N. Round Points BH-1 BH-2 SB GS
  ---- --- ----- --------- ---- ---- ------- ... ------- ---- ---- ---- ---- --
In the crosstab, for each round in which a player is matched against another player; opponent's player
the starting sequence number, the color of the player (b/s) and the result of the match for the player are one in between
It is written with spaces, the following characters are used for the match result:
  1: win
  0: defeat
  ½: tie (the ASCII code of the ½ character is 171)
  +: the opponent did not come
  -: he did not come
If the player has made a round (not matched) in a round, the opposing player for that round in the crosstab and
The color is indicated by the - character, while the result of the match is indicated by 1.
