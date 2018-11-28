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
bool check(char c[]){
	for(int i=0;c[i]!=0;i++)
	if(c[i]=='-')
	return false;
	return true;
}
int main(){
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		char c[1005];
		scanf("%s",c);
		int k;
		scanf("%d",&k);
		int ans=0;
		for(int i=0;c[i+k-1]!=0;i++){
			if(c[i]=='-'){
				for(int j=i;j<i+k;j++)
				{
					c[j]=  c[j]=='+'?'-':'+';
				}
				ans++;
			}
		}
		if(check(c)){
			printf("Case #%d: %d\n",T,ans);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n",T);
		}
	}
}
/*
Y  * (5y-4)(y+1)*/

