#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-soln.out","w",stdout);
    int trials;
    cin >> trials;
    int initrials = trials + 1;
    while (trials > 0)
    {
        string candidate, resultant;
        int repcount = 0;
        bool done = false;
        cin >> candidate;
        cout << "Case #" << initrials - trials << ": ";
        for (int i=0; i<=candidate.size()-1; i++)
        {
            if (candidate[i] == '0')
            {
                for (int i=1; i<=candidate.size()-1; i++)
                    cout << "9";
                cout << endl;
                done = true;
                break;
            }
            else if (i < candidate.size()-1)
            {
                if (candidate[i+1] == '0')
                {
                    if ((candidate[i-repcount] != '1') || (i-repcount != 0))
                        resultant += (candidate[i-repcount] - 1);
                    cout << resultant;
                    for (int j=i+1-repcount; j<=candidate.size()-1; j++)
                        cout << "9";
                    cout << endl;
                    repcount = 0;
                    done = true;
                    break;
                }
                else if(candidate[i] > candidate[i+1])
                {
                    resultant += (candidate[i-repcount] - 1);
                    cout << resultant;
                    for (int j=i+1-repcount; j<=candidate.size()-1; j++)
                        cout << "9";
                    cout << endl;
                    repcount = 0;
                    done = true;
                    break;
                }
                else if(candidate[i] == candidate[i+1])
                    ++repcount;
                else
                {
                    while(repcount > 0)
                    {
                        resultant += candidate[i];
                        --repcount;
                    }
                    resultant += candidate[i];
                }
            }
            else
            {
                while(repcount > 0)
                {
                    resultant += candidate[i];
                    --repcount;
                }
                resultant += candidate[i];
            }
        }
        if(!(done))
            cout << resultant << endl;
        --trials;
    }
    return 0;
}
