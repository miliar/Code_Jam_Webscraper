#define LOCAL

#ifdef LOCAL
#define _GLIBCXX_DEBUG
#pragma GCC optimize("O3")
#endif
#include<bits/stdc++.h>
#define rep(i,k,n) for(ll i= (ll) k;i< (ll) n;i++)
#define all(v) (v).begin(), (v).end()
#define SZ(v) (int)((v).size())
#define pb push_back
#define ft first
#define sd second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const long long INF = 4e18L + 1;
const int IINF = 2e9 + 1;
using namespace std;
template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<','; _dbg(sdbg+1, a...);
}
#ifdef LOCAL
#define DBG(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define DBG(...) (__VA_ARGS__)
#define cerr if(0)cout
#endif

//wszyscy modulo 
//zera dodac na poczatku

char dp[5][101][101][101][4];//1, 2, 3

char wyjmij(int i, int j, int k, int l, int co, int P)
{
	l += P;
	l -= co+1;
	if (l >= P)
		l -= P;
	int wyn = 0;
	if (l == 0)
		wyn++;
	if (co == 0)//1
		i--;
	if (co == 1)//2
		j--;
	if (co == 2)//3
		k--;
	wyn += dp[P][i][j][k][l];	
	return wyn;
}

int wez_wyn(int i, int j, int k, int P)
{
	return dp[P][i][j][k][(i + 2*j + 3*k)%P];
}

int main()
{
#ifndef LOCAL
    ios_base::sync_with_stdio(0);
    cin.tie(0);
#endif
	for(int P = 2; P<=4; P++)
	{
		for(int i=0; i<=100; i++)
		{
			for(int j=0; j<=100; j++)
			{
				for(int k=0; k<=100; k++)
				{
					if (i == 0 && j == 0 && k == 0)
						dp[P][i][j][k][1] = dp[P][i][j][k][2] = dp[P][i][j][k][3] = -101;
					int l = (i + j*2 + 3*k) % P;
					if (i > 0)
						dp[P][i][j][k][l] = max(dp[P][i][j][k][l], wyjmij(i, j, k, l, 0, P));
					if (j > 0)
						dp[P][i][j][k][l] = max(dp[P][i][j][k][l], wyjmij(i, j, k, l, 1, P));
					if (k > 0)
						dp[P][i][j][k][l] = max(dp[P][i][j][k][l], wyjmij(i, j, k, l, 2, P));
				}
			}
		}
	}
	int t;
	cin>>t;
	for(int ii=1; ii<=t; ii++)
	{
		int wyn = 0;
		int n, k;
		vector < int > V(5, 0);
		cin>>n>>k;
		for(int i=0; i<n; i++)
		{
			int temp;
			cin>>temp;
			temp %= k;
			if (temp == 0)
				wyn++;
			else
				V[temp-1]++;
		}
		wyn += wez_wyn(V[0], V[1], V[2], k);
		cout << "Case #" << ii << ": " << wyn << endl;
	}
	
    return 0;
}

