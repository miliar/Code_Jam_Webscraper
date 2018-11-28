#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <vector>
#include <math.h>
#include <algorithm>

//char cake[30][30];

// bool fill_if_empty(int x1, int y1, int x2, int y2, char c)
// {
	// bool empty = true;
	// for(int i=x1; i<=x2; ++i)
		// for(int j=y1; j<=y2; ++j)
			// if( cake[i][j] != '?' && cake[i][j] != c )
				// empty = false;
	// if( !empty )
		// return false;
	// for(int i=x1; i<=x2; ++i)
		// for(int j=y1; j<=y2; ++j)
			// if( cake[i][j] == '?' )
				// cake[i][j] = c;
	// return true;
// }


struct cake {
	int r, h;
	bool operator < (const cake& other) const
	{
		if( r != other.r )
			return r > other.r;
			
		return h < other.h;
	}
};

int main()
{
int N;
scanf("%d", &N);
char ch[10000];
int k;
gets(ch);
cake c[1005];

for(int I=1; I<=N; ++I)
{
	int n, k;
	scanf("%d%d",&n,&k);
	gets(ch);
	for(int i=0;i<n;++i)
	{
		scanf("%d%d", &c[i].r, &c[i].h);
	}
	std::sort(c, c+n);
	long long max = 0;
	for(int i=0; i<n; ++i)
	{
		std::vector<long long> v;
		for(int j=i+1; j<n; ++j)
		{
			assert(c[j].r <=c[i].r);
			v.push_back(c[j].r*(long long)c[j].h);
		}
		//printf("%d %d %lf\n", i, c[i].r, max);
		std::sort(v.begin(), v.end());
		if(v.size()>=k-1)
		{
			long long m = c[i].r*(long long)(c[i].r + 2*c[i].h);
			for(int j=v.size()-k+1; j<v.size(); ++j)
			{
				m += v[j] * 2;
			}
			//printf("%d %d %lld\n", n-1-k, n-1, m);
			if( m > max )
				max = m;
		}
		else
			break;
	}

	long double D = max;
	D *= acos(0);
	D *= 2;
printf("Case #%d: %Lf\n", I, D);
// for(int i=0; i<r; ++i)
	// puts(cake[i]);


}

return 0;
}