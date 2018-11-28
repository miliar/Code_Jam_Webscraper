#include<bits/stdc++.h>
#include<unistd.h>
#define int long long
const int inf=8938103643641919514ll;
const int mod=1000000007ll;
const int dd[]={0,-1,0,1,0};
using namespace std;
int a,b,c,d;
pair<int,int> p[1000];
double sokumen(int x,int y){
	return (double)x*2*3.1415926535*(double)y;
}
signed main(){
	int i,j;
	cin>>a;
	for(i=0;i<a;i++){
		int n,k;
		cin>>n>>k;
		for(j=0;j<n;j++)
			cin>>p[j].first>>p[j].second;
		double u,ans=0;
		for(j=0;j<=n-k;j++){
			sort(p,p+n);
			reverse(p,p+n);
			u=sokumen(p[j].first,p[j].second)+(double)p[j].first*p[j].first*3.1415926535;
			sort(p+j+1,p+n,[](pair<int,int> x,pair<int,int> y){return sokumen(x.first,x.second)>sokumen(y.first,y.second);});
			for(int l=j+1;l<k+j;l++)
				u+=sokumen(p[l].first,p[l].second);
			ans=max(u,ans);
		}
		cout<<"Case #"<<i+1<<": "<<setprecision(15)<<ans<<endl;
	}
}
