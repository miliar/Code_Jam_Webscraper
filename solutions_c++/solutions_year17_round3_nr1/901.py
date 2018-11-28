#include<bits/stdc++.h>

using namespace std;

# define PI           3.14159265358979323846

pair<double, double> rh[1100];
double ans, d[1100][1100];
int n, k;

void solve()
{
	cin>>n>>k;                 
	for(int i=0; i<n; i++) cin>>rh[i].first>>rh[i].second;
	sort(rh, rh+n);

	ans = 0.0;
	for(int i=0; i<=k; i++)
		for(int j=0; j<=n; j++) d[i][j] = 0.0;      

	for(int i=0; i<=n-k; i++)
		d[0][i] = PI*rh[i].first*rh[i].first + 2.0*PI*rh[i].first*rh[i].second,
		ans = max(ans, d[0][i]);

	double tmp;
	for(int cnt=1; cnt<k; cnt++)
		for(int i=cnt; i<=n-(k-cnt); i++)
			for(int j=cnt-1; j<i; j++)
				tmp = PI*rh[i].first*rh[i].first,
				tmp+= 2.0*PI*rh[i].first*rh[i].second,
				tmp-= PI*rh[j].first*rh[j].first, 
				d[cnt][i] = max(d[cnt][i], d[cnt-1][j] + tmp),
				ans = max(d[cnt][i], ans);

	cout<<fixed<<setprecision(12)<<ans<<endl;
}

int main()
{
	int T;
	cin>>T;

	for(int i=1; i<=T; ++i)
		cout<<"Case #"<<i<<": ",
		solve();
	return 0;
}