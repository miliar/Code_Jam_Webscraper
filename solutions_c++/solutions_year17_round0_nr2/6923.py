#include <bits/stdc++.h>
#define ll long long
using namespace std; 
int T; 
ll n; 
ll Find(ll x) 
{
	if (x < 10) return x; 
	ll t = Find(x / 10); 
	if (x % 10 < t % 10) return Find(x - 1); 
	return t * 10 + x % 10; 
}
int main()  
{
	freopen("in.in", "r", stdin); 
	freopen("out.out", "w", stdout); 
	scanf("%d", &T); 
	for (int Cs = 1; Cs <= T; Cs++)
	{
		cin >> n; 
		cout << "Case #" << Cs << ": " << Find(n) << endl; 
	}
}
