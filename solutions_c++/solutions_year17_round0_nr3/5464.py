#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <deque>
#include <queue>
#include <functional>
#include <string>


using namespace std;


int main(int argc, char** argv) {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	setbuf(stdout, NULL);

	int T;
	int test_case;
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case) {
		int N, K;
		//N : stalls, K : people
		scanf("%d %d", &N, &K);

		vector<int> v;
		v.push_back(N);

		for (int i = 0; i < K; ++i) {
			//find max in v
			int max = 0;
			int maxp = 0;
			for (int j = 0; j < v.size(); ++j) {
				if (max < v[j]) {
					max = v[j];
					maxp = j;
				}
			}
			v.erase(v.begin() + maxp);
			v.push_back((max-1) / 2);
			v.push_back((max-1) - ((max - 1) / 2));
		}

		


		printf("Case #%d: ", test_case);
		printf("%d %d\n", *(v.end() - 1), *(v.end() - 2));;
	}

	return 0;	
}

