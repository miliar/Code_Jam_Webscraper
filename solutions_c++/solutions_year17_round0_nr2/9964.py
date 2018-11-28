#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>

#define NAME "B-large"
#define FOR(i, a, b) for(int i = (a), _b = (b); i <= _b ; ++i)
#define FORD(i, a, b) for(int i = (a) , _b = (b) ; i >= _b ; --i)
#define pb push_back
#define ll long long

using namespace std;
string s;
int a[20];
int n;
int t;
void io()
{
    freopen(NAME".in","r",stdin);
    freopen(NAME".out","w",stdout);
}
int main()
{
    io();
    cin >> t;
    FOR(k, 1, t)
    {
        cin >> s;
        n = s.size();
        FOR(i, 0, n - 1)
        {
            a[i + 1] = s[i] - '0';
        }
        FOR(l, 1, 20)
        {
            FOR(i, 1, n - 1)
            {
                if(a[i] <= a[i + 1]) continue;
                if(a[i] > a[i + 1])
                {
                    a[i]--;
                    FOR(j, i + 1, n) a[j] = 9;
                    break;
                }
            }
        }
        bool ok = true;
        cout << "Case #" << k << ": ";
        FOR(i, 1, n)
        {
            if(ok && a[i] == 0) continue;
            if(a[i] != 0) ok = false;
            if(!ok) cout << a[i];
        }
        cout << "\n";
    }
    return 0;
}
