#define _CRT_SECURE_NO_WARNINGS
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

#define MEMSET(x, WITH) memset(x, (WITH), sizeof(x))
#define FOR(i, E) for (int i=0; i<(E); i++)
typedef long long ll;
//const ll MOD = 1000000007;
//const double PI = atan(1) * 4;



int N, C, M;

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TC; scanf("%d", &TC);
	for (int tc=1; tc<=TC; tc++) {
		printf("Case #%d: ", tc);
		cin >> N >> C >> M;
		//printf("\t %d %d %d\n", N, C, M);
		if (C != 2) {
			assert(false);
			puts("NO");
			continue;
		}

		
		vector<int> ap;
		vector<int> bp;
		FOR(i, M) {
			int p, b; cin >> p >> b;
			if (b == 1) 
				ap.push_back(p);
			else 
				bp.push_back(p);
		}

		sort(ap.begin(), ap.end());
		sort(bp.begin(), bp.end());

		int a1 = count(ap.begin(), ap.end(), 1);
		int a11 = ap.size() - a1;
		vector<int> a2(ap.begin() + a1, ap.end());


		int b1 = count(bp.begin(), bp.end(), 1);
		int b11 = bp.size() - b1;
		vector<int> b2(bp.begin() + b1, bp.end());



		int rollers = (a1 + b1) + max({ 0, b11 - a1, a11 - b1 });

		int cost;
		if (b11 <= a1 && a11 <= b1)
			cost = 0;
		else if (b11 <= a1)
			cost = 0;
		else if (a11 <= b1)
			cost = 0;
		else {
			int bbb = b11 - a1;
			int aaa = a11 - b1;

			int choose = min(aaa, bbb);
			for (int a : a2) {
				for (int i=0; i<b2.size(); i++) if (a != b2[i]) {
					b2.erase(b2.begin() + i);
					choose--;
					break;
				}

				if (choose == 0) break;
			}

			cost = choose;

		}


		cout << rollers << " " << cost << endl;


	}





	return 0;
}
