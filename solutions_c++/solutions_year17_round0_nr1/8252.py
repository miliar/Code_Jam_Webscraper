#include <bits/stdc++.h>
#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define mp make_pair
#define f first
#define s second
#define pb push_back
#define pf push_front
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef pair<ll,ll> LL;

const ll INF = 1e9;
const double EPS = 1e-9;
const ll MOD = 1e9 + 7;

int t,k,c = 1,n;
string s;

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);cin.tie(0);
	cin >> t;
	while(t--){
		cin >> s;
		cin >> k;
		n = s.size();
		//01234
		cout << "Case #" << c++ << ": ";
		if (n < k){
			cout << "IMPOSSIBLE\n";
			continue;
		}
		int res = 0;
		REP(i,n - k + 1){
			if (s[i] == '-'){
				res++;
				FOR(j,i,i + k - 1){
					if (s[j] == '-')s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		bool bisa = true;
		REP(i,n)if (s[i] == '-'){
			cout << "IMPOSSIBLE\n";
			bisa = false;
			break;
		}
		if (bisa)cout << res << '\n';
	}
}
