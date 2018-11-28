#include<cstdio>
#include<string>
#include<cstring>
#include<iostream> 
#include<algorithm> 
using namespace std;
int a[101];
inline void dfs(int d)
{
	if(d==0)
		return ;
	a[d]--;
	if(a[d]<a[d-1])
	{
		dfs(d-1);
		a[d]=9;
	}
}
int main()
{
//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,kk=0;
	scanf("%d",&T);
	while(T>0)
	{
		T--;
		kk++;
		string x;
		cin>>x;
		int lx=x.size();
		int d=0;
		bool flag=true;
		int i;
		for(i=0;i<=lx-1;i++)
		{
			if(flag)
			{
				if(x[i]-'0'>=a[d])
				{
					d++;
					a[d]=x[i]-'0';
				}
				else
				{
					dfs(d);
					d++;
					a[d]=9;
					flag=false;
				}
			}
			else
			{
				d++;
				a[d]=9;
			}
		}
		printf("Case #%d: ",kk);
		int l=1;
		while(a[l]==0)
			l++;
		for(i=l;i<=d;i++)
			printf("%d",a[i]);
		printf("\n");
	}
	return 0;
}
