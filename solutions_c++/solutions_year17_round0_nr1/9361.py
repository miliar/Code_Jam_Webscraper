#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int check(string & s, int length)
    {        
        for(int i=0; i<length; i++)
            {
                if(s[i] == '-')
                    return i;
            }
        return -1;
    }

int main()
{
    int t;
    cin >> t;
    for(int i=1; i<=t; i++)
        {
            string s;
            int flips;
            cin >> s >> flips;
            int length = s.length();
            int counter = 0;
            while(true)
                {
                    int result = check(s, length);
                    if(result == -1)
                        {
                            cout << "Case #" << i << ": " << counter << endl;
                            break;
                        }
                    else
                        {
                            if((length-result) < flips)
                                {
                                    cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
                                    break;
                                }
                            else
                                {
                                    for(int k=result; k<result+flips; k++)
                                        {
                                            if(s[k] == '+')
                                                s[k] = '-';
                                            else if(s[k] == '-')
                                                s[k] = '+';
                                        }
                                }
                                
                        }
                    ++counter;
                }
        }   
    return 0;
}
