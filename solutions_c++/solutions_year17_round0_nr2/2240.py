#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <cstring>

#define ll long long
#define f first
#define s second
#define INF (int)(1e9 + 7)
#define EPS (1e-6)
#define pb push_back
#define mp make_pair

using namespace std;
int n, o, m, y, r;
bool was;
string s;
char d[5000];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin >> m;

    for (int h = 1; h <= m; h++)
    {
        cin >> s;
        n = s.length();
        cout << "Case #" << h << ": ";
        while (true)
        {

            o = n;
            was = false;
            y = 0;
            for (int j = 0; j < n - 1; j++)
                if (s[j] > s[j + 1])
                {
                    o = j;
                    break;
                }
            if (o == n)
                break;


            for (int j = 0; j < o; j++){
                d[y] = s[j];
                y++;
                //cout << s[j];
                was = true;
            }
            if (o < n)
            {
                d[y] = char(s[o] - 1);
                y++;
            }

            for (int j = o + 1; j < n; j++)
            {
                d[y] = '9';
                y++;
            }

            for (int r = 0; r < n; r++)
                s[r] = d[r];

            while (s[r] == '0')
                r++;
            //for (int i = r; r < n; r++)
              //  cout << s[r];
        }

        r = 0;
        while (s[r] == '0')
            r++;
        for (int i = r; r < n; r++)
            cout << s[r];
        cout << endl;
    }



    return 0;
}
