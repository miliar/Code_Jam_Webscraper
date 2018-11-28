#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

int T,L;
long long N;
int now[22];
bool flag;

bool num(int i)
{
	int p;
	long long tmp,q,ans=0;
	for (p=1;p<=i;p++)
	{
		tmp=1;
		q=L-p;
		while (q--)	tmp*=10;
		ans+=now[p]*tmp;
	}
	if (ans<=N)	return true;
	return false;
}

void print()
{
	int i,j;
	if (now[1]==0)	j=2;
	else	j=1;
	for (i=j;i<=L;i++)
		printf("%d",now[i]);
	printf("\n");
}

void solve(int i,int k)
{
	int j;
	for (j=9;j>=k;j--)
	{
		if (!flag)
		{
			now[i]=j;
			if (num(i))
				if (i<L)
					solve(i+1,j);
				else
				{
					print();
					flag=true;
				}
		}
	}
}

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&T);
	long long tmp;
	int O;
	for (O=1;O<=T;O++)
	{
		printf("Case #%d: ",O);
		scanf("%lld",&N);
		tmp=N;	L=0;
		while (tmp/10>0)
		{
			++L;
			tmp/=10;
		}
		L++;
		flag=false;
		solve(1,0);
	}
	return 0;
}
