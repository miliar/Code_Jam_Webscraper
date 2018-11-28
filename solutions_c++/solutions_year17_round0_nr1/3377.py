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
#define forsn(i,s,n) for(int i=int(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=int(n)-1;i>=0;i--)
#define dforsn(i,s,n) for(int i=int(n)-1;i>=(int)(s);i--)

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

char flip(char x)
{
    return (x == '-') ? '+' : '-';
}

string calc(string s, int k)
{
    int total = 0;
    forn(i,s.size()-k+1)
    if (s[i] != '+')
    {
        total++;
        forn(j,k)
            s[i+j] = flip(s[i+j]);
    }
    forsn(i,s.size()-k+1, s.size())
    if (s[i] != '+')
        return "IMPOSSIBLE";
    return to_string(total);
}

int main()
{
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        string s; int k;
        cin >> s >> k;
        string res = calc(s,k);
		cout << "Case #" << caso + 1 << ": " << res << endl;
		cerr << "Case #" << caso + 1 << ": " << res << endl;
	}
	return 0;
}
