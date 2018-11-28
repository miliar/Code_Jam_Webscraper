/*input
4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
*/
#include <bits/stdc++.h>
#define endl '\n'
#define fo(i,n) for(i=0;i<n;++i)
#define forr(i,n) for(i=n-1;i>=0;--i)
using namespace std;
typedef long long int ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

const long double PI = 3.1415926535897932384626433832795028841971693993751058209749445;
int main(){
	ifstream cin("A-large.in");
	ofstream cout("A-large-output.txt");
	ll t, i, n, k, x, y;
	long double ans, ans1, ans2, ans3;
	cin>>t;
	for(int te=1;te<=t;++te){
		cout<<"Case #"<<te<<": ";
		cin>>n>>k;
		ll maxr, maxh;
		maxr = -1;
		maxh = -1;
		ans = 0.0;
		ans1 = 0.0;
		ans2 = 0.0;
		ans3 = 0.0;
		vector<pair<ll,ll> >r;
		fo(i,n){
			cin>>x>>y;
				if(x==maxr){
					if(y>maxh){	
						maxr = x;
						maxh = y;
					}
				}
				if(x>maxr){
					maxr = x;
					maxh = y;
				}
			r.push_back(make_pair(x*y,x)); //r*h,r
		}
		double maxer = 0.0;
		sort(r.rbegin(),r.rend());
			
			double mx = -1.0;
			// ans = 2*1.0*PI*r[0].first;

			for(int j=0;j<k;j++){
					ans += 2*1.0*PI*r[j].first;
					if(r[j].second>mx)
						mx = r[j].second;
			}
				ans = ans + PI*mx*mx;
				maxer = ans;
		


		for(i=k;i<n;i++){
			ans = 2*1.0*PI*r[i].first;
			mx = r[i].second;
			for(int j=0;j<k-1;j++){
				ans += 2*1.0*PI*r[j].first;
				if(r[j].second>mx)
					mx = r[j].second;
			}
			ans = ans + PI*mx*mx;
			if(ans>maxer)
				maxer = ans;
		}
		cout<<fixed<<setprecision(10)<<maxer<<endl;
	}
	return 0;
}
