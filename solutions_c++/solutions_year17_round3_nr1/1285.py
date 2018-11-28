#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

#define M_PI 3.14159265358979323846

struct pan
{
	long double r, h;
};
	
bool comp(pan &p1, pan &p2)
{
	return p1.r * p1.h > p2.r * p2.h;
}
	
int main()
{
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		vector<pan> v;
		for(int i = 0; i < n; i++)
		{
			pan p;
			scanf("%Lf %Lf", &p.r, &p.h);
			v.push_back(p);
		}
		
		sort(v.begin(), v.end(), comp);
		
		long double res = 0;
		
		long double maxR = 0;
		
		for(int i = 0; i < k-1; i++)
		{
			res += v[i].r * v[i].h;
			if(maxR < v[i].r)
				maxR = v[i].r;
		}
		
		res *= 2;
		
		long double m = 2 * v[k-1].r * v[k-1].h + max(maxR, v[k-1].r) * max(maxR, v[k-1].r);
		long double maxRes = res + m;
		for(int i = k; i < v.size(); i++)
		{
			m = 2 * v[i].r * v[i].h + max(maxR, v[i].r) * max(maxR, v[i].r);
			if(res + m > maxRes)
				maxRes = res + m;
		}
		maxRes *= M_PI;
		printf("Case #%d: ", tt);
		printf("%Lf\n", maxRes);
	}
	return 0;
}

