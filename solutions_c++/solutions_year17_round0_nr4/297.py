#include <bits/stdc++.h>

using namespace std;

typedef long long lint;

int fku;

bool mysort(int a, int b){
	return abs(a) > abs(b);
}

int main(){
	// freopen("D-large.in","r",stdin);
	// freopen("answer.out","w",stdout);
	cin.sync_with_stdio(0); cin.tie(0);
	int T; cin >> T;
	for (int tc = 1; tc <= T; ++tc){
		int n, m; cin >> n >> m;
		fku = n + 1;
		vector<int> hori, vert, diag1, diag2;
		bool modified[110][110]; memset(modified, false, sizeof(modified));
		bool plus[110][110], mult[110][110]; memset(plus, false, sizeof(plus)); memset(mult, false, sizeof(mult));
		for (int i=1; i<=n; ++i){
			hori.push_back(i);
			vert.push_back(i);
		}
		//1 - 100, to 100 - 1
		for (int d=1-n; d <= n - 1; ++d){
			diag1.push_back(d);
		}
		for (int i=2; i<=n+n; ++i){
			diag2.push_back(i);
		}
		int ans = 0;

		for (int qq=0; qq<m; ++qq){
			char ch; int r, c; cin >> ch >> r >> c;
			if (ch == 'o' || ch == '+'){
				plus[r][c] = true;
				ans++;
				diag1.erase(find(diag1.begin(), diag1.end(), r-c)); diag2.erase(find(diag2.begin(), diag2.end(), r+c));
			}
			if (ch == 'o' || ch == 'x'){
				mult[r][c] = true;
				ans++;
				hori.erase(find(hori.begin(), hori.end(), r)); vert.erase(find(vert.begin(), vert.end(), c));
			}
		}
		for (int i=0; i<hori.size(); ++i){
			if (i < vert.size()){
				int r = hori[i];
				int c = vert[i];
				mult[r][c] = true; modified[r][c] = true;
				ans++;
			}
		}
		sort(diag1.begin(), diag1.end(), mysort);
		for (int d1 : diag1){
			for (int i=0; i<diag2.size(); ++i){
				int d2 = diag2[i];
				if (((d1+200) % 2) != (d2 % 2)) continue;
				int r = (d1 + d2)/2, c = (d2 - d1)/2;
				if (1 <= r && r <= n && 1 <= c && c <= n){
					plus[r][c] = true; modified[r][c] = true;
					ans++;
					diag2.erase(find(diag2.begin(), diag2.end(), d2));
					break;
				}
			}
		}

		printf("Case #%d: ", tc);
		int nmodified = 0;
		for (int r=1; r<=n; ++r){
			for (int c = 1; c<=n; ++c){
				if (modified[r][c]) nmodified++;
			}
		}
		printf("%d %d\n", ans, nmodified);
		for (int r=1; r<=n; ++r){
			for (int c = 1; c<=n; ++c){
				if (modified[r][c]){
					if (plus[r][c] && mult[r][c]){
						printf("%c %d %d\n", 'o', r, c);
					}
					else if (plus[r][c]){
						printf("%c %d %d\n", '+', r, c);
					}
					else if (mult[r][c]){
						printf("%c %d %d\n", 'x', r, c);
					}
				}
			}
		}
	}
	return 0;
}