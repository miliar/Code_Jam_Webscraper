#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;

int memo[101][101][101][4];
int n, p;

int cnt[4];

int pd(int m1, int m2, int m3, int ok) {
	if(!m1 and !m2 and !m3) {
		return 0;
	} else if(memo[m1][m2][m3][ok] != -1) {
		return memo[m1][m2][m3][ok];
	} else {
			int ret = 0;
			if(m1) {
				ret = max(ret, pd(m1 - 1, m2, m3, (ok + 1)%p));
			}
			if(m2) {
				ret = max(ret, pd(m1, m2 - 1, m3, (ok + 2)%p));
			}
			if(m3) {
				ret = max(ret, pd(m1, m2, m3 - 1, (ok + 3)%p));
			}

			return memo[m1][m2][m3][ok] = ret + (ok == 0);
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	int T;	
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cin >> n >> p;
		memset(cnt, 0, sizeof cnt);
		memset(memo, -1, sizeof memo);
		for(int i = 0; i < n; i++){ 
			int aux;
			cin >> aux;	
			cnt[aux%p]++;
		}
		cout << "Case #"<< t << ": " << pd(cnt[1], cnt[2], cnt[3], 0) + cnt[0] << endl;
	}
	return 0;
}
