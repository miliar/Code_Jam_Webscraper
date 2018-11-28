#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>
#include <unordered_map>
#include <limits.h>
#include <assert.h>
#include <string.h>
#include <Util.h>

using namespace std;

bool debug = false;

int Hd, Ad, Hk, Ak, B, D;

int solveBD2(int bCount, int dCount) {
	int thisHd = Hd;
	int thisAd = Ad;
	int thisHk = Hk;
	int thisAk = Ak;
	int step = 0;

	// fixme;

if (debug) cout << "solveBD2()" << endl;
	if (debug) cout << "bCount = " << bCount << endl;
	if (debug) cout << "dCount = " << dCount << endl;

	int lastHd = -1;
	int lastAd = -1;
	int lastHk = -1;
	int lastAk = -1;
	int lastB = -1;
	int lastD = -1;
	while (true) {

		if (thisHd == lastHd &&
			thisAd == lastAd &&
			thisHk == lastHk &&
			thisAk == lastAk &&
			bCount == lastB &&
			dCount == lastD) return -1;  // recurse;

		lastHd = thisHd;
		lastAd = thisAd;
		lastHk = thisHk;
		lastAk = thisAk;
		lastB = bCount;
		lastD = dCount;

		if (debug) cout << thisHd << " " << thisAd << " | " << thisHk << " " << thisAk << " " << " | " << B << ", " << D << endl; 

		step++;
		if (thisHk <= thisAd) {
			thisHk -= thisAd;
			if (debug) cout << "ATTACK ..." << endl;
		} else if (thisHd <= thisAk) {
			if (dCount > 0 && thisHd > thisAk - D) {
				thisAk -= D;
				if (thisAk < 0) thisAk = 0;
			if (debug) cout << "DEBUFF ..." << endl;
				dCount--;
				goto END;  // Debuff;
			} else {
				thisHd = Hd;
			if (debug) cout << "CURE..." << endl;
				goto END;  // cure;
			}
		} else if (dCount > 0) {
			thisAk -= D;
			if (thisAk < 0) thisAk = 0;
			if (debug) cout << "DEBUFF ..." << endl;
			dCount--;
			goto END;  // Debuff;
		} else if (bCount > 0) {
			thisAd += B;
			if (debug) cout << "BUFF ..." << endl;
			bCount--;
			goto END;  // Buff;
		} else {
			thisHk -= thisAd;
			if (debug) cout << "ATTACK ..." << endl;
			goto END;
		}

END:
		if (thisHk <= 0) return step;
		thisHd -= thisAk;
		if (thisHd <= 0) return -1;  // failed;
	}
}

int solveBD(int CASE) {
	int best = -1;
	int maxBCount = B == 0 ? 0 : ((Hk + B - 1) / B);
	int maxDCount = D == 0 ? 0 : ((Ak + D - 1) / D);
	for (int bCount = 0; bCount <= maxBCount; bCount++) {
		for (int dCount = 0; dCount <= maxDCount; dCount++) {
			int answer = solveBD2(bCount, dCount);
			if (answer == -1) continue;
			if (best == -1 || answer < best)
				best = answer;
		}
	}
	return best;
}

void solve(int CASE) {
	int best = solveBD(CASE);
	if (best == -1) {
		cout << "Case #" << CASE << ": " << "IMPOSSIBLE" << endl;
	} else {
		cout << "Case #" << CASE << ": " << best << endl;
	}
}

int main(int argc, const char * argv[]) {

	istream &fin = cin;
	// fstream fin("tiny.in");

	int T;
	fin >> T;
	for (int CASE = 1; CASE <= T; CASE++) {
		fin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		solve(CASE);
	}
    return 0;
}
