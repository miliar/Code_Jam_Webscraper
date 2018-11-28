#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

#define M_PIl 3.141592653589793238462643383279502884L

int main()
{
	freopen("inp.in", "r", stdin);
	freopen("output.txt","w",stdout);

	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; ++t) {
		int n, k;
		scanf("%d %d", &n, &k);
		vector<int> R(n), H(n);
		map<long long, int> rh2;
		vector<vector<int>> num(n);
		int count = 0;
		int count2 = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d %d", &R[i], &H[i]);
			long long buf = (long long)R[i] * (long long)H[i] * (long long)2;
			if (rh2.find(buf) == rh2.end()) {
				rh2[buf] = count;
				num[count].push_back(i);
				++count;
			} else {
				num[rh2[buf]].push_back(i);
			}
		}
		int i = 0;
		long long maxr = 0;
		long long ans = 0;
		long long lasth = 0;
		long long jj = 0;
		map<long long, int>::reverse_iterator it = rh2.rbegin();
		int flag = 0;
		for (; it != rh2.rend() && i < k; ++it) {
			int size = num[(*it).second].size();
			for (int j = 0; j < size; ++j) {
				++i;
				if (R[num[(*it).second][j]] > maxr)
					maxr = R[num[(*it).second][j]];
				if (i >= k) {
					lasth = (*it).first;
					jj = j + 1;
					flag = 1;
					break;
				}
				ans +=(*it).first;
			}
			if (flag == 1) break;
		}
		//ans += maxr * maxr;

		long long lastelem = maxr * maxr;
		lastelem += lasth;

		for (; it != rh2.rend(); ++it) {
			int size = num[(*it).second].size();
			for (int j = jj; j < size; ++j) {
				long long localsum =(*it).first;
				long long rad = R[num[(*it).second][j]];
				if (rad <= maxr) continue;
				rad = rad * rad;

				localsum += rad;

				if (lastelem < localsum) {
					lastelem = localsum;
				}
			}
			jj = 0;
		}
		ans += lastelem;

		long double globalsum = M_PIl;
		globalsum *= (long double)ans;
		printf("Case #%d: %.9Lf\n", t, globalsum);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}