#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
double ar[1005];
pair<double,double> p[1005];
double q[1005];
const double pi=3.14159265358979323846;

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	
	int t;
	cin>>t;
	for(int qq=1;qq<=t;qq++){
		int n,k;
		cin>>n>>k;
		for(int i=0;i<n;i++){
			int r,h;
			cin>>r>>h;
			ar[i]=pi*r*r;
			double x=2*pi*r*h;
			q[i]=x;
			p[i]=make_pair(x,i);
		}
		sort(p,p+n);
		double ans=0;
		for(int i=0;i<n;i++){
			double a1=ar[i]+q[i];
			for(int x1=n-1,j=1;j<k;x1--){
				if(p[x1].second==i) continue;
				a1+=p[x1].first;
				j++;
			}
			ans=max(a1,ans);
		}
		cout.precision(17);
		cout<<"Case #"<<qq<<": "<<ans<<endl;
	}
	
	return 0;
}
