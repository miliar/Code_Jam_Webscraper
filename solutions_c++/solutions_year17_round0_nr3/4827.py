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

ofstream fout ("C.out");
priority_queue <pair<int, int> > Q;

int main ()
{
    int t;
    cin >> t;
    rep (tt, t)
    {
        while ( Q.size() )
            Q.pop();

        int n, k;
        cin >> n >> k;

        Q.push (mp(n, 0));
        int cnt;
        rep (i, k)
        {
            cnt = Q.top().first;
            int at = -Q.top().second;
            Q.pop();

            if ( (cnt-1)>>1 > 0 )
                Q.push (mp((cnt-1)>>1, -at));
            if ( cnt>>1 > 0 )
                Q.push (mp(cnt>>1, (((cnt+1)>>1)+at)));
        }

    	fout << "Case #" << tt+1 << ": " << cnt/2 << " " << (cnt-1)/2 << endl;
    }
    
	return 0;
}