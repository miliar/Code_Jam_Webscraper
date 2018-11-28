#include <algorithm>
#include <iostream>
#include <string>

using namespace std;	//Yeah, yeah, it's just a competition. I'm gonna stick this here.

//bool* MakePancake(string s, bool& hasSad, bool& hasHappy) {
//	hasSad = false;
//	hasHappy = false;
//
//	bool* pancake = new bool[s.size()];
//	for (int i = 0; i < s.size(); i++) {
//		if (s[i] == '+') {
//			pancake[i] = true;
//			hasHappy = true;
//		}
//		else {
//			pancake[i] = false;
//			hasSad = true;
//		}
//	}
//
//	return pancake;
//}

int MakePancake(string s, bool& hasSad, bool& hasHappy) {
	hasSad = false;

	int pancake = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '+')
			pancake |= (1 << i);
		else
			hasSad = true;
	}

	hasHappy = (pancake != 0);
	return pancake;
}

void DoFlips(int pancake, int flipper, int cakes, int width, int depth, bool* seen, int* minSeen) {
	
	for (int i = 0; i <= cakes - width; i++) {
		int movedFlipper = flipper << i;
		
		int flipped = pancake ^ movedFlipper;
		if (flipped == (1 << cakes) - 1) {
			seen[flipped] = true;
			minSeen[flipped] = min(minSeen[flipped], depth);
			return;
		}

		if (!seen[flipped] || depth < minSeen[flipped]) {
			seen[flipped] = true;
			minSeen[flipped] = depth;
			DoFlips(flipped, flipper, cakes, width, depth + 1, seen, minSeen);
		}
	}
}

int main()
{
	int testCount;
	cin >> testCount;

	for (int i = 0; i < testCount; i++) {
		string s;
		cin >> s;

		int k;
		cin >> k;

		bool hasSad, hasHappy;
		//bool* pancake = MakePancake(s, hasSad, hasHappy);
		int pancake = MakePancake(s, hasSad, hasHappy);

		if (!hasSad) {
			cout << "Case #" << i + 1 << ": 0" << endl;
			continue;
		}
		else if (!hasHappy && k == s.size()) {
			cout << "Case #" << i + 1 << ": 1" << endl;
			continue;
		}

		int flipper = 0;
		for (int i = 0; i < k; i++) {
			flipper |= (1 << i);
		}

		//Only gonna work for small case... need less suckage for big case.
		bool* seen = new bool[1024];
		int* minSeen = new int[1024];
		for (int i = 0; i < 1024; i++) {
			seen[i] = false;
			minSeen[i] = 1000000000;
		}
		seen[pancake] = true;
		minSeen[pancake] = 0;

		DoFlips(pancake, flipper, s.size(), k, 1, seen, minSeen);

		if (!seen[(1 << s.size()) - 1])
			cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i + 1 << ": " << minSeen[(1 << s.size()) - 1] << endl;
		//delete[] pancake;
	}

    return 0;
}

