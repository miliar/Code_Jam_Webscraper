#include <fstream>
#include <iostream>
#include <string>
#include <queue>
#include <math.h>

using namespace std;

int main(void)
{
    ifstream input("in.txt");
    ofstream output("out.txt");
    
    string number;
    int numCases;
    priority_queue<unsigned long long> slots;
    unsigned long long people;
    unsigned long long slotsPartition;
    unsigned long long slotsOnRight;
    unsigned long long slotsOnLeft;
    
    if (input.is_open())
    {
        input >> number;
        numCases = stoi(number);
        
        for(int i = 0; i < numCases; i++)
        {
            input >> number;
            slots.push(stoull(number));
            input >> number;
            people = stoull(number);
            
            for (int personNo=1; personNo<=people; personNo++)
            {
                slotsPartition = slots.top();
                
                slotsOnRight = floor(slotsPartition/2);
                slotsOnLeft = slotsPartition - slotsOnRight - 1;
                
                slots.pop();
                slots.push(slotsOnLeft);
                slots.push(slotsOnRight);
            }
            
            
            
            cout << "Case #" << i+1 << ": " << slotsOnRight << " " << slotsOnLeft << endl;
            output << "Case #" << i+1 << ": " << slotsOnRight << " " << slotsOnLeft << endl;
            while(!slots.empty())
                  slots.pop();
            
        }
    }
    
    else cout << "Unable to open file";
    
    return 0;
}
