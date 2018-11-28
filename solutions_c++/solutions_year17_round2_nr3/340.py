#include <bits/stdc++.h>

using namespace std;
const double pi=acos(-1.0);
const double eps=1e-9;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define re return
#define vi vector <int> 
#define pii pair <int,int>
#define pll pair <long long , long long>
typedef long long ll;

const int N = 105;
const ll inf = (ll)1e18;


ll t,n,q,e[N],s[N],d[N][N],u,v;
double tt[N][N];
bool can[N][N];

int main()
{
	ios:: sync_with_stdio(false);
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	cin >> t;
	cout << fixed << setprecision(10);
	for(int test = 1; test <= t; test++)
	{
		cin >> n >> q;
		for(int i = 0; i < n; i++)
			cin >> e[i] >> s[i];
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
			{
				cin >> d[i][j];
				if(d[i][j] == -1)d[i][j] = inf;
				if(i == j)d[i][j] = 0;
			}
		for(int k = 0; k < n; k++)
			for(int i = 0; i < n; i++)
				for(int j = 0; j < n; j++)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
		for(int i = 0; i < n;i++)
			for(int j = 0; j < n; j++)
				if(e[i] >= d[i][j])can[i][j] = true; else can[i][j] = false;
		for(int i = 0; i < n ;i++)
			for(int j = 0;j < n; j++)
				if(!can[i][j])tt[i][j] = inf; else tt[i][j] = d[i][j]/((double)s[i]);
		for(int k = 0; k < n; k++)
			for(int i = 0; i < n; i++)
				for(int j = 0; j < n; j++)
					tt[i][j] = min(tt[i][j], tt[i][k] + tt[k][j]);
		cout << "Case #" << test << ": ";
		for(int i = 0; i < q; i++)
		{
			cin >> u >> v;
			u--;v--;
			cout << tt[u][v] << " ";
		}
		cout << "\n";
	}
	return 0;
}
