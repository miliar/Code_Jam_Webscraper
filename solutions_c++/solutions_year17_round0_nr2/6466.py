#include <stdio.h>
#include <algorithm>
#include <vector>
#define pb push_back
#define sz(V) ((int)(V).size())
#define allv(V) ((V).begin()),((V).end())
using namespace std;
typedef long long ll;
inline void removeZeros(vector<int>& V) {
	for(reverse(allv(V)); !V.back(); V.pop_back());
	reverse(allv(V));
}
inline void prtAns(const int& t_i, vector<int>& V) {
	printf("Case #%d: ", t_i); removeZeros(V);
	for(const int& v : V) putchar(v + '0');
	putchar('\n');
}

vector<int> V;
ll N; int T;

int main() {
	scanf("%d", &T); for(int t_i = 1; t_i <= T; t_i++) {
		scanf("%lld", &N); vector<int>().swap(V);
		for(; N; V.pb(N%10), N/=10);
		reverse(allv(V));
		int sidx = sz(V)-1; for(int i = 1; i < sz(V); i++)
			if(V[i-1] > V[i]) { sidx = i-1; break; }
		if(sidx == sz(V)-1) { prtAns(t_i, V); continue; }
		for(; 0 < sidx && V[sidx] == V[sidx-1]; sidx--);
		V[sidx]--; for(int i = sidx+1; i < sz(V); i++) V[i] = 9;
		prtAns(t_i, V);
	}
	return 0;
}
