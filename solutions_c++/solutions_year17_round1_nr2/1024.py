#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <algorithm>

int is_valid(int p, int q)
{
	int d = p/q;
	if( d!=0 && d*q *11 >= p*10 && p*10 >= d*q*9 )
		return d;
	if( (d+1)*q *11 >= p*10 && p*10 >= (d+1)*q*9 )
		return d+1;
	if(  d>=2 && (d-1)*q *11 >= p*10 && p*10 >= (d-1)*q*9 )	
		return d-1;
	return -1;
}

bool is_possible(int p, int g, int r)
{
//printf("p=%d g=%d r=%d rg=%d %d %d\n", p, g, r, r*g*11, r*g*9, p*10);
	return ( r*g *11 >= p*10 && p*10 >= r*g*9 );
}

int get_min(int p, int g)
{
	//int d = p/g;
	int m = is_valid(p, g);
	assert(m!=-1);

	//printf("p=%d g=%d m=%d\n", p, g, m);
	while( m>1 && is_possible(p, g, m-1) )
		--m;
	assert(m>0);
	return m;
	// p = g*0.9*n; // n = p/g/0.9
	// printf("p=%d g=%d\n", p, g);
	// return (int) p/(g*0.9);
}

int get_max(int p, int g)
{
	//int d = p/g;
	int m = is_valid(p, g);
	assert(m!=-1);
	while( is_possible(p, g, m+1) )
		++m;
	assert(m>0);
	return m;
	// p = g*1.1*n; // n = p/g/1.1
	//return (int) p/(g*1.1);
}

int main()
{
int N;
scanf("%d", &N);
char ch[10000];
int k;
int g[60];
int q[60][60];
//gets(ch);
for(int I=1; I<=N; ++I)
{
int n, r;
scanf("%d%d",&n,&r);
for(int i=0;i<n;++i)
	scanf("%d",&g[i]);
for(int i=0;i<n;++i)
	for(int j=0;j<r;++j) // p packages of i-th ingredient
		scanf("%d", &q[i][j]);
	//printf("S1\n");
for(int i=0; i<n; ++i)
	std::sort(q[i], q[i]+r);
	//printf("S2\n");

int kit = 0;
int last[60] = {0};
//int ps[60] = {0};
for(;;) //int __=0;__<r; ++__)
{
	bool finished = false;
	for(int i=0; i<n; ++i)
	{
		while( last[i] < r )
		{
			if(-1==is_valid(q[i][ last[i] ], g[i]))
				++last[i];
			else
				break;
		}
		if( last[i] == r )
			finished = true;
		//ps[i] = is_valid(q[i][ last[i] ], g[i]);
	}
	//for(int i=0; i<n; ++i) printf("%d ", ps[i]); printf("\n");
	//for(int i=0; i<n; ++i) printf("%d ", last[i]); printf("\n");
	if(finished)
		break;
	bool same = false;
	int _min = get_min(q[0][last[0]], g[0]);
	int _max = get_max(q[0][last[0]], g[0]);
	//printf("%d %d\n", _min, _max);
	//for(int i=1; i<n; ++i) if( ps[i] > _max ) _max = ps[i];
	//for(int i=1; i<n; ++i) if( ps[i] < _min ) _min = ps[i];
	for(int z=_min; z<=_max; ++z)
	{
		bool possible = true;
		for(int i=0; i<n; ++i)
		{
			if( !is_possible( q[i][last[i]], g[i], z ) )
			{
				possible = false;
				break;
			}
		}
		if( possible )
		{
			same = true;
			break;
		}
	}
	if(same) 
	{
		++kit;
		for(int i=0; i<n; ++i) ++last[i];
	}
	else
	{
		int min = get_min(q[0][last[0]], g[0]);
		for(int i=0; i<n; ++i) 
		{
			int d = get_min(q[i][last[i]], g[i]);
			if( d < min ) min = d;
		}
		for(int i=0; i<n; ++i) 
		{
			int d = get_min(q[i][last[i]], g[i]);
			if( d == min )
				++last[i];
		}
	}
}
	
printf("Case #%d: %d\n", I, kit);

}

return 0;
}