#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <deque>
#include <queue>
#include <functional>
#include <string>
#define FLIP(a){(a=='+')? '-':'+'}

using namespace std;

unsigned long long int power_10(int n) {
	unsigned long long int result=1;
	while (n--) {
		result *= 10;
	}
	return result;
}

int main(int argc, char** argv) {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	setbuf(stdout, NULL);

	int T;
	int test_case;
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case) {
		unsigned long long int N, answer = 0;
		deque<int, vector<int>> v, ans;
		
		scanf("%llu", &N);
		
		while (N > 0) {
			v.push_front(N % 10);
			N /= 10;
		}
		ans.resize(v.size());

		bool unlimited = false;
		bool backtrack = false;
		for (int i = 0; i < v.size(); ) {

			//first digit from left
			if (i == 0) {
				//if normal track
				if (!backtrack) {
					//max out first
					ans[i] = v[i];
				}
				//first digit doesn't need to ensure if it can be decreased
				else {
					//--v[i];
					--ans[i];
					unlimited = true;
					backtrack = false;
				}
			}
			//not first digit(most cases)
			else {
				if (!backtrack) {
					if (unlimited) {
						ans[i] = 9;
					}
					else {
						if (ans[i - 1] <= v[i]) {
							ans[i] = v[i];
						}
						//v[i] can't top the digit before
						else {
							backtrack = true;
							--i;
							continue;
						}
					}
				}
				//backtracking
				else {
					//if it can't be decreased
					if (ans[i - 1] > ans[i] - 1) {
						--i;
						continue;
					}
					else {
						--ans[i];
						unlimited = true;
						backtrack = false;
					}
				}
			}

			++i;
		}

		for (int i = 0; i < v.size(); ++i) {
			answer += ans[i] * power_10(v.size() - 1 - i);
		}

		printf("Case #%d: ", test_case);
		printf("%llu\n", answer);
	}

	return 0;	
}

