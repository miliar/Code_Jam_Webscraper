#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

const int N = 1441;
const int INF=0x3f3f3f3f;
int na, nb;
bool a[2][1441], b[1441];

int dp[N][N][2][2];

int f(int i, int m, int h, int h1) {

	if (m>720) return INF;

	if (i==1440){
		return m == 720 ? h1!=h : INF;
	}

	int &ret = dp[i][m][h][h1];
	if (ret != -1) return ret;

	ret = INF;
	int ok =0 ;
	if (a[h][i]) {
		ok=1;
		ret = min(ret, f(i+1, m + h, h, h1));
	}

	if (a[!h][i]){
		ok=1;
		ret = min(ret, 1+f(i+1, m+!h, !h, h1));
	}
	return ret;
}

int main(void) {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tt = 1; tt<=T; tt++) {
		cin >> na >> nb;
		cout << "Case #" << tt << ": ";

		for(int j=0;j<2;j++)
			for(int i =0 ; i<N; i++)
				a[j][i] = 1;

		for (int i = 0; i<na; i++) {
			int s, x;cin>>s>>x;
			for (int j = s; j<x; j++)
				a[0][j] = 0;
		}

		for (int i = 0; i<nb; i++) {
			int s, x;cin>>s>>x;
			for (int j = s; j<x; j++)
				a[1][j] = 0;
		}
		memset (dp, -1, sizeof dp);
		int ans = INF;
		if (a[0][0])
			ans = min(ans, f(1, 0, 0, 0));
		if (a[1][0])
			ans = min(ans, f(1, 1, 1, 1));
		cout << ans << endl;
	}
	
	
	return 0;
}
