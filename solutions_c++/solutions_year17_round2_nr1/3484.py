#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <iomanip>

using namespace std;

int main(void)
{
    ifstream input("in.txt");
    ofstream output("out.txt");
    
    unsigned long long number;
    int numCases;
    
    if (input.is_open())
    {
        input >> number;
        numCases = number;
        
        for(int i = 0; i < numCases; i++)
        {
            input >> number;
            int destination = number;

            input >> number;
            int otherHorses = number;

            double* timeToArrive = new double [otherHorses];
            double maxTimeToArrive = 0;
            
            for(int k=0; k<otherHorses; k++)
            {
                input >> number;
                int initialPosition = number;
                
                input >> number;
                int maxSpeed = number;
                

                int distanceToTravel = destination - initialPosition;
                timeToArrive[k] = (double)distanceToTravel / maxSpeed;
                
                if(timeToArrive[k] > maxTimeToArrive)
                    maxTimeToArrive = timeToArrive[k];
            }
            
            float speed = (float)destination / maxTimeToArrive;
            
            cout << "Case #" << i + 1 << ": " << setiosflags(ios::fixed) << setprecision(6) << speed << endl;
            output << "Case #" << i + 1 << ": " << setiosflags(ios::fixed) << setprecision(6) << speed << endl;
            
        }
    }
}
