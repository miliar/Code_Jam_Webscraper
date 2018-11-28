#include<iostream>
#include<math.h>
#include<stdlib.h>
#define ul unsigned long long
#define ll long long
using namespace std;
int main(void){
	ll int t,n,tc;
	scanf("%lld",&t);
	tc=t;
	while(t--){
		scanf("%lld",&n);
		ll int m=n;
		while(m--){
			ll int a[19]={-1},d,f=0,i=-1;
			while(n>0){
				d=n%10;
				a[++i]=d;
				n/=10;
			}
			for(ll int j=0;j<i;++j){
				if(a[j+1]>a[j]){
					f=1;
					break;
				}
			}
			if(f){
				n=m;
				continue;
			}
			else
				break;
		}
		cout<<"Case #"<<tc-t<<": "<<m+1<<endl;
	}
	return 0;
}