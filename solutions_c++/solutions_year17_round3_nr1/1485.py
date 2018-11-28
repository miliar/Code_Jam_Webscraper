#include<bits/stdc++.h>
using namespace std;
#define pi acos(-1.0)
int main(){
	freopen("A-large.in","r",stdin);
	freopen("1.txt","w",stdout);
	int T,kase=0;cin>>T;
	while(T--){
		kase++;
		int n,k;
		cin>>n>>k;
		pair<int,int>a[1001];
		for (int i=0;i<n;i++)cin>>a[i].first>>a[i].second;
		pair<double,pair<int,int> >b[1001];
		for (int i=0;i<n;i++)b[i]=make_pair((double)a[i].second*2*pi*a[i].first,a[i]);
		sort(b,b+n);
		double sum=0,mx=0;
		for (int i=n-1;i>=n-k;i--){
			sum+=b[i].first;
			mx=max(mx,(double)b[i].second.first);
		}
		double xxx=mx*mx*pi;
		for (int i=n-k-1;i>=0;i--)
			xxx=max((double)(b[i].second.first)*(b[i].second.first)*pi-(b[n-k].first-b[i].first),xxx);
		printf("Case #%d: %.9f\n",kase,sum+xxx);
	}
}
