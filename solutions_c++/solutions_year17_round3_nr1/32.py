#include <bits/stdc++.h>
#define N 1010
#define db double
#define ll long long
#define sqr(x) ((x)*(x))
using namespace std; 
struct pan
{
	ll r, h; 
}a[N]; 
ll n, k, w[N], sum, ans;
int T; 
multiset <ll> s;  
const db PI = acos(-1.0); 
bool cmp(pan a, pan b) 
{
	if (a.r == b.r) return a.h > b.h; 
	return a.r > b.r; 
}
void init()
{
	ans = 0; sum = 0;
	memset(w, 0, sizeof(w)); 
}
int main()
{
	freopen("a.in", "r", stdin); 
	freopen("a.out", "w", stdout); 
	cin >> T; 
	for (int Cs = 1; Cs <= T; Cs++) 
	{
		init(); 
		cin >> n >> k; 
		for (int i = 1; i <= n; i++) 
			scanf("%I64d%I64d", &a[i].r, &a[i].h); 
		sort(a + 1, a + n + 1, cmp); 
		for (int i = n; i >= 1; i--)
			w[i] = a[i].r * a[i].h; 
		s.clear(); 
		for (int i = n; i >= 1; i--) 
		{
			s.insert(w[i]); sum += w[i]; 
			if (s.size() == k) {
				sum -= *s.begin(); 
				s.erase(s.begin()); 
			}
			w[i] = sum; 
		}
		for (int i = 1; i <= n; i++) 
		{
			ll t = sqr(a[i].r) + a[i].r * a[i].h * 2 + w[i + 1] * 2; 
			ans = max(ans, t); 
		}
		printf("Case #%d: %.10lf\n", Cs, ans * PI); 
	}
	return 0; 
}
