#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <math.h>

struct Data {
	int u;
	int v;
	int w;
};

struct cmp {
	bool operator()(const Data&a, const Data &b) {
		return a.w < b.w;
	}
};

#define pll pair<long long, long long>
#define pii pair<int, int>
#define pil pair<int, long>
#define MAX 4
using namespace std;

int T, N, P;
int Count[MAX];

int main() {
	int num;
	int ret;
	ifstream in("A-small-attempt0.in");
	ofstream out("output.txt");

	in >> T;

	for (int tt = 0; tt < T; ++tt) {
		out << "Case #" << tt + 1 << ": ";
		for (int i = 0; i < MAX; ++i) Count[i] = 0;
		
		in >> N >> P;
		for (int i = 0; i < N; ++i) {
			in >> num;
			Count[num%P]++;
		}

		if (P == 2) {
			ret = Count[0] + (Count[1] + 1) / 2;
		}

		else if (P == 3) {
			ret = Count[0];
			int Min;
			Min = min(Count[1], Count[2]);
			
			ret += Min;
			Count[1] -= Min;
			Count[2] -= Min;

			if (Count[1] > 0) ret += (Count[1] + 2) / 3;
			if (Count[2] > 0) ret += (Count[2] + 2) / 3;
		}

		else if (P == 4) {
			ret = Count[0];
			ret += Count[2] / 2;
			Count[2] /= 2;

			int Min;
			Min = min(Count[1], Count[3]);
			ret += Min;
			Count[1] -= Min;
			Count[3] -= Min;

			if (Count[1] > 0) {
				ret += (Count[1] + 3) / 4;
				Count[1] %= 4;
				if (Count[2] > 0 && (Count[1] == 3 || Count[1] == 0)) ret += 1;
			}

			if (Count[3] > 0) {
				ret += (Count[3] + 3) / 4;
				Count[3] %= 4;
				if (Count[2] > 0 && (Count[3] == 3 || Count[3] == 0)) ret += 1;
			}
		}

		out << ret << endl;
	}


	in.close();
	out.close();
}
