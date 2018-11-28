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

int main()
{
	int totalCasos;
	cin >> totalCasos;
	forn(caso,totalCasos)
	{
        int N,K; cin >> N >> K;
        deque<int> dh, dl;
        dh.push_back(N);
        int h=0,l=0;
        forn(i,K)
        {
            int next;
            if (dh.empty() || (!dl.empty() && dl.front() > dh.front()))
            {
                next = dl.front();
                dl.pop_front();
            }
            else 
            {
                next = dh.front();
                dh.pop_front();
            }
            h = (next)/2;
            l = (next-1)/2;
            dh.push_back(h);
            dl.push_back(l);
        }
		cout << "Case #" << caso + 1 << ": " << h << " " << l << endl;
	}
	return 0;
}
