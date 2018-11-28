/*input
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
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
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	ifstream cin("A-large.in");
	ofstream cout("A-large-output.txt");
	int t;
	cin>>t;
	for(int te=1;te<=t;te++){
		cout<<"Case #"<<te<<": ";
		double k, x, y, maxer = -1, ans;
		ll d;
		cin>>k>>d;
		while(d--){
			cin>>x>>y;
			ans = k - x;
			ans = ans*1.0/y;
			if(ans > maxer)
				maxer = ans;
		}
		ans = k*1.0/maxer;
		cout<<fixed<<setprecision(12)<<ans<<endl;
	}
	return 0;
}
