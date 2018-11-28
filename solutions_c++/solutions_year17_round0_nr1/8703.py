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

int T, C, sol;
string s;
bool ok;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;
	REP(tc, T){
		cin >> s >> C;
		
		ok = true;
		sol = 0;
		
		REP(I, SZ(s)-C+1) if (s[I]=='-'){
			sol ++;
			REP(K, C) s[I+K] = (s[I+K]=='-')?'+':'-';
		}
		cout << "Case #" << tc+1 << ": ";
		REP(I, C) if (s[SZ(s)-I-1]=='-'){
			cout << "IMPOSSIBLE" << endl;
			ok = false;
			break;
		}
		if (ok) cout << sol << endl;
	}
}

















