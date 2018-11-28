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
		LL n;
		scanf("%lld",&n);
		char c[20];
		sprintf(c,"%lld",n);
		for(int i=0;c[i+1]!=0;i++){
			if(c[i]>c[i+1]){
				int j;
				for(j=i-1;j>=0;j--)
				if(c[j]!=c[i]){
					break;
				}
				j++;
				c[j]--;
				for(int k=j+1;c[k]!=0;k++)
				c[k]='9';
				break;
				
			} 
		}
		sscanf(c,"%lld",&n);
		printf("Case #%d: %lld\n",T,n);
	}
}
/*
Y  * (5y-4)(y+1)*/

