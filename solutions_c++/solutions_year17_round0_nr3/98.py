#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <algorithm>
#define MOD 1000000007
#define forn(a, n) for(int a = 0; a<(int) (n); ++a)
#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define forall(a, all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)
#define EPS 0.000000000001
typedef long long tint;
using namespace std;

int main()
{
#ifdef ACMTUYO
	freopen("C-large(2).in","r",stdin);
	freopen("C-large(2).out","w",stdout);
#endif
	
	int C;
	cin >> C;
	forn(tc, C) {
		tint n, k;
		cin >> n >> k;
		map<tint,tint> holes;
		holes[n] = 1;
		
		while(holes.rbegin()->second < k) {
			tint a = holes.rbegin()->first, b = holes.rbegin()->second;
			tint c = (a-1)/2;
			holes.erase(a);
			if(!holes.count(c)) {
				holes[c] = 0;
			}
			if(!holes.count(a-c-1)) {
				holes[a-c-1] = 0;
			}
			holes[c] += b;
			holes[a-c-1] += b;
			k -= b;
		}
		
		tint f = holes.rbegin()->first-1;
		cout << "Case #" << tc+1 << ": "; 
		cout << f-f/2 << " " << f/2;
		cout << endl;
	}
	
	return 0;
}
