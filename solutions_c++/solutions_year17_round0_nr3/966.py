//#include<stdio.h>
//#include<stdlib.h>
#include<bits/stdc++.h>
//#define Min(a,b,c) min((a),min((b),(c)))
#define mp(a,b) make_pair((a),(b))
#define pii pair<int,int>
#define pll pair<LL,LL>
#define pb(x) push_back(x)
#define x first
#define y second
#define sqr(x) ((x)*(x))
#define EPS 1e-11
#define MEM(x) memset(x,0,sizeof(x))
//#define N 200005
#define M
#define pi 3.14159265359
using namespace std;
typedef long long LL;
vector<LL> ans; 
int main(){
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		LL n,k;
		scanf("%lld %lld",&n,&k);
		printf("Case #%d: ",T);
		if(n==k){
			printf("0 0\n");
			continue;
		}
		LL a=0,b=1,num=n,sub=1;
		while(sub<k){
			k-=sub;
			if(num%2==0)
			{
				a*=2;
				a+=b;
				num=(num-1)/2; 
			}
			else{
				b*=2;
				b+=a;
				num=num/2;
			}
			sub=a+b;
		}
		
		if(k>a){
			printf("%lld %lld\n",(num-1)/2+(num-1)%2,(num-1)/2);
		}
		else{
			printf("%lld %lld\n",num/2+num%2,num/2);
		}
	}
}
/*
Y  * (5y-4)(y+1)*/

