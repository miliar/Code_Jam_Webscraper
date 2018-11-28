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

int calcdp(vector<int>& restos, int P, vector<vector<vector<int> > >& DP, int tot){
	int s = 0;
	forn(i, P-1) s+=restos[i]*(i+1);
	if(s == 0) return 0;
	if(DP[restos[0]][restos[1]][restos[2]]!=-1){
		return DP[restos[0]][restos[1]][restos[2]];
	}
	
	int &ans = DP[restos[0]][restos[1]][restos[2]];
	
	forn(i, 3) {
		if(restos[i]>0){
			restos[i]--;
			ans = max(ans, calcdp(restos, P, DP, tot));
			restos[i]++;
		}
	}
	if((tot-s)%P == 0) ans++;
	return ans;
}

int main()
{
#ifdef ACMTUYO
	freopen("A-large(1).in","r",stdin);
	freopen("A-large(1).out","w",stdout);
#endif
	int C;
	cin >> C;
	forn(tc, C) {
		int N, P;
		cin >> N >> P;
		vector<vector<vector<int> > > DP(101, vector<vector<int> >(101, vector<int>(101, -1)));
		int m = 0;
		vector<int> start(3, 0);
		int tot = 0;
		forn(i, N){
			int a;
			cin >> a;
			tot += a;
			if(a%P == 0) m++;
			else start[a%P-1]++;
		}

		m += calcdp(start, P, DP, tot);

		cout << "Case #" << tc+1 << ": "; 
		cout << m << endl;
	}
}
