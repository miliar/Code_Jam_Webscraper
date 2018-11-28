#include <bits/stdc++.h>
using namespace std;
pair< double, double > a[100005],b[100005];
string s;
struct myclass {
  bool operator() (pair<double,double> i,pair<double,double> j) { 
  	return (i.first*i.second<j.first*j.second);
  }
} myobject;
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t,tc=1;
	for(cin>>t;tc<=t;++tc){
		cout<<"Case #"<<tc<<": ";
		long long int n,k,l;
		long double ans, p=0;
		cin>>n>>k;
		for(int i=0;i<n;++i) cin>>a[i].first>>a[i].second;
		sort(a,a+n);
		for(l=n-1;l>=0;--l){
			ans=(a[l].first*a[l].first) + 2*a[l].first*a[l].second;
			for(int i=0,j=0;i<n;++i) if(i!=l) {
				b[j].first=a[i].second;
				b[j].second=a[i].first;
				j++;
			}
			sort(b,b+n-1,myobject);
			for(int i=n-2;i>n-2-k+1;--i){
				ans+=2*b[i].first*b[i].second;
			}
			p=max(p,ans);
		}
		cout<<fixed<<setprecision(8)<<p*3.14159265358979323846264<<'\n';
	}
}