#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long int ULLI;
typedef long long int LLI;

int main(int argc, char** argv)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    ULLI n;
    cin >> n;
    for(ULLI i=0; i<n; i++)
    {
        string row;
        ULLI k;
        bool poss = true;
        ULLI count = 0;
        cin >> row;
        cin >> k;
        for(ULLI j=0; j<row.length(); j++)
        {
            if(row[j] == '-')
            {
                count++;
                if(j+k>row.length())
                {
                    poss = false;
                    break;
                }
                else
                {
                    for(ULLI l=j; l<j+k; l++)
                    {
                        if(row[l] == '-')
                            row[l] = '+';
                        else
                            row[l] = '-';
                    }
                }
            }
        }
        cout << "Case #" << i+1 << ": ";
        if(poss)
            cout << count << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
