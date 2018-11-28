#include<bits/stdc++.h>

#define PB push_back
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(), (c).end()
#define CONTAINS(c, x) ((c).find(x) != (c).end())
#define REP(i, n) for(int i=0; i<n; i++)
#define WAIT cout<<flush, system("PAUSE");
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

ll T, p;
vector<ll> sol;

void DFS(ll n){
	if (n * 10.0 > 1e18 +10) return;
	sol.PB(n);
	
	for(ll d=9; d>=max(1ll, n%10); d--) DFS(n*10ll + d);
}
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	DFS(0);
	sort(ALL(sol));
	cin >> T;
	REP(tc, T){
		cin >> p;
		
		cout << "Case #" << tc+1 << ": ";
		cout << *(upper_bound(ALL(sol), p)-1) << "\n";
	}
}

















