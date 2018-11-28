#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>

#define D(x) x

using namespace std;

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& vec) {
	os << "[";
	for (int i = 0; i < vec.size(); i++) {
		if (i > 0) os << ", ";
		os << vec[i];
	}
	os << "]";
	return os;
}

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
        string S;
        int K;
        cin >> S >> K;
        int N = S.length();

        vector<bool> needsFlip(N), unflip(N);
        for (int i = 0; i < N; i++) {
            needsFlip[i] = (S[i] == '-');
        }

        int totalFlips = 0;
        bool flipped = false;

        for (int i = 0; i + K - 1 < N; i++) {
            if (needsFlip[i] != flipped) {
                totalFlips++;
                flipped = !flipped;
                unflip[i + K - 1] = true;
            }
            if (unflip[i]) {
                flipped = !flipped;
            }
        }

        bool failed = false;
        for (int i = N - K + 1; i < N; i++) {
            if (needsFlip[i] != flipped) {
                failed = true;
                break;
            }
            if (unflip[i]) {
                flipped = !flipped;
            }
        }

        cout << "Case #" << testCase << ": ";
        if (failed) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << totalFlips << endl;
        }
    }
}
