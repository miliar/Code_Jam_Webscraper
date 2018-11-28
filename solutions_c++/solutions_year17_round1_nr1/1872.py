#define F(n) Fi(i,n)
#define Fi(i,n) Fl(i,0,n)
#define Fl(i,l,n) for(int i=(l);i<(n);++i)
#include <bits/stdc++.h>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/priority_queue.hpp>
using namespace std;
// using namespace __gnu_pbds;
int t, r, c;
char cake[50][50];
void hdfs(int x, int y, char ch) {
	if (y < 0 || y >= c || cake[x][y] != '?') return;
	cake[x][y] = ch;
	hdfs(x, y-1, ch), hdfs(x, y+1, ch);
}
void vdfs(int x, int s) {
	// cout << "TEST: " << x << '\n';
	if (x < 0 || x >= r || cake[x][0] != '?') return;
	F(c) cake[x][i] = cake[s][i];
	vdfs(x-1, s), vdfs(x+1, s);
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> t;
	Fl(cases, 1, t+1) {
		cin >> r >> c;
		F(r) cin >> cake[i];
		F(r) Fi(j, c) if (cake[i][j] != '?')
			hdfs(i, j-1, cake[i][j]), hdfs(i, j+1, cake[i][j]);
		F(r) if (cake[i][0] != '?')
			vdfs(i-1, i), vdfs(i+1, i);
		cout << "Case #" << cases << ":\n";
		F(r) cout << cake[i] << '\n';
	}
}