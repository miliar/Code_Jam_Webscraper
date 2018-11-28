#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ll long long

string s;

int main()
{
	// freopen ("A1.in","r",stdin);
	// freopen ("A1.out","w",stdout);
	int t;
	sd(t);
	for(int tt=1;tt<=t;tt++)
	{
		cin>>s;
		int n=s.length();
		int k,i,j;
		sd(k);
		int ans=0;
		for(i=0;i+k-1<n;i++)
		{
			if(s[i]=='+')	continue;
			ans++;
			for(j=0;j<k;j++)
				s[i+j]=(s[i+j]=='+'?'-':'+');
		}
		for(i=0;i<n;i++)
			if(s[i]!='+')
				ans=-1;

		printf("Case #%d: ",tt);
		if(ans==-1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
}