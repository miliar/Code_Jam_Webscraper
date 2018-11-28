#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T;
	int count = 1;
	scanf("%d", &T);
	int C, J;
	while( scanf("%d%d", &C, &J) != EOF) {
		vector<int> vC_1(C), vC_2(C);
		vector<int> vJ_1(J), vJ_2(J);
		for (int i = 0; i < C; i++) {
			scanf("%d%d", &vC_1[i], &vC_2[i]);
		}
		for (int i = 0; i < J; i++) {
			scanf("%d%d", &vJ_1[i], &vJ_2[i]);
		}
		int min_d = 0;
		if (vC_1.size() == 0 && vJ_2.size() == 2) {
			sort(vJ_1.begin(), vJ_1.end());
			sort(vJ_2.begin(), vJ_2.end());
			if (vJ_2[1] - vJ_1[0] <= 720 || 1440 - (vJ_1[1] - vJ_2[0]) <= 720) {
				min_d = 2;
			}
			else {
				min_d = 4;
			}
		}
		else if (vJ_1.size() == 0 && vC_2.size() == 2) {
			sort(vC_1.begin(), vC_1.end());
			sort(vC_2.begin(), vC_2.end());
			if (vC_2[1] - vC_1[0] <= 720 || 1440 - (vC_1[1] - vC_2[0]) <= 720) {
				min_d = 2;
			}
			else {
				min_d = 4;
			}
		}
		else {
			min_d = 2;
		}
		printf("Case #%d: %d\n", count++, min_d);
	}
}