#include <iostream>

using namespace std;


int main()
    {
    int test;
    cin >> test;
    string n,best;
    int d;
    for(int i=1;i<=test;i++)
        {
        cin >> n;
        d = n.length();
        best = n;
        best[0] = '0';
        for(int j=0;j<d;j++)
            {
            while(best[j]<'9')
                {
                best[j]++;
                for(int w=j+1;w<d;w++)
                    best[w] = best[w-1];
                if(best>n)
                    {
                    for(int w=j;w<d;w++)
                        best[w]--;
                    break;
                    }
                }
            }
        if(best[0]=='0')
            best.erase(0,1);
        cout << "Case #" << i << ": " << best << endl;
        }
    return 0;
    }
