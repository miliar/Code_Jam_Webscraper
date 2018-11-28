#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int index = 0;

void fill(unsigned long long Nseq[]) {
	for (unsigned long long i = 0; Nseq[i] != 0; i++) {
		if (Nseq[i] % 2 == 0) {
			Nseq[index++] = Nseq[i] / 2;
			Nseq[index++] = Nseq[i] / 2 - 1;
		} else {
			Nseq[index++] = Nseq[i] / 2;
			Nseq[index++] = Nseq[i] / 2;
		}

	}
}

unsigned long long getES(unsigned long long k, unsigned long long N) {
	if (k == 0)
		return N;

	unsigned long long val;
	if (k % 2 == 0) {
		val = getES(k / 2 - 1, N);
		if (val == 0)
			return 0;
		if (val % 2 == 0)
			return val / 2 - 1;
		else
			return val / 2;
	} else {
		val = getES(k / 2, N);
		if (val == 0)
			return 0;
		return val / 2;
	}
}

unsigned long long max(unsigned long long val) {
	return val / 2;
}

unsigned long long min(unsigned long long val) {
	if (val % 2 == 0)
		return val / 2 - 1;
	else
		return val / 2;
}

struct MM {
	unsigned long long count;
	unsigned long long MAX;
	unsigned long long MIN;
};

bool mf(MM A, MM B) {
	if (A.MIN == B.MIN) {
		return A.MAX > B.MAX;
	}
	return A.MIN > B.MIN;
}

int main() {
	unsigned long long T;
	cin >> T;
	for (unsigned long long t = 0; t < T; t++) {
		unsigned long long N, K, MAX = 0, MIN = 0, size = 0;
		cin >> N;
		cin >> K;
		//memset(Nseq, 0, sizeof(Nseq));
		/*unsigned long long val;
		 if (K > N / 2)
		 val = getES(K - 1, N);
		 else
		 val = 1;*/
		MM M[10000] = { 0 };

		for (unsigned long long k = 1; k <= N; k++) {
			MAX = getES(k * 2 - 1, N);
			MIN = getES(k * 2, N);
			unsigned long long i;
			for (i = 0; i < size; i++) {
				if (M[i].MAX == MAX && M[i].MIN == MIN) {
					M[i].count++;
					break;
				}
			}
			if (i == size) {
				M[size].MAX = MAX;
				M[size].count = 1;
				M[size++].MIN = MIN;
			}
		}

		sort(M, M + size, mf);
		//stable_sort(M, M + N + 1, mmf);
		unsigned long long i;
		for (i = 0; i < size; i++) {
			if (K > M[i].count){
				K -= M[i].count;
				continue;
			}
			else
				break;
		}

		cout << "Case #" << t + 1 << ": " << M[i].MAX << " " << M[i].MIN
				<< endl;


	}
}
