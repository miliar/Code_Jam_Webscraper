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

tint solve(string n, int i) {
	if(i >= (int) n.size()) return 0;
	if(n[i] < n[i-1]) return -1;
	tint ans = solve(n, i+1);
	if(ans == -1) {
		if(n[i] == n[i-1]) return -1;
		int p = n.size()-i-1;
		ans = n[i]-'1';
		forn(j, p) {
			ans = 10LL*ans+9LL;
		}
		return ans;
	}
	tint r = n[i]-'0';
	int p = n.size()-i-1;
	forn(j,p){
		r *= 10LL;
	}
	return r+ans;
	
}

int main()
{
#ifdef ACMTUYO
	freopen("B-large(3).in","r",stdin);
	freopen("B-large(3).out","w",stdout);
#endif
	
	int C;
	cin >> C;
	forn(tc, C) {
		string n;
		cin >> n;
		string m = "0";
		m += n;
		
		tint ans = solve(m, 1);
		cout << "Case #" << tc+1 << ": "; 
		cout << ans;
		cout << endl;
	}
	
	return 0;
}
