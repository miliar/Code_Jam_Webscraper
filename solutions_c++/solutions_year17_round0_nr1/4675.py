// In the name of Allah

#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <iomanip>
#include <stdio.h>
#include <fstream>
#include <sstream>
#include <complex>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

#define dbg(x) cerr << #x << " = " << (x) << endl;
#define FOR(i,a,b) for (int i = (a); i < (b); i ++)
#define rep(i,n) for (int i = 0; i < (n); i ++)
#define repd(i,n) for (int i = (n); i >= 0; i --)
#define PI 3.14159265358979323846
#define pb push_back
#define mp make_pair
#define X first
#define Y second

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

ofstream fout ("A.outt");
const int max_n = 1000+10;
int sum [max_n];

char flip (char c)
{
    return (c == '+' ? '-' : '+');
}

int main ()
{
    int t;
    cin >> t;
    rep (tt, t)
    {
    	string s;
        cin >> s;
        int k;
        cin >> k;
        const int n = s.size();

        memset (sum, 0, sizeof sum);
        int ans = 0;
        rep (i, n)
        {
            if ( i > 0 )
                sum [i] += sum[i-1];
            if ( sum[i]&1 )
                s[i] = flip (s[i]);

            if ( s[i] == '-')
            {
                if ( i+k <= n )
                {
                    sum[i] ++;
                    sum[i+k] --;

                    ans ++;
                }
                else
                    ans = -1;
            }
        }
        fout << "Case #" << tt+1 << ": ";
    	if ( ans == -1 )
    	    fout << "IMPOSSIBLE" << endl;
        else
            fout << ans << endl;
    	//cout << "Case #" << tt+1 << ": " << ans << endl;
    }
    
	return 0;
}