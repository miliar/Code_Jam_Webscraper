/******************************************
*    AUTHOR:         CHIRAG AGARWAL       *
*    INSTITUITION:   BITS PILANI, PILANI  *
******************************************/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL; 
typedef long double LD;
const int MAX=1003;

map<int,int> mp;
int st[MAX];
int sp[MAX];

int main() 
{
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		mp.clear();
		int dest,n;
		scanf("%d %d",&dest,&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%d %d",&st[i],&sp[i]);
			mp[st[i]]=max(mp[st[i]],sp[i]);
		}	
		double ans=1e17;
		for(map<int,int>::iterator it=mp.begin();it!=mp.end();it++)
		{
			double left=dest-(it->first);
			double tt=left/it->second;
			double tr1=(it->first)/tt;
			ans=min(ans,tr1+it->second);
		}
		printf("Case #%d: %lf\n",tc,ans);
	}	
	return 0;
}
60/8/