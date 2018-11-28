//#include<bits/stdc++.h>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<iostream>
#include<algorithm>
#define vi vector<LL>
#define pii pair<int,int>
#define pll pair<LL,LL>
#define fr first
#define sc second
#define MAX 50010
#define LL   long long int
#define ll   long long int
//#define LLL long long int
#define inf 1e18
#define INF 10000000
#define mod 1000000007
#define N 65
#define mMax 30010
#define nMax 2010
#define SZ(a) a.size()
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define all(A) A.begin(),A.end()
using namespace std;
LL bigmod(LL a,LL b,LL Mod)
{
    if(b==0) return 1ll;
    if(b%2) return (a*bigmod(a,b-1,Mod))%Mod;
    LL c=bigmod(a,b/2,Mod);
    return (c*c)%Mod;
}
char str[30];
pll dp[30][15][3];

pll call(int ind,int last,int f)
{
	if(ind==-1) return mp(0ll,0ll) ;
	pll &ret=dp[ind][last][f];
	if(ret.fr!=-1) return ret;
	int val=str[ind]-'0';
	if(f==1) val=(val-1+10)%10;
	ret.fr=1ll*LONG_LONG_MAX;
	//if(ind==0) cout<<ind<<" "<<last<<" "<<f<<endl;
	for(int i=0;i<=last;i++)
	{
		if(ind==0 && val<i) break;
		pll temp,ans;
		temp.fr=(val-i+10)%10;
		temp.sc=i;
		ans=call(ind-1,i,(val<i)||(f==1 && val==9));
		temp.fr+= 10ll*ans.fr;
		temp.sc+= 10ll*ans.sc;
		ret=min(ret,temp);
	}
	return ret;
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
	int T,I=1;
	cin>>T;
	while(T--)
	{
		printf("Case #%d: ",I++);
		scanf("%s",str);
		for(int i=0;i<30;i++)
			for(int j=0;j<15;j++)
				for(int k=0;k<3;k++)
					dp[i][j][k]=mp(-1ll,-1ll);
		pll ans=call(strlen(str)-1,9,0);
		printf("%lld\n",ans.sc);
	}
	return 0;
}
