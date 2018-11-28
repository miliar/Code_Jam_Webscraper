#include <bits/stdc++.h>
#define ll int
using namespace std; 
ll aA, aB, tA, tB, n, k; 
queue<ll> a, b; 
int T;
int main() 
{
	freopen("in.in", "r", stdin); 
	freopen("out.out", "w", stdout); 
	cin >> T; 
	for (int Cs = 1; Cs <= T; Cs++) 
	{
		while (!a.empty()) a.pop(); aA = 0; 
		while (!b.empty()) b.pop(); aB = 1 << 30; 
		cin >> n >> k; 
		k--; tB = (n-1)/2; tA = n-1-tB; aA = tA;  aB = tB; 
		a.push(tA); b.push(tB); 
		for (int i = 1; i <= k; i++) 
		{
			if (a.front() > b.front()) {
				n = a.front(); a.pop(); 
			}
			else {
				n = b.front(); b.pop(); 
			}
			tB = (n-1)/2; tA = n-1-tB;
			aB = min(aB, tB); 
			a.push(tA); b.push(tB); 
		}
		aA = max(a.front(), b.front()); 
		printf("Case #%d: %d %d\n", Cs, tA, tB); 
	}
}
