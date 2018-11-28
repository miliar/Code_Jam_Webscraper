#include<bits/stdc++.h>
using namespace std;
const int maxn=30;
int R,C;
char ch[maxn][maxn];
bool check(int j)
{
	for (int i=0;i<R;i++) if (ch[i][j]!='?') return 1;
	return 0;
}
void make(int j)
{
	int k;
	for (k=0;k<R;k++) if (ch[k][j]!='?') break;
	char op=ch[k][j];
	for (int i=0;i<k;i++) ch[i][j]=op;
	for (int i=k+1;i<R;i++)
	    if (ch[i][j]=='?') ch[i][j]=op;
	    else op=ch[i][j];
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;cin>>T;
	for (int ca=1;ca<=T;ca++)
	{
		scanf("%d%d",&R,&C);
		for (int i=0;i<R;i++) scanf("%s",ch[i]);
		int k;
		for (k=0;k<C;k++)
		    if (check(k))
		        break;
		make(k);
		for (int j=0;j<k;j++)
		    for (int i=0;i<R;i++)
		        ch[i][j]=ch[i][k];
		for (int j=k+1;j<C;j++)
		    if (check(j)) make(j);
		    else
		        for (int i=0;i<R;i++)
		            ch[i][j]=ch[i][j-1];
		printf("Case #%d:\n",ca);
		for (int i=0;i<R;i++) printf("%s\n",ch[i]);
	}
	return 0;
	fclose(stdin);fclose(stdout);
}
