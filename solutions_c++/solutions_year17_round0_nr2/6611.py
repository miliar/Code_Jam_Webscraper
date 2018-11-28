#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	//freopen("B-small-attempt0.in.","r",stdin);
	//freopen("1","w",stdout);
	ll n;
	int T,TT=0;
	scanf("%d",&T);
	while(T--){
		cin>>n;
		printf("Case #%d: ",++TT);
		lab:
		int r=0;
		ll t=1;
		while(t<=n){
			r++;
			t*=10;
		}
		t=n;
		int first;
		while(t){
			first=t%10;
			t/=10;
		}
		ll tt=0;
		for(int i=1;i<=r;i++)
			tt=tt*10+first;
		if(n<tt){
			if(first-1)
				printf("%d",first-1);
			for(int i=1;i<r;i++)
				printf("9");	
		}
		else{
			printf("%d",first);
			n-=pow(10,r-1)*first;
			if(n)
				goto lab;
		}
		printf("\n");
	}
	return 0;
}
/*

*/
