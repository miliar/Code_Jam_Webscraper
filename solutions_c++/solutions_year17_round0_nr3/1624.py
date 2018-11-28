#include<bits/stdc++.h>
using namespace std;
#define FOR(i,s,e) for(int i = (s); i < (e); i++)
#define FOE(i,s,e) for(int i = (s); i <= (e); i++)
#define FOD(i,s,e) for(int i = (s); i >= (e); i--)
#define ll long long
#define pb push_back

int tc, tt, w;
ll n, k, large, small, x, K;
int A[1005];

int main ()
{
	scanf("%d", &tc);
	while (tc--)
	{
		scanf("%lld %lld", &n, &K);	
		
		w = 0;
		k = K;
		while (k > 1ll)
		{
			w++; 
			k /= 2ll;
		}
		
		k = K;
		large = 0ll;
		small = 1ll;
		x = 1ll;
		
		FOR(i, 0, w)
		{
			n--;
			if (n % 2ll == 0ll) 
			{
				small = large + small * 2ll;
				large = large;
			}
			else 
			{
				large = large + large + small;
				small = small;
			}
			
			k -= x;
			x *= 2ll;
			n /= 2ll;
		}
		
		if (k > large) n--;
		printf("Case #%d: %lld %lld\n", ++tt, n - n / 2ll, n / 2ll);
		
	}
	
	return 0;
}
