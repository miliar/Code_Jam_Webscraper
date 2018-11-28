#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
    ifstream input("in.txt");
    ofstream output("out.txt");
    string pancakes;
    int flipper;
    int numCases;
    
    if (input.is_open())
    {
        input >> numCases;
        
        for(int i = 0; i < numCases; i++)
        {
            int flips = 0;
            input >> pancakes;
            input >> flipper;
            
            for(int j = 0; (j+(flipper-1))<pancakes.length(); j++)
            {
                if(pancakes[j] == '-')
                {
                    for(int k=0; k<flipper; k++)
                    {
                        if(pancakes[j+k] == '-')
                        {
                            pancakes[j+k] = '+';
                        }
                        else
                        {
                            pancakes[j+k] = '-';
                        }
                    }
                    flips++;
                }
            }
            
            bool isPossible = true;
            for(int i = 0; i < pancakes.length(); i++)
            {
                if(pancakes[i] == '+')
                    continue;
                else
                {
                    isPossible = false;
                    break;
                }
            }
            
            if(isPossible)
            {
                cout << "Case #" << i+1 << ": " << flips << endl;
                output << "Case #" << i+1 << ": " << flips << endl;
            }
            else
            {
                cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
                output << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
            }
            
        }
    }
    
    else cout << "Unable to open file";
    
    return 0;
}



//go to first '-' and flip next K pancakes
//go to next '-' and flip next K pancakes

//check end bounds
//after 1 pass quit out? when to give up?
