#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

struct aaa
{
	int num;
	double r,h,value;
}s[1005];

int O=0,T,N,K;
double ANS;

void qqqsort()
{
	int i,j,k;
	double tmp;
	for (i=1;i<=N;i++)
	{
		tmp=0;
		for (j=i;j<=N;j++)
		{
			if (s[j].value>tmp)
			{
				k=j;
				tmp=s[j].value;
			}
		}
		swap(s[i],s[k]);
	}
}

double area(int i)
{
	double Q=0;
	Q+=s[i].r*2.0*3.1415926535898*s[i].h;
	return Q;
}

double areaaaa(int i)
{
	return s[i].r*s[i].r*3.1415926535898;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	int i,j,num;
	double tmp;
	while (T--)
	{
		++O;
		printf("Case #%d: ",O);
		ANS=0;
		scanf("%d%d",&N,&K);
		for (i=1;i<=N;i++)
		{
			scanf("%lf%lf",&s[i].r,&s[i].h);
			s[i].value=area(i)+areaaaa(i);
			s[i].num=i;
		}
		tmp=0;
		for (i=1;i<=N;i++)
		{
			if (s[i].value>tmp)
			{
				tmp=s[i].value;
				j=i;
			}
		}
		ANS+=tmp;
		num=s[j].num;
		for (i=1;i<=N;i++)	s[i].value-=areaaaa(i);
		qqqsort();
		j=0;
		if (K>1)
		{
			for (i=1;i<=N;i++)
			{
				if (s[i].num!=num)
				{
					++j;
					ANS+=s[i].value;
					if (j==K-1)	break;
				}
			}
		}
		printf("%0.9lf\n",ANS);
	}
	return 0;
}
