#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int a[101],s[5];
int main()
{
//	freopen("A-small-attempt1.in","r",stdin);
//	freopen("A-small-attempt1.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,kk=0;
	scanf("%d",&T);
	while(T>0)
	{
		kk++;
		memset(s,0,sizeof(s));
		T--;
		int n,p;
		scanf("%d%d",&n,&p);
		int i,j,k;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			a[i]%=p;
			s[a[i]]++;
		}
		int ans=0;
		if(p==2)
		{
			ans=s[0];
			if(s[1]!=0)
				ans+=(s[1]-1)/2+1;
		}
		else if(p==3)
		{
			ans=s[0];
			if(s[1]>s[2])
			{
				ans+=s[2];
				s[1]-=s[2];
				if(s[1]!=0)
					ans+=(s[1]-1)/3+1;
			}
			else
			{
				ans+=s[1];
				s[2]-=s[1];
				if(s[2]!=0)
					ans+=(s[2]-1)/3+1;
			}
		}
		else
		{
			ans=s[0];
			if(s[2]!=0)
				ans+=s[2]/2;
			s[2]%=2;
			if(s[1]>s[3])
			{
				ans+=s[3];
				s[1]-=s[3];
				s[3]=0;
				if(s[1]!=0)
				{
					ans+=s[1]/4;
					s[1]%=4;
				}
			}
			else
			{
				ans+=s[1];
				s[3]-=s[1];
				s[1]=0;
				if(s[3]!=0)
				{
					ans+=s[3]/4;
					s[3]%=4;
				}
			}
			if(s[2]==1)
			{
				if(s[3]<=2&&s[1]<=2)
					ans++;
				else
					ans+=2;
			}
			else
			{
				if(s[3]>0||s[1]>0)
					ans++;
			}
		}
		printf("Case #%d: %d\n",kk,ans);
	}
	return 0;
}
