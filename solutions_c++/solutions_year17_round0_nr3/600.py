#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
int calc(long long n, long long *vmax, long long *vmin)
{
	if (n&1)
	{
		*vmax = *vmin = n/2;
	} else
	{
		*vmax = n/2;
		*vmin = n/2;
		(*vmin)--;
	}
	return 0;
}

int solve(long long n, long long *v1, long long *v2, long long sum, long long *s1, long long *s2)
{
	if (n & 1){
		if (*v1 == (n>>1))
			*s1 += (2LL*sum);
		else
			*s2 += (2LL*sum);
	} else
	{
		*v1 = n>>1;
		*v2 = (n>>1) -1;
		*s1 = *s2 = sum;
	}
	return 0;
} 

int main()
{
	FILE *fp, *fo;
	
	int n, m, tot, tt;
	fp = fopen("c.input", "r");
	fo = fopen("c.output", "w");
	fscanf(fp, "%d\n", &tot);
	for (tt = 1; tt <= tot; tt++)
	{
		long long n, m, ans1, ans2;
		long long n1, n2, sum1, sum2;
		fscanf(fp, "%I64d%I64d", &n, &m);
		fprintf(fo, "Case #%d: ", tt);
		if (m > n){
			ans1 = ans2 = 0;
		} else
		if (m == 1)
		{
			calc(n, &ans1, &ans2);
		} else
		{
			n1 = n;
			n2 = n-1;
			sum1 = 1;
			sum2 = 0;

			while (m > sum1+sum2){
				m -= (sum1+sum2);
				if (n1 & 1){
					swap(n1, n2);
					swap(sum1, sum2);
				}

				long long v1, v2, s1 = 0, s2 = 0;
				solve(n1, &v1, &v2, sum1, &s1, &s2);
				solve(n2, &v1, &v2, sum2, &s1, &s2);
				sum1 = s1;
				sum2 = s2;
				n1 = v1;
				n2 = v2;
			}
			if (n1 < n2){
				swap(n1, n2);
				swap(sum1, sum2);
			}
			
			if (m <= sum1)
				calc(n1, &ans1, &ans2);
			else
				calc(n2, &ans1, &ans2); 
		}

		fprintf(fo, "%I64d %I64d\n", ans1, ans2);
	}
	fclose(fp);
	fclose(fo);
	return 0;	
} 
