#include<bits/stdc++.h>
using namespace std;
int main()
{
	int i,j,t,T,k,l;
	char s[1001];
	cin>>t;
	for(T=0;T<t;++T)
	{
		j=0;
		cin>>s>>k;
		l=strlen(s);
		for(i=0;i<(l-k+1);++i)
		{
			if(s[i]=='-')
			{
				j++;
				s[i]='+';
				for(int m=1;m<k;++m)
				{
					if(s[i+m]=='-')
						s[i+m]='+';
					else
						s[i+m]='-';
				}
			}
		}
		int d=0;	
		printf("Case #%d: ",T+1);
		for(int m=1;m<k;++m)
		{
			if(s[l-m]=='-')
			{
				d=1;
				printf("IMPOSSIBLE\n");
				break;
			}
		}
		if(!d)
			printf("%d\n",j);
	}
	return 0;
}
