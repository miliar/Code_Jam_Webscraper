#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(int)(s);i--)

#define forall(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(),(c).end()

#define esta(x,c) ((c).find(x) != (c).end())
#define zMem(c) memset((c),0,sizeof(c))

typedef long long tint;
typedef long double tdbl;

typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vstr;

tint v[64][64];
tint rat[64];

int main()
{
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        int N,P; cin >> N >> P;
        forn(i,N) cin >> rat[i];
        forn(i,N)
        forn(j,P)
            cin >> v[i][j];
        forn(i,N) sort(v[i], v[i] + P);
        vector<tint> activ;
        forn(i,N)
        forn(j,P)
            activ.push_back((10LL*v[i][j] + 11LL * rat[i] - 1) / (11LL * rat[i]));
        sort(all(activ));
        vector<int> next(N, 0);
        int res = 0;
        for (tint k : activ)
        {
            forn(i,N)
            {
                while (next[i] < P && 10LL * v[i][next[i]] < 9LL * rat[i] * k) next[i]++;
                if (next[i] == P) goto outofit;
            }
            forn(i,N) if (10LL * v[i][next[i]] > 11LL * rat[i] * k) goto nextk;
            res++;
            forn(i,N) if (++next[i] == P) goto outofit;
nextk:;
        }
outofit:;
		cout << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}
