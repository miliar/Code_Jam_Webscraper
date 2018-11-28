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
#define fr first
#define sc second
#define MAX 50010
#define LL   int
#define ll   int
//#define LLL long long int
#define inf 1e15
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
char str[1010];
int main()
{
	int T,I=1;
	cin>>T;
	while(T--)
	{
		printf("Case #%d: ",I++);
		int k,n;
		scanf("%s %d",str,&k);
		n=strlen(str);
		int ans=0;
		for(int i=0;i<n-k+1;i++)
		{
			if(str[i]=='-')
			{
				ans++;
				for(int j=i;j<i+k;j++) 
					if(str[j]=='-') str[j]='+';
					else str[j]='-';
			}
		}
		for(int i=0;i<n;i++) if(str[i]=='-') { ans=-1;break; }
		if(ans==-1)
			printf("IMPOSSIBLE\n");
		else
		printf("%d\n",ans);
	}
	return 0;
}