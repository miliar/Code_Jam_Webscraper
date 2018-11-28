#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm>
#include <iostream> 
#include <string.h> 
#include <stdlib.h>
#include <complex>
#include <sstream> 
#include <fstream>
#include <numeric>
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
using namespace std;

#define pi acos(-1.0)
#define eps 1e-9
#define mod 1000000007

int T, n, k;

struct segment
{
	int L, R;
	segment(int L, int R) : L(L), R(R) {}
	bool operator<(const segment& b) const
	{
		if(R - L != b.R - b.L)
			return R - L > b.R - b.L;
		return L < b.L;
	}
};

int main()
{
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
	{
		scanf("%d %d", &n, &k);
		set<segment> s;
		s.insert(segment(1, n));
		int minv, maxv;
		for(int i = 0; i < k; i++)
		{
			segment cur = *s.begin();
			s.erase(s.begin());
			int C = (cur.L + cur.R) / 2;
			minv = C - cur.L;
			maxv = cur.R - C;
			if(minv > 0)
				s.insert(segment(cur.L, C - 1));
			if(maxv > 0)
				s.insert(segment(C + 1, cur.R));
		}
		printf("Case #%d: %d %d\n", t, maxv, minv);
	}
	return 0;
}