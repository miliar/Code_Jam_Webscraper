#include <bits/stdc++.h>

using namespace std;
#define int long long 
#define MOD 1000000007
#define EPS 0.0000000001
#define double long double
vector<pair<int,pair<int,int> > > v;

signed main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int tt;
	cin >> tt;
	for(int t=1;t<=tt;t++){
		cout << "Case #" << t << ": ";
		int n,k;
		cin >> n >> k;
		double u;
		cin >> u;
		double p[n];
		for(int i=0;i<n;i++){
			cin >> p[i];
		}
		while(u>EPS){
			sort(p,p+n);
			double a = p[0];
			double b = p[0];
			int j = 0;
			for(int i=1;i<n;i++){
				//cout << p[i] << " " << a << endl;
				if(fabs(p[i]-a)>EPS){
					b = p[i];
					j = i;
					break;
				}
			}
		//	cout << endl;
			if(fabs(a-b)<EPS){
				double l = u/n;
				for(int i=0;i<n;i++) p[i] += l;
				u = 0;
				break;
			}
			else{
		//	cout << u << " " << a << " " << b << " " << j << endl;
				double l = min(u/j,b-a);
				for(int i=0;i<j;i++){
					p[i] += l;
				}
				u -= (b-a)*j;
			}
		}
		//for(int i=0;i<n;i++) cout << p[i] << " ";
		double res = 1;
		for(int i=0;i<n;i++){
			res *= p[i];
		//	cout << res << " ";
		}
		cout << fixed << setprecision(6) << res << "\n";
	}
	return 0;
}