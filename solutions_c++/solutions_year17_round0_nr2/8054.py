#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cctype>
#define SZ(x) ( (int) (x).size() )
#define me(x,a) memset(x,a,sizeof(x))
#define FN(a,n) for(int a=0;a<n;a++)
#define FOR(a,ini,fin) for(int a=(ini);a<(fin);a++)
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define endl "\n"
#define MOD 1000000007
#define MAXN 1003
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
using namespace std;

int main() {
	int tc;
	sc(tc);
	FN (itc, tc) {
		vector<int> digs;
		string s;
		cin >> s;
		
		digs.clear();
		
		reverse(s.begin() , s.end());
		FN (i, SZ(s)) digs.pb(s[i] - '0');
		digs.pb(0);
		
		int ld = 0;
		for (int i = SZ(digs) - 1; i >= 0; i--) {
			int d = digs[i];
			if (d < ld) {
				int j;
				for (j = i + 1; j < SZ(digs) && digs[j] == ld;j++) {
					;
				}
				j--;
				if (j >= 0) digs[j] = ld - 1;
				j--;
				for (; j >= 0; j--) digs[j] = 9;
				break;
			}
			ld = d;
		}

		printf("Case #%d: ", itc + 1);	
		
		int ind = 0;
		reverse(digs.begin(), digs.end());
		while(ind < SZ(digs) && digs[ind] == 0) ind++;
		FOR (i, ind, SZ(digs)) {
			putchar(digs[i] + '0');
		}
		puts("");
	}
}
