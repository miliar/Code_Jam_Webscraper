#include <bits/stdc++.h>

using namespace std;
#define int long long
#undef int
int main(){
	#define int long long
	int tc,tci=1;cin>>tc;
	while(tc-->0){
		int d,n;cin>>d>>n;
		int nowk,nows;
		cin>>nowk>>nows;
		for(int i=1;i<n;i++){
			int k,s;cin>>k>>s;
			if(((long double)(d-k)/s)>((long double)(d-nowk)/nows)){
				nowk=k;nows=s;
			}
		}
		long double time=(long double)(d-nowk)/nows;
		cout<<"Case #"<<tci++<<": "<<fixed<<setprecision(6)<<d/time<<endl;
	}
	return 0;
} 
