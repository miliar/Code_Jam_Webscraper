#include<bits/stdc++.h>

using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define ps(mark) printf("%s\n",mark);
#define pd(mark) printf("%d\n",mark);
#define pl(mark) printf("%lld\n",mark);
#define clr(mark) memset(mark,0,sizeof(mark))
#define rec(x,y) for(x=0;x<y;x++)
#define rec_1(x,y) for(x=1;x<=y;x++)
#define F first
#define S second
#define MP make_pair
#define pb push_back
#define ll long long


int main()
{

	freopen("A-large.in","r",stdin);
	freopen("A-large-attempt.out","w",stdout);
	int t;
	sd(t);
	for(int z=1;z<=t;z++)
	{
		int k=5;
		char s[1001];
		scanf(" %s %d",s,&k);
		int ans=0,flag=0;
		int len =strlen(s);
		for(int i=0;i<len;i++)
		{
			if(s[i]=='-'&& (i+k)>(len))
			{
				flag=1;
				i=i+k;
			}
			else if(s[i]=='-')
			{
				for(int j=i;j<i+k;j++)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
				ans++;
			}

		}
		if(flag==1)
		{
			printf("CASE #%d: IMPOSSIBLE\n",z);
		}
		else
		{
			printf("CASE #%d: %d\n",z,ans );
		}

	}
	return 0;
} 