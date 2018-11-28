#include <bits/stdc++.h>

int main(){
	int tests;
	std::cin >> tests;
	for (int test = 0; test < tests; ++test){
		std::cout << "Case #" << test + 1 << ": ";
		int n, p;
		std::cin >> n >> p;
		std::vector<int> r(n);
		for (int i = 0; i < n; ++i){
			std::cin >> r[i];
		}
		std::vector<std::vector<int>> q(n, std::vector<int>(p));
		for (int i = 0; i < n; ++i){
			for (int j = 0; j < p; ++j){
				std::cin >> q[i][j];
			}
		}
		std::vector<int> point(n);
		for (int i = 0; i < n; ++i){
			std::sort(q[i].begin(), q[i].end());
		}
		int ans = 0;
		for (int i = 0; i < p; ++i){
			int down = q[0][i] * 10 / 11, up = q[0][i] * 10 / 9;
			if (q[0][i] % 11 != 0){
				++down;
			}
			up /= r[0];
			if (down % r[0] != 0){
				down /= r[0];
				++down;
			} else {
				down /= r[0];
			}
			if (down > up)
				continue;
			int maxdown = down, minup = up;
			int upper = 0;
			int totalflag = 0;
			for (int k = 1; k < n; ++k){
				int flag = 0;
				while (flag == 0){
					int j = point[k];
					int down = q[k][j] * 10 / 11, up = q[k][j] * 10 / 9;
					if (q[k][j] % 11 != 0){
						++down;
					}
					up /= r[k];
					if (down % r[k] != 0){
						down /= r[k];
						++down;
					} else {
						down /= r[k];
					}
					//std::cout << maxdown << " " << minup << " " << down << " " << up << "\n";
					if (down > up || up < maxdown){
						++point[k];
						if (point[k] >= p){
							flag = 2;
							break;
						}
						continue;
					}
					if (down > minup){
						++point[upper];
						flag = 2;
						break;
					}
					if (up < minup){
						upper = k;
						minup = up;
					}
					if (down > maxdown){
						maxdown = down;
					}
					flag = 1;
				}
				if (flag == 2)
					break;
				++totalflag;
			}
			//std::cout << totalflag << "\n";
			if (totalflag == n - 1){
				++ans;
				for (auto& x : point){
					++x;
				}
			}
			int flag = 0;
			for (auto& x : point){
				if (x >= p){
					flag = 1;
					break;
				}
			}
			if (flag)
				break;
		}
		std::cout << ans << "\n";
	}
}