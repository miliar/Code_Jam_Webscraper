#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <long long, long long> pll;

int main()
{
	int tt, n, k, x, cont;
	scanf("%d", &tt);
	for (int t = 0; t < tt; t++) {
		scanf("%d %d", &n, &k);
		multiset <int> s;
		s.insert(n);
		cont = 0;
		while (!s.empty()) {
			cont++;
			x = *(s.rbegin());
			if (cont == k) {
				if (x%2 != 0) printf("Case #%d: %d %d\n", t+1, x/2, x/2);
				else printf("Case #%d: %d %d\n", t+1, x/2, (x-1)/2);
				break;
			}
			if (x%2 != 0) {
				s.insert(x/2);
				s.insert(x/2);
			}
			else {
				s.insert(x/2);
				s.insert((x-1)/2);
			}
			s.erase(s.find(x));
		}
	}	

	return 0;
}