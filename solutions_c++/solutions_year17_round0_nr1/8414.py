#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <list>
#include <set>
#include <map>

using namespace std;

int main(int argc, char *argv) {
	FILE *input = fopen("input.txt", "r");
	FILE *output = fopen("output.txt", "w");

	int T;
	fscanf(input, "%d", &T);
	for (int t = 0; t < T; t++) {
		vector<char> S(1001, 0);
		for (int i = 0; i < 1000; i++) {
			fscanf(input, "%c", &S[i]);
			if (S[i] == '\n') {
				i -= 1;
			}
			else if (S[i] == ' ') {
				S.resize(i);
				break;
			}
		}

		int K;
		fscanf(input, "%d", &K);
		
		list<int> A;
		int count = 0;
		int is_possible = 1;
		for (int i = 0; i < S.size(); i++) {
			if (!A.empty() && A.front() <= i - K) {
				A.pop_front();
			}
			if ((S[i] == '+') ^ (A.size() % 2 == 0)) {
				if (i <= S.size() - K) {
					A.push_back(i);
					count += 1;
				}
				else {
					is_possible = 0;
					break;
				}
			}
		}
		if (is_possible) {
			fprintf(output, "Case #%d: %d\n", t+1, count);
		}
		else {
			fprintf(output, "Case #%d: IMPOSSIBLE\n", t + 1);
		}
	}
}