#include <bits/stdc++.h>
using namespace std;
multiset <int> s;
multiset <int> ::iterator it;
int main()
{
	int t,p=1;
	scanf("%d",&t);
	while(t--)
	{
		char a[110];
		int b[110];
		scanf("%s",a);
		int l;
		l=strlen(a);
		printf("Case #%d: ",p);
		if(l==1)
		{
			printf("%s",a);
			printf("\n");
			p++;
			continue;
		}
		for(int i=0;i<l;i++)
		{
			b[i]=a[i]-'0';
			//s.insert(b[i]);
		}
		int f=0;
		for(int i=l-1;i>=0;i--)
		{
			f=0;
			int x=b[0];
			for(int j=1;j<=i;j++)
			{
				if(x>b[j])
				{
					f=1;
					break;
				}
				else
				{
					x=b[j];
				}
			}
			if(f==1)
			{
				b[i]=9;
				for(int j=i-1;j>=0;j--)
				{
					if(b[j]==0)
					{
						b[j]=9;
					}
					else
					{
						b[j]=b[j]-1;
						break;
					}
				}
			}
			else
				break;
		}
		if(b[0]>0)
			printf("%d",b[0]);
		for(int i=1;i<l;i++)
		{
			printf("%d",b[i]);
		}
		printf("\n");
		s.clear();
		p++;
	}
}