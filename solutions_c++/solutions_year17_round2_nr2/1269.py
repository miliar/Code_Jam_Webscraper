#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
int n,m,d;
pair<int,char>  A[10];
char s[100010];
int main()
{
	int i,j,x,r,o,y,g,b,v;
	int t,temp;
	scanf("%d",&t);
	temp=t;
	while(t--)
	{
		int sflag=0,endind;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			s[i]='#';
		scanf("%d%d%d%d%d%d",&r,&o,&y,&g,&b,&v);
		A[0]=mp(r,'R'),A[1]=mp(b,'B'),A[2]=mp(y,'Y');
		sort(A,A+3);
		int m= A[2].first;
		char c=A[2].second;
		i=0;
		for(i=0;i<n;i+=2)
		{	if (m==0)
			{	endind=i;
				break;
			}
			s[i]=c;m--;
		}
		if (m || s[n-1]==s[0])
			sflag=-1;
		else
		{
			m= A[1].first;
			c=A[1].second;
			for(i=endind;i<n;i+=2)
		{	if (m==0)
			{	endind=i;
				break;
			}
			s[i]=c;m--;
		}
		if (m)
		{
		for(i=1;i<n;i+=2)
		{	if (m==0)
			{	endind=i;
				break;
			}
			s[i]=c;m--;
		}
		}
		if (m)
			sflag=-1;
		else
		{
		c= A[0].second;
		for(i=0;i<n;i++)
			if (s[i]=='#')
				s[i]=c;
		
		
		}
		}	
		
		printf("Case #%d: ",temp-t);
		if (sflag==-1)
			printf("IMPOSSIBLE");
		else{
		for(i=0;i<n;i++)
			printf("%c",s[i]);}
		printf("\n");
	}
	return 0;
}
