#include<iostream>
#include<cstring>
#include<algorithm>
#include<fstream>
using namespace std;
pair<long long,long long>arr[1005];
int main(){
	#ifndef ONLINE_JUDGE
	freopen("i.txt", "r", stdin);
	freopen("o.txt", "w", stdout);
#endif
	int t;cin>>t;
	long long  d;int n;long long k,s;
	for(int i=0;i<t;++i){
	cin>>d>>n; double x=-1;
	for(int j=0;j<n;++j){
	cin>>k>>s;
	x=max(x,(d-k)/1.0/s);
	}
	double h=d/x;
	cout<<"Case #"<<i+1<<": ";
	printf("%.10f", h);cout<<endl;
	/*for(int j=0;j<1000;++j)
		arr[j].first=arr[j].second=0;*/
	}
}