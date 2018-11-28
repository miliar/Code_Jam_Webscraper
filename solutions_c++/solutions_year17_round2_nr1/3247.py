#include <iostream>
using namespace std;
#include <vector>
#include <cstdlib>

int main()
{
    int numbertestcases;
    cin >> numbertestcases;
    for (int i = 0; i < numbertestcases; i++)
    {
        // read in horses
        int destination, numberHorses;
        vector<long double> ArrivalTime;
        cin >> destination >> numberHorses;
        // figure out all times
        for (int j = 0; j < numberHorses; j++)
        {
            long double initPos, maxSpeed;
            cin >> initPos >> maxSpeed;
            ArrivalTime.push_back((destination-initPos)/maxSpeed);
        }
        // highest time (slowest speed)
        long double maxVal = ArrivalTime[0];
        for (int k = 0; k < (int)ArrivalTime.size(); k++)
        {
            if (ArrivalTime[k] > maxVal)
            {
                maxVal = ArrivalTime[k];
            }
        }
        cout.precision(100);
        cout << "Case #" << i+1 << ": " << (destination / maxVal) << endl;

    }
    return 0;
}