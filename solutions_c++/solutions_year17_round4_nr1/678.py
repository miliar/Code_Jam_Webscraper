#include <bits/stdc++.h>

#define DEBUG

#ifdef DEBUG
#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
#define debug(...)
#endif

using namespace std;

int n, p;

const int N = 111;

vector<int> g;

int main(){
	int tests;
	std::cin >> tests;
	for (int test = 0; test < tests; ++test){
		std::cout << "Case #" << test + 1 << ": ";
		std::cin >> n >> p;
		int ans = 0;
		g.resize(n);
		for (int i = 0; i < n; ++i){
			std::cin >> g[i];
			g[i] %= p;
			if (g[i] == 0){
				++ans;
				--n, --i;
			}
		}
		g.resize(n);
		sort(g.begin(), g.end());
		std::vector<bool> visit(n);
		for (int i = 0; i < n; ++i){
			for (int j = i + 1; j < n; ++j){
				if (!visit[i] && !visit[j] && g[i] + g[j] == p){
					++ans;
					visit[i] = visit[j] = 1;
				}
			}
		}
		int idx = 0;
		for (int i = 0; i < n; ++i){
			if (!visit[i])
				g[idx++] = g[i];
		}
		n = idx;
		g.resize(n);
		if (n > 0){
			if (p == 2){
				assert(n == 1);
				++ans;
			} else if (p == 3){
				while (n > 0){
					n -= 3;
					++ans;
				}
			} else if (p == 4){
				if (g[0] == 2 || g.back() == 2){
					if (g[0] == 2 && n > 1){
						assert(g[1] == 3);
					} else if (g.back() == 2 && n > 1){
						assert(g[n - 2] == 1);
					}
					if (n > 0){
						n -= 3;
						++ans;
					}
					while (n > 0){
						n -= 4;
						++ans;
					}
				} else {
					int a = g[0];
					for (auto& x : g){
						assert(x == a);
					}
					while (n > 0){
						n -= 4;
						++ans;
					}
				}
			} else {
				assert(0);
			}
		}
		cout << ans << "\n";
	}
}