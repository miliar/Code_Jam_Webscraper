/*input
3
2 2
0.0000
0.9000 0.8000
4 4
1.4000
0.5000 0.7000 0.8000 0.6000
2 2
1.0000
0.0000 0.0000
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

int main(){
	ifstream cin("C-small-1-attempt3.in");
	ofstream cout("C-small-1-output-attempt3.txt");
	int t, n, k, i, j;
	cin>>t;
	for(int te=1;te<=t;++te){
		cout<<"Case #"<<te<<": ";
		double u;
		cin>>n>>k;
		double a[n+1];
		cin>>u;	
		a[n] = 1.0;

		fo(i,n)
			cin>>a[i];
		sort(a,a+(n+1));

		for(i=1;i<=n;i++){
			if(u>i*(a[i]-a[0])){
				u = u - i*(a[i]-a[0]);
				for(j=0;j<i;j++){
					a[j] = a[i];
				} 
			}
			else{
				for(j=0;j<i;j++){
					a[j] = a[j] + u*1.0/i;
				}
				break;
			}
		}

		long double ans = 1.0;
		fo(i,n){	
			// cout<<a[i]<<" ";
			ans = ans * a[i];
		}
		cout<<fixed<<setprecision(12)<<ans<<endl;


	}
	return 0;
}
