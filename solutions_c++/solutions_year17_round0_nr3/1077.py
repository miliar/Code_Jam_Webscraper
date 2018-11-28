//============================================================================
// Name        : C_Stall.cpp
// Author      : Oliver Roese
//============================================================================
// Name        : B_tidy.cpp
// Author      : Oliver Roese
//============================================================================

#include <iostream>
#include <algorithm>
#include <cstdint>
#include <array>
#include <cassert>

using namespace std;

struct space_count {
	uint64_t space;
	uint64_t count;
};
bool operator<(const space_count& l, const space_count& r) {return l.space < r.space;}

class Heap {
public:
	void reset() {free_forms = 0;}
	void insert(uint64_t space, uint64_t count) {
		assert(free_forms + 1 < N);
		const space_count s{space, count};
		space_count* elem = lower_bound(toilet.begin(), toilet.begin()+free_forms, s);
		if (elem - toilet.begin() == free_forms || elem->space != space) {
			toilet[free_forms++] = s;
			sort(toilet.begin(), toilet.begin()+free_forms);
		} else {
			elem->count += count;
		}
	}
	space_count popMax() {
		assert(free_forms > 0);
		return toilet[--free_forms];
	}
private:
	static const unsigned N = 512;
	array<space_count, N> toilet;
	unsigned free_forms;
};

void printLastSpacing(unsigned i, uint64_t N, uint64_t K) {
	assert(1<=K && K <= N && N <= 1000000000000000000);

	Heap h;
	h.reset();
	h.insert(N, 1);
	uint64_t remK = K;
	for(;;) {
		const space_count s = h.popMax();
		if (s.count < remK) {
			remK -= s.count;
			if (s.space % 2 != 0) {
				h.insert(s.space/2, s.count*2);
			} else {
				h.insert(s.space/2, s.count);
				h.insert(s.space/2-1, s.count);
			}
		} else {
			const uint64_t maxS = s.space/2;
			const uint64_t minS = s.space - maxS - 1;
			cout << "Case #" << i << ": " << maxS << " " << minS << "\n";
			break;
		}
	}
}

void processStalls() {
	unsigned T = 0;
	cin >> T;
	assert(1<=T && T<=100);
	for (unsigned i = 1; i <= T; ++i) {
		uint64_t N;
		uint64_t K;
		cin >> N >> K;
		printLastSpacing(i,N,K);
	}
}

int main() {
	processStalls();

	return 0;
}
