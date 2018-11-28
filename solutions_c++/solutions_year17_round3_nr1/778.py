#include <bits/stdc++.h>

using namespace std;
#define int long long 
#define MOD 1000000007

signed main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int tt;
	cin >> tt;
	for(int t=1;t<=tt;t++){
		cout << "Case #" << t << ": ";
		int n,k;
		cin >> n >> k;
		vector<pair<int,int> >p(n);
		for(int i=0;i<n;i++){
			cin >> p[i].first >> p[i].second;
		}
		p.push_back({-1,-1});
		sort(p.begin(),p.end());
		double res = 0;
		double d[n+5][n+5];
		double f[n+5][n+5];
		for(int i=0;i<n+5;i++) for(int j=0;j<n+5;j++) d[i][j] = 0;
		for(int i=0;i<n+5;i++) for(int j=0;j<n+5;j++) f[i][j] = 0;
		/*for(int i=1;i<=n;i++){
			for(int j=1;j<=k;j++){
				if(j>i) break;
				for(int l=0;l<i;l++){
					d[i][j] = max(d[i][j],d[l][j-1] + )
				}
				d[i][j] = max(d[i-1][j],d[i-1][j-1] + 2*p[i].second*p[i].first);
			}
		}*/
		for(int j=1;j<=k;j++){
			for(int i=j;i<=n;i++){
				d[i][j] = f[i-1][j-1] + 2*p[i].second*p[i].first;
			}
			for(int i=1;i<=n;i++){
				f[i][j] = max(d[i][j],f[i-1][j]);
			}
		}
		/*for(int i=0;i<=n;i++){
			cout << d[i][1] << " " << f[i][1] << endl;
		}
		for(int i=0;i<=n;i++){
			cout << d[i][2] << " " << f[i][2] << endl;
		}*/
		for(int i=1;i<=n;i++){
			res = max(res,d[i][k] + p[i].first*p[i].first);
		//	cout << d[i][k] << " " << p[i].first*p[i].first << " " << i << endl;
		}
		res *= atan(1)*4;
		cout << fixed << setprecision(10) << res << "\n";
	}
	return 0;
}