#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<char> vt, int K)
{
	int ret = 0;
	for (int i = 0; i < vt.size() - K + 1; i++) {
		if (vt[i] == '-') {
			ret++;
			for (int m = 0; m < K; m++) {
				if (vt[i + m] == '-')
					vt[i + m] = '+';
				else
					vt[i + m] = '-';
			}
		}
	}

	for (int i = 0; i < vt.size(); i++) {
		if (vt[i] == '-')
			return -1;
	}
	return ret;
}

int main()
{
	//FILE *fp = fopen("test_input.txt", "r");

	int T;
	scanf("%d", &T);
	//fscanf(fp, "%d", &T);
	for (int w = 0; w < T; w++) {
		char S[1002];
		int K;

		scanf("%s %d", S, &K);
		//fscanf(fp, "%s %d", S, &K);

		vector<char> vt;
		for (int i = 0; i < strlen(S); i++) {
			vt.push_back(S[i]);
		}

		int ret = solve(vt, K);
		std::reverse(vt.begin(), vt.end());
		int ret2 = solve(vt, K);

		if (ret < 0 && ret2 < 0)
			printf("Case #%d: IMPOSSIBLE\n", w+1);
		else if (ret < ret2)
			printf("Case #%d: %d\n", w+1, ret);
		else
			printf("Case #%d: %d\n", w + 1, ret2);
	}

	return 0;
}