#include <iostream>

using namespace std;

typedef struct
{
    long long speed;
    long long initPos;
} horse;

horse slowestHorse(horse horses[], int horselen)
{
    horse slowestHorse = horses[0];

    for (int i = 1; i < horselen; i++)
    {
        if (horses[i].speed < slowestHorse.speed)
        {
            slowestHorse = horses[i];
        }
    }

    return slowestHorse;
}

double singlehorse(double totalDist, horse horse)
{
    double dSlowest = totalDist - horse.initPos;
    double timeSlowest = dSlowest / horse.speed;
    return totalDist / timeSlowest;
}

double multipleHorses(double totalDist, horse horses[], int totalHorses)
{
    double minSpeed = singlehorse(totalDist, horses[0]);
    for (int i = 1; i < totalHorses; i++)
    {
        float thisHorse = singlehorse(totalDist, horses[i]);
        if (thisHorse < minSpeed)
            minSpeed = thisHorse;
    }

    return minSpeed;
}

int main()
{
    int testCases;

    cin >> testCases;

    for (int i = 1; i <= testCases; i++)
    {
        int destination, numberOfHorses;

        cin >> destination >> numberOfHorses;

        horse horses[1000] = { 0 };

        for (int j = 0; j < numberOfHorses; j++)
        {
            cin >> horses[j].initPos >> horses[j].speed;
        }

        printf("Case #%d: %8f\n", i, multipleHorses(destination, horses, numberOfHorses));        
    }

    return 0;
}
