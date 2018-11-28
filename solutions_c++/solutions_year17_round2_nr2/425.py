#include <bits/stdc++.h>
using namespace std;
int Ts, N, Q, u, v, R, O, Y, G, B, V;
typedef pair<int, char> T;
void solve(int N, int R, int Y, int B) {
	if (R*2>N) {puts("IMPOSSIBLE"); return;}
	if (Y*2>N) {puts("IMPOSSIBLE"); return;}
	if (B*2>N) {puts("IMPOSSIBLE"); return;}
	priority_queue< T > pq;
	if(B) pq.push(T(B, 'B'));
	if(R) pq.push(T(R, 'R'));
	if(Y) pq.push(T(Y, 'Y'));
	string buf = "";
	T tmp(-1, 0);
	while(pq.size()) {
		T o = pq.top(); pq.pop();
		buf += o.second;
		if (tmp.first > 0) pq.push(tmp);
		o.first -= 1; tmp = o;
	}
	if (buf[buf.length()-1] == buf[0]) {
		swap(buf[buf.length()-1], buf[buf.length()-2]);
		fprintf(stderr,"%c %c%c%c\n", buf[0], buf[buf.length()-3], buf[buf.length()-2], buf[buf.length()-1]);
	}
	puts(buf.c_str());
}
int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d", &Ts);
	for(int Ks=1; Ks<=Ts; Ks++) {
		scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V); 
		printf("Case #%d: ", Ks);
		solve(N, R, Y, B);
	}
}
