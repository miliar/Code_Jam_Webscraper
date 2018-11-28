#include <bits/stdc++.h>
using namespace std;

char g[30][30];

int main() {
	freopen("A-large.in","r",stdin);
	freopen("a2.out","w",stdout);
	int T; cin >> T;
	for(int as=0; as<T; as++) {
		int a,b; cin >> a >> b;
		for(int x=0; x<a;x++)for(int y=0; y<b; y++) cin >> g[x][y];
		int f = -1;
		for(int x=0; x<a; x++) {
			int h = -1;
			for(int y=0; y<b; y++) if(g[x][y]!='?') {h=y; break;}
			if(h!=-1) {
				if(f == -1) f = x;
				for(int y=h-1; y>=0; y--) g[x][y]=g[x][y+1];
				for(int y=h+1; y<b; y++) {
					if(g[x][y]=='?') g[x][y]=g[x][y-1];
				}
			} else {
				if(f == -1) continue;
				for(int y=0; y<b; y++) g[x][y]=g[x-1][y];
			}
		}
		for(int x=f-1; x>=0; x--) for(int y=0; y<b;y++)
			g[x][y] = g[x+1][y];
		cout << "Case #" << as+1 << ":\n";
		for(int x=0; x<a; x++) {for(int y=0; y<b; y++) {
			cout << g[x][y]; } cout << endl;}
	}
}
