#include<iostream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

struct pos {
	int i;
	int m;
	int x;
};

typedef struct pos pos;

int main(){ 
	int t;
	cin >> t;
	int n, k;
	vector<pos> p;
	int mn, mx, i, y;
	for (int z = 0; z<t; z++) {
		cin >> n >> k;
		if (k>(n*.75)) {
			cout << "Case #" << z + 1 << ": " << 0 << " " << 0 << endl;
			continue;
		}
		int * stalls = new int[n+2]();
		stalls[0] = 1; stalls[n + 1] = 1;
		for (int j = 0; j<k; j++) {
			mn = 0, mx = 0, i = 0, y = 0;
			for (int l = 1; l<=n; l++) {
				if (stalls[l] == 1) {
					continue;
				}
				else {
					int ls = 0, rs = 0;
					for (int m = l - 1; m>0; m--) {
						if (stalls[m] == 1) {
							break;
						}
						ls++;
					}
					for (int m = l + 1; m<=n; m++) {
						if (stalls[m] == 1) {
							break;
						}
						rs++;
					}
					if (min(ls, rs) >= mn) {
						if (min(ls, rs) > mn) {
							p.clear();
							i = 0;
						}	
						mn = min(ls, rs);
						i++;
						p.resize(i);
						p[i-1].i = l;
						p[i-1].m = mn;
						p[i-1].x = max(ls, rs);
						}
					}
				}
				if (i == 1) {
					stalls[p[0].i] = 1;
				}
				else {
					y = 0;
					for (int u = 0; u<i; u++) {
						if (p[u].x>mx) {
							mx = p[u].x;
							y = u;
						}
					}
					stalls[p[y].i] = 1;
				}
			}
		cout << "Case #" << z + 1 << ": " << p[y].x << " " << p[y].m << endl;
		}
		
	}

