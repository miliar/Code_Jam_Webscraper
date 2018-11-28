#include <bits/stdc++.h>
#define MAXN 101
using namespace std;

#define rep(i, f, t) for (int i = f; i < int(t); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define trav(x,a) for (auto& x : a)
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

char dp[5][4][105][105][105][105];

void solve(){
	int N, P;
	cin >> N >> P;
	int a[4]={0,0,0,0};
	rep(i,0,N){
		int G;
		cin >> G;
		a[G%P]++;
	}
	cout << ((int)dp[P][0][a[0]][a[1]][a[2]][a[3]]) << endl;
}

int main(){
	rep(P,2,5){
		int a[5];
		for(a[0] = 0; a[0] <= MAXN; ++a[0]){
			cerr << a[0] << endl;
		for(a[1] = 0; a[1] <= MAXN; ++a[1]){
		for(a[2] = 0; a[2] <= MAXN; ++a[2]){
		for(a[3] = 0; a[3] <= MAXN; ++a[3])
		rep(cur,0,P){
			rep(i,0,4){
				if(!a[i]){
					continue;
				}
				int b[4];
				rep(j,0,4)
					b[j]=a[j];
				--b[i];
				dp[P][cur][a[0]][a[1]][a[2]][a[3]] = max(
						(int)dp[P][cur][a[0]][a[1]][a[2]][a[3]], 
						dp[P][(cur+i)%P][b[0]][b[1]][b[2]][b[3]] + (cur == 0));
			}
		}
		}
		}
		}
	}
	int N;
	cin >> N;
	rep(t,1,N+1){
		cout << "Case #" << t << ": ";
		solve();
	}
}
