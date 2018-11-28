#include<bits/stdc++.h>
#define si(k) scanf("%d",&k)
#define p printf
#define ll long long
using namespace std;
int noDig(int num){
	int c=0;
	while(num!=0){
		num/=10;
		c++;
	}
	return c;
}
ll n,t;
int i,mi,u,v,test,j,q,m[300],k,x,y,z,c,s,a[300001],b[300001];
int main(){
	int l,sl,dig;
	cin>>test;
	for(z=1;z<=test;z++){
		
		cin>>n;
		while(1){
			dig=noDig(n);
				t=n;
			for(i=0;i<dig;i++){
				l=t%10;
				sl=(t/10)%10 ;
				if(l<sl){
					n--;
					break;
				}
				t/=10;
			
			}
			if(i==dig){
				p("Case #%d: %lld\n",z,n);
				break;
			}
		}
	}


return 0;
}
