/*input
4
132
1000
7
111111111111111110
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
	string n;
	cin >> n;
	if(n.sz() < 2){
		cout << n << '\n';
		return;
	}
	while(!is_sorted(all(n))){
		for(int i = 0; i < n.sz() - 1; i++){
			if(n[i] > n[i + 1]){
				n[i]--;
				for(int j = i + 1; j < n.sz(); j++){
					n[j] = '9';
				}
			}
		}
	}
	if(n[0] == '0'){
		n = n.substr(1, n.sz() - 1);
	}
	cout << n << '\n';
}

int main(){
	fastIo;

	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int t;
	cin >> t;

	for(int i = 1; i <= t; i++){
		cout << "Case #" << i << ": ";
		solve();	
	}

	return 0;
}