/*input
3
---+-++- 3
+++++ 4
-+-+- 4
*/
#include <bits/stdc++.h>
#define fastIo ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define fi first
#define se second
#define sz size
#define pb push_back
#define mp make_pair
using namespace std;

//#define LOCAL
#ifdef LOCAL
	#define DEBUG(x) do { cout << #x << ": " << x << '\n'; } while (0)
#else
	#define DEBUG(x) 
#endif

const double EPS = 1e-9;
const double PI = 3.141592653589793238462;

const int dr[] = {1, 1, 0, -1, -1, -1, 0, 1};
const int dc[] = {0, 1, 1, 1, 0, -1, -1, -1};

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};

void solve(){
	string s;
	int k;
	cin >> s >> k;

	int ans = 0;
	for(int i = 0; i <= s.sz() - k; i++){
		if(s[i] == '-'){
			for(int j = i; j < i + k; j++){
				if(s[j] == '-'){
					s[j] = '+';
				}
				else{
					s[j] = '-';
				}
			}
			ans++;
		}
	}

	int f = 0;
	for(int i = 0; i < s.sz(); i++){
		if(s[i] != '+'){
			f = 1;
			break;
		}
	}

	if(f){
		cout << "IMPOSSIBLE\n";
	}
	else{
		cout << ans << '\n';
	}

}
int main(){
	fastIo;

	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int t;
	cin >> t;

	for(int i = 1; i <= t; i++){
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}