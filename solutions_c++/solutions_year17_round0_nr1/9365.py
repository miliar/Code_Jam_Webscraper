#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

vector<int> pank;
vector<int> flaped;

void klir()
{
    pank.clear();
    flaped.clear();
}

int check(int k)
{
    int flap = 0;
    int res = 0;

    for(int i=0; i < pank.size(); i++)
    {
        if((pank[i] + flap) % 2 == 0)
        {
            if((i + k) > pank.size() )
                return -1;
            
            flap = (flap+1) % 2;
            flaped[i+k-1] = (flaped[i+k-1]+1) % 2;
            res++;
        }

        flap = (flap + flaped[i]) % 2;
    }

    return res;
}

int main()
{
    int tests;
    cin >> tests;

    for(int x = 1; x <= tests; x++)
    {
        klir();
        string s;
        int k;

        cin >> s >> k;

        for(int i=0; i < s.size(); i++)
        {
            if(s[i] == '+')
            {
                pank.push_back(1);
            }
            else
            {
                pank.push_back(0);
            }
            flaped.push_back(0);
        }

        int res = check(k);

        cout << "Case #" << x << ": ";
        if(res == -1)
        {
            cout << "IMPOSSIBLE";
        }
        else
        {
            cout << res;
        }

        cout << "\n";
    }

    return 0;
}