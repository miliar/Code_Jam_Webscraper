#include <iostream>
#include <stdint.h>
using namespace std;

typedef pair<uint64_t, uint64_t> LRDist;

LRDist dist(uint64_t iRegion, uint64_t iPerson);

int main(int argc, char** argv) {
	int iRounds = 0;
	cin >> iRounds;
	for (int i = 0; i < iRounds; i++) {
		LRDist dResult(0,0);
		uint64_t iRegionSize = 0;
		uint64_t iPersonId = 0;
		cin >> iRegionSize >> iPersonId;
		dResult = dist(iRegionSize, iPersonId);
		// output
		cout << "Case #" << i+1 << ": ";
		cout << dResult.first << " " << dResult.second << endl;;
	}
	return 0;
}

LRDist dist(uint64_t iRegion, uint64_t iPerson) {
	// take one stall off first
	iRegion--;
	iPerson--;
	if (iPerson == 0) {
		return make_pair(iRegion / 2 + iRegion % 2, iRegion / 2);
	} else if (iPerson % 2 == 1) {
		return dist(iRegion / 2 + iRegion % 2, iPerson / 2 + 1);
	} else {
		return dist(iRegion / 2, iPerson / 2);
	}
}
