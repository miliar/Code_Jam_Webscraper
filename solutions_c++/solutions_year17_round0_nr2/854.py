#include "cmath"
#include "cstdio"
#include <iostream>
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

bool tidy(string& N)
{
	if (N.size() == 1) return true;
	
	for (size_t i = 0; i < N.size() - 1; ++i) {
		if (N[i] > N[i+1]) {
			N[i]--;
			for (size_t j = i + 1; j < N.size(); ++j) {
				N[j] = '9';
			}
			if (i == 0 && N[i] == '0') {
				N.erase(N.begin());
			}
			return false;
		}
	}
	return true;
}

int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		string N;
		cin >> N;

		while (!tidy(N)) {}

		printf("Case #%d: %s\n", Ti, N.c_str());
	}
	return 0;
}
