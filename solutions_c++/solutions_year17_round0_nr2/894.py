//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
typedef long long int LL;
int s[20];
int x;
LL ans;
void dfs(int num, int pos, bool smaller,LL tmp){
	if(pos<0){
		ans=max(ans,tmp);
		return ;
	}
	if(smaller){
		dfs(9,pos-1,true,tmp*10+9);
	}else{
		if(s[pos]>=num) dfs(s[pos],pos-1,false,tmp*10+s[pos]);
		if(s[pos]-1>=num) dfs(s[pos]-1,pos-1,true,tmp*10+s[pos]-1);
	}
}
int main(void){
    int t;
    scanf("%d",&t);
    for(int hh=1;hh<=t;hh++){
		LL n;
		scanf("%lld",&n);
		LL n2=n;
		x=0;
		while(n2){
			s[x++]=n2%10;
			n2/=10;
		}
		ans=0;
		dfs(s[x-1],x-2,false,s[x-1]);
		dfs(s[x-1]-1,x-2,true,s[x-1]-1);
		printf("Case #%d: %lld\n",hh,ans);
	}
    return 0;
}
