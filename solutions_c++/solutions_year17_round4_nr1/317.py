/*\
 * ...
 * ......
 * In the name of ALLAH
 * ......
 * ...
\*/

#include <bits/stdc++.h>

using namespace std;
#define Size(x) ((int)(x).size())
#define pb push_back
#define LD_OUT setprecision(12) << fixed
typedef long long ll;
typedef long double ld;
typedef pair<int,int>pii;
const int INF = 1e9 + 10;
const int MN = 1e2 + 10;

int ans = 0;
int dp[MN][MN][MN] , C[4];
int n , p;
int arr[MN];

void solve()
{
	for(int a=0;a<=C[0];++a)
		for(int b=0;b<=C[1];++b)
			for(int c=0;c<=C[2];++c){
				if(a == b && b == c && c == 0) continue;
				if(a) // yani baghimande '1' mikhaim joda konim
					dp[a][b][c] = max(dp[a][b][c] , dp[a-1][b][c] + ((1 * (a-1) + 2 * b + 3 * c)%p == 0));
				if(b)
					dp[a][b][c] = max(dp[a][b][c] , dp[a][b-1][c] + ((1*a + 2 * (b-1) + 3 * c)%p == 0));
				if(c)
					dp[a][b][c] = max(dp[a][b][c] , dp[a][b][c-1] + ((1 * a + 2 * b + 3 * (c-1))%p == 0));	
			}
}

int main()
{
	ios_base :: sync_with_stdio(false) ,cin.tie(0) , cout.tie(0);
	int T;
	cin >> T;
	int cnt = 0;
	while(T--){
		++cnt;
		ans = 0;
		cout << "Case #" << cnt << ": ";
		memset(C , 0 , sizeof C);	
		cin >> n >> p;
		for(int i=0;i<n;++i){
			cin >> arr[i];
			if(arr[i]%p == 0) ++ans;
			else ++C[arr[i]%p - 1]; 
		}
		memset(dp , 0 , sizeof dp);	
		solve();
		cout << dp[C[0]][C[1]][C[2]] + ans << '\n';
	}
	return 0;
}

