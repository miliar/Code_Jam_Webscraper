#include <bits/stdc++.h>
using namespace std;

int t,caso,a[1010],n,cont,total,soma;
string s;

int main()
{
	scanf("%d",&t);
	while(caso<t)
	{
		total=soma=0;
		cont = 0;
		cin >> s >> n;
		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='+') a[i]=1;
			else a[i]=0;
		}
		// for(int i=0;i<s.size();i++)
		// {
		// 	if(a[i]==0) cont++;
		// 	else cont=0;
		// 	if(cont==n) 
		// 	{
		// 		for(int j=0;j<n;j++) a[i-j]=1,cont=0;
		// 		total++;
		// 	}
		// }

		for(int i=0;i<s.size()-n+1;i++)
		{
			if(a[i]==0)
			{
				for(int j=0;j<n;j++) a[i+j] = 1-a[i+j];
				total++;
			}
		}		
		for(int i=0;i<s.size();i++) soma+=a[i];
		(soma==s.size())? printf("Case #%d: %d\n",caso+1,total) : printf("Case #%d: IMPOSSIBLE\n",caso+1);
		memset(a,0,sizeof(a));
		caso++;
	}
}

/*

-+-+- 4
+-+--
++--+


-+++---- 3
+--+----
+++-----
++++++--
-++-++






*/