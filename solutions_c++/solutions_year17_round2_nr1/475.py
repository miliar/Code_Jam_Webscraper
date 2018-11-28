#include<bits/stdc++.h>
using namespace std;
#define FOR(i,s,e) for(int i = (s); i < (e); i++)
#define FOE(i,s,e) for(int i = (s); i <= (e); i++)
#define FOD(i,s,e) for(int i = (s); i >= (e); i--)
#define ll long long
#define pb push_back

int tc, n, tt;
double D, A[1005], B[1005], R, ans;

int main ()
{
	scanf("%d", &tc);
	while (tc--)
	{
		scanf("%lf %d", &D, &n);
		FOR(i, 0, n) scanf("%lf %lf", &A[i], &B[i]);
		
		FOR(i, 0, n)
		{
			R = (D - A[i]) / B[i];
			if (i == 0) ans = R;
			else ans = max(R, ans);
		}
		
		printf("Case #%d: %.10lf\n", ++tt, D / ans);
	}
	
	return 0;
}
