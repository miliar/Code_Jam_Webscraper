#include<cstdio>
#include<cstdlib>
#include<cstdlib>
#include<algorithm>

using namespace std;

int n;

struct color
{
	int num;
	char c;
	bool operator<(const color &a)const
	{
		return num>a.num;
	}
}z[10];

char res[1010];

bool map[500][500];

void solve_small()
{
	if ((z[1].num+z[2].num+z[6].num)*2>n)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	if ((z[2].num+z[3].num+z[4].num)*2>n)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	if ((z[4].num+z[5].num+z[6].num)*2>n)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	if (z[1].num<z[4].num || z[3].num<z[6].num || z[5].num<z[2].num)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	z[1].num-=z[4].num;z[3].num-=z[6].num;z[5].num-=z[2].num;
	swap(z[2],z[5]);
	int cnt=0;
	cnt=(z[4].num>=1)+(z[5].num>=1)+(z[6].num>=1);
	if (cnt>1)
	{
		cnt-=(z[1].num>=1)+(z[2].num>=1)+(z[3].num>=1);
		if (cnt>0)
		{
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	sort(z+1,z+4);
	n-=(z[4].num+z[5].num+z[6].num)*2;
	if (z[1].num*2>n || z[2].num*2>n || z[3].num*2>n)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	for (int a=1;a<=n;a++)
	{
		int p=1;
		if (res[a-1]==z[p].c) p=2;
		for (int b=2;b<=3;b++)
			if (z[b].num>z[p].num && !map[res[a-1]][z[p].c]) p=b;
		res[a]=z[p].c;
		z[p].num--;
	}
	res[n+1]=res[1];
	for (int a=1;a<=n;a++)
		if (map[res[a]][res[a+1]]) printf("GG\n");
	for (int a=1;a<=n;a++)
	{
		printf("%c",res[a]);
		if (res[a]=='R')
		{
			while (z[4].num)
				printf("GR"),z[4].num--;
		}
		if (res[a]=='Y')
		{
			while (z[6].num)
				printf("VY"),z[6].num--;
		}
		if (res[a]=='B')
		{
			while (z[5].num)
				printf("OB"),z[5].num--;
		}
	}
	if (z[4].num && z[5].num)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	if (z[6].num && z[5].num)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	if (z[4].num && z[6].num)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	while (z[4].num)
		printf("GR"),z[4].num--;
	while (z[6].num)
		printf("VY"),z[6].num--;
	while (z[5].num)
		printf("OB"),z[5].num--;
	printf("\n");
}

void solve_big()
{
}

int main()
{
	int T;
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		z[1].c='R';
		z[2].c='O';
		z[3].c='Y';
		z[4].c='G';
		z[5].c='B';
		z[6].c='V';
		z[0].c='V';
		for (int a=1;a<=5;a+=2)
		{
			map[z[a-1].c][z[a].c]=true;
			map[z[a].c][z[a-1].c]=true;
			map[z[a+1].c][z[a].c]=true;
			map[z[a].c][z[a+1].c]=true;
		}
		scanf("%d",&n);
		for (int a=1;a<=6;a++)
			scanf("%d",&z[a].num);
		printf("Case #%d: ",t);
		solve_small();
		//solve_big();
	}

	return 0;
}
