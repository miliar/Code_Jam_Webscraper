#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <climits>
#include <ctime>
#include <algorithm>
#include <string>
#include <set>
#include <cmath>
#include <map>

using namespace std;


int main()
{
    int n;
    cin >> n;


    for(int i = 0; i < n; i++)
    {
        int k;
        string s;
        cin >> s;
        cin >> k;

        //cout << s << endl;

        int indice = 0;
        int nb = 0;

        for(int j = 0; j < s.size() - k + 1; j++)
        {
            if(s[j] == '+')
                continue;
            else
            {
                nb++;
                for(int x = 0; x < k; x++)
                {
                    if(s[j + x] == '-')
                        s[j + x] = '+';
                    else
                        s[j + x] = '-';
                }
            }
        }

        bool good = true;
        for(int j = 0; j < s.size(); j++)
        {
            if(s[j] == '-')
                good = false;
        }

        if(good)
            cout << "Case #" << i+1 << ": " << nb << endl;
        else
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
    }
}
