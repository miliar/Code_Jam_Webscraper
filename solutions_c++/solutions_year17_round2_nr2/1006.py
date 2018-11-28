#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
struct node
{
	int data,color;
}p[11];
bool cmp(node a,node b)
{
	if (a.data>b.data) return 1;
	return 0;
}
void op(int a)
{
	if (a==1) printf("R");
	if (a==2) printf("Y");
	if (a==3) printf("B");
}
int test,n,a;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("2.out","w",stdout);
	cin>>test;
	for (int kk=1;kk<=test;kk++)
	{
		printf("Case #%d: ",kk);
		cin>>n;
		for (int i=1;i<=3;i++)
		scanf("%d%d",&p[i].data,&a),p[i].color=i;
		sort(p+1,p+4,cmp);
		if (p[1].data>n/2) 
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		for (int i=1;i<=p[1].data;i++)
		{
			op(p[1].color);
			if (p[2].data>p[3].data) op(p[2].color),p[2].data--;
			else op(p[3].color),p[3].data--;
		}
		for (int i=p[1].data*2+1;i<=n;i++)
		{
			if (p[2].data>p[3].data) op(p[2].color),p[2].data--;
			else op(p[3].color),p[3].data--;
		}
		cout<<endl;
	}
	return 0;
}
