#include <iostream>
#include <deque>
using namespace std;

void process(__int64& maxLR, __int64& minLR, __int64 N, __int64 K) {
	if (N == K) {
		maxLR = minLR = 0;
		return;
	}
	if (K == 1) {
		if (N % 2 == 0) {
			maxLR = N / 2;
			minLR = maxLR - 1;
		} else {
			maxLR = minLR = N / 2;
		}
		return;
	}
	/// 5 2   o.....o| o..o..o| oo.o..o| oo.oo.o
	/// 6 2   o......o, o..o...o, o..o.o.o, oo.o.o.o, oooo.o.o, oooooo.o, oooooooo
	/// 17 3  o.................o| o........o........o| o...o....o...o....o| o.o.o.o..o.o.o.o..o|
	/// 44 3  o............................................o 44
	///		  o.....................o......................o first time divide 2: 21 22
	///		  o..........o..........o..........o...........o 2nd time divide 2: 10 11
	///		  o....o.....o....o.....o....o.....o.....o.....o 3rd time divide 2: 4 5
	///		  o.o..o..o..o.o..o..o..o.o..o..o..o..o..o..o..o 4th time divide 2: 1 2
	__int64 peopleOfXthDivide = 1, remainingPeopleCount = K, maxEmptySequenceLen = N;
	__int64 shorterEmptySequenceCount = 0, shorterEmptySequenceLen = -1;
	__int64 longerEmptySequenceCount = 1, longerEmptySequenceLen = N;
	while (peopleOfXthDivide < remainingPeopleCount) {
		maxEmptySequenceLen /= 2;
		remainingPeopleCount -= peopleOfXthDivide;
		//
		__int64 shorterCount = 0, longerCount = 0;
		if (longerEmptySequenceLen % 2 == 0) {
			shorterCount += longerEmptySequenceCount;
			longerCount += longerEmptySequenceCount;
		} else {
			longerCount += longerEmptySequenceCount;
			longerCount += longerEmptySequenceCount;
		}
		//
		if (shorterEmptySequenceLen % 2 == 0) {
			shorterCount += shorterEmptySequenceCount;
			longerCount += shorterEmptySequenceCount;
		} else {
			shorterCount += shorterEmptySequenceCount;
			shorterCount += shorterEmptySequenceCount;
		}
		//
		longerEmptySequenceCount = longerCount;
		shorterEmptySequenceCount = shorterCount;
		longerEmptySequenceLen = maxEmptySequenceLen;
		shorterEmptySequenceLen = maxEmptySequenceLen - 1;
		//
		peopleOfXthDivide <<= 1;
	}
	//
	__int64 emptySequenceLenOfLastPerson = longerEmptySequenceCount >= remainingPeopleCount
		? longerEmptySequenceLen : shorterEmptySequenceLen;
	if (emptySequenceLenOfLastPerson % 2 == 0) {
		maxLR = emptySequenceLenOfLastPerson / 2;
		minLR = maxLR - 1;
	} else {
		maxLR = minLR =  emptySequenceLenOfLastPerson / 2;
	}
}

int main() {
	//data
	int T;
	__int64 N, K;
	
	//input
	cin >> T;

	for (int i = 0; i < T; ++i) {
		// input
		cin >> N >> K;

		//process
		__int64 maxLR, minLR;
		process(maxLR, minLR, N, K);

		//output
		cout << "Case #" << (i + 1) << ": " << maxLR << " " << minLR;
		if (i + 1 < T) cout << endl;
	}

	return 0;
}