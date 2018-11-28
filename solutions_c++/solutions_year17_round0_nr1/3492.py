#include<bits/stdc++.h>
using namespace std;
const int maxn=2000;
int n,m;
char ch[maxn];
int Q[maxn],qb,qe;
int main()
{
	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);
	int T;
	cin>>T;
	for (int ca=1;ca<=T;ca++)
	{
		scanf("%s%d",&ch,&m);
		n=strlen(ch);
		qb=qe=0;
		int ans=0;
		for (int i=0;i<=n-m;i++)
		{
		    if (qb!=qe&&Q[qb+1]+m==i) qb++;
			if ((ch[i]=='+'&&(qe-qb)%2==1)||(ch[i]=='-'&&(qe-qb)%2==0))
		    {
		    	ans++;
		    	Q[++qe]=i;
			}
		}
		bool flag=1;
		for (int i=n-m+1;i<n;i++)
		{
			if (qb!=qe&&Q[qb+1]+m==i) qb++;
			if ((ch[i]=='+'&&(qe-qb)%2==1)||(ch[i]=='-'&&(qe-qb)%2==0))
			{
				flag=0;
				break;
			}
		}
		printf("Case #%d: ",ca);
		if (flag) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
		
	}//fclose(stdin);fclose(stdout);
	return 0;
}
