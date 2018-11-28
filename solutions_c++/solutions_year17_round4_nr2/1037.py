#include <cstdio>
#include <list>
#include <map>

using namespace std;

int promotionAnswer;

int seats[1000];
int seatHint[1000];

bool isPossible(map<int, list<int>> &allTickets, int roundCount, int seatCount)
{
    promotionAnswer = 0;
    for (int i = 0; i < seatCount; i++)
    {
        seats[i] = 0;
        seatHint[i] = i;
    }

    for (auto &ticketPerCustomer : allTickets)
    {
        for (auto &wantedSeat : ticketPerCustomer.second)
        {
            // printf("[%d]", wantedSeat);
            int lookupSeat = seatHint[wantedSeat];

            while (lookupSeat >= 0 && seats[lookupSeat] >= roundCount)
            {
                lookupSeat--;
            }

            if (lookupSeat >= 0)
            {
                // printf(" => %d\n", lookupSeat);
                if (lookupSeat != wantedSeat)
                {
                    promotionAnswer++;
                }
                seats[lookupSeat]++;
                seatHint[wantedSeat] = lookupSeat;
            }
            else
            {
                // printf("NOPE\n");
                return false;
            }
        }
    }

    return true;
}

void testcase()
{
    int seatCount, customerCount, ticketCount;
    map<int, list<int>> tickets;

    scanf("%d %d %d", &seatCount, &customerCount, &ticketCount);
    for (int i = 0; i < ticketCount; i++)
    {
        int person, seat;
        scanf("%d %d", &seat, &person);
        tickets[person - 1].push_back(seat - 1);
    }

    int minPossibleAnswer = 1;
    int maxPossibleAnswer = 1001;

    for (auto &ticketsOfPerson : tickets) {
        int temp = ticketsOfPerson.second.size();
        if (temp > minPossibleAnswer) {
            minPossibleAnswer = temp;
        }
    }

    int promotion;

    while (minPossibleAnswer < maxPossibleAnswer)
    {
        int roundCount = (minPossibleAnswer + maxPossibleAnswer) / 2;
        // printf("[%d]\n", roundCount);
        if (isPossible(tickets, roundCount, seatCount))
        {
            maxPossibleAnswer = roundCount;
            promotion = promotionAnswer;
        }
        else
        {
            minPossibleAnswer = roundCount + 1;
        }
    }

    printf("%d %d\n", minPossibleAnswer, promotion);
}

int main()
{
    int tc;
    scanf("%d", &tc);
    for (int t = 1; t <= tc; t++)
    {
        printf("Case #%d: ", t);
        testcase();
    }
    return 0;
}
