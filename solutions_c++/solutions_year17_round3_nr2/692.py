#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;
const double EPS = 1e-9;
const int INF = 1 << 29;
#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define all(a) a.begin(),a.end()
#ifndef ONLINE_JUDGE
#define tr(a, it) for (decltype(a.begin()) it = a.begin(); it != a.end(); ++it)
#else
#define tr(a, it) for (typeof(a.begin()) it = a.begin(); it != a.end(); ++it)
#endif
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d",n);
#define outl(n) printf("%lld",n);

int const NN = 1442;
bool busyC[NN]; 
bool busyJ[NN];
int ac, aj;
int C[NN], D[NN];
int J[NN], K[NN];
int mnJ;
int dp[NN][NN / 2][3][3];
//bool existsJ[NN];

int rec(int tot, int mx, int prev, int endd){
	if (tot == 0){
		if (mx != 0)return INF;
		return dp[tot][mx][prev][endd] = (prev != endd);
	}
	if (mx == 0){
		if (tot - 1 >= mnJ && mnJ != -1)return INF;
		return dp[tot][mx][prev][endd] = (1 + (endd != 2));
	}
	if (prev != -1 && endd != -1 && dp[tot][mx][prev][endd] != -1)
		return dp[tot][mx][prev][endd];
	if (busyC[tot - 1]){
		if (prev == -1)return rec(tot - 1, mx, 2, 2);
		return dp[tot][mx][prev][endd] = ((prev != 2) + rec(tot - 1, mx, 2, endd));
	}
	else if (busyJ[tot - 1]){
		if (prev == -1)return rec(tot - 1, mx - 1, 1, 1);
		return dp[tot][mx][prev][endd] = ((prev != 1) + rec(tot - 1, mx - 1, 1, endd));
	}
	else{
		if (prev == -1)
			return min(rec(tot - 1, mx, 2, 2), rec(tot - 1, mx - 1, 1, 1));
		return dp[tot][mx][prev][endd] = min((prev != 1) + rec(tot - 1, mx - 1, 1, endd), 
			(prev != 2) + rec(tot - 1, mx, 2, endd));
	}
}

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int t; in(t);
	for (int cs = 1; cs <= t; ++cs){		
		Fill(busyC, false);
		Fill(busyJ, false);
		mnJ = -1;
		//Fill(existsJ, false);
		in(ac); in(aj);
		for (int i = 1; i <= ac; ++i){
			in(C[i]); in(D[i]);			
			for (int j = C[i]; j < D[i]; ++j)busyC[j] = true;
		}
		for (int i = 1; i <= aj; ++i){
			in(J[i]); in(K[i]);
			if (mnJ == -1)mnJ = J[i];
			else mnJ = min(mnJ, J[i]);
			for (int j = J[i]; j < K[i]; ++j)busyJ[j] = true;
		}
		for (int i = 0; i < NN; ++i){
			for (int j = 0; j < NN / 2; ++j){
				for (int jj = 0; jj < 3; ++jj){
					for (int jjj = 0; jjj < 3; ++jjj)dp[i][j][jj][jjj] = -1;
				}
			}
		}
		int ans = rec(1440, 720, -1, -1);
		printf("Case #%d: %d\n", cs, ans);
	}
	return 0;
}