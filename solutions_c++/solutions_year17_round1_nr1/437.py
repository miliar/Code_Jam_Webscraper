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

string g[64];

void solve(string &s)
{
    char prev = '?';
    bool isFirst = true;
    forn(i,s.size())
    if (s[i] == '?')
        s[i] = prev;
    else
    {
        if (isFirst)
        {
            isFirst = false;
            forn(j,i)
                s[j] = s[i];
        }
        prev = s[i];
    }
}

int main()
{
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        int R,C; cin >> R >> C;
        forn(i,R)
        {
            cin >> g[i];
            solve(g[i]);
        }
        forn(j,C)
        {
            string s;
            forn(i,R) s += g[i][j];
            solve(s);
            forn(i,R) g[i][j] = s[i];
        }
        
		cout << "Case #" << caso + 1 << ": " << endl;
        forn(i,R)
        {
            forn(j,C)
                cout << g[i][j];
            cout << endl;
        }
		//cerr << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}
