// q1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <cstdint>
#include <vector>
#include <fstream>
#include <algorithm>
#include <queue>

using namespace std;

pair<int64_t, int64_t> solve2(int64_t N, int64_t K) {
	int64_t jmp = K;
	for (size_t j = 0; j < 8; j++) {
		jmp |= jmp >> (1 << j);
	}
	jmp++;

	int64_t mx_init = K + jmp / 2 - jmp;
	int64_t mx = ((N - mx_init) / jmp);

	int64_t mn_init = K;
	int64_t mn = ((N - mn_init) / jmp);
	
	//uint64_t mx = N / (1 << (K - 1));
	//uint64_t mn = 0;
	//if (N >= (1 << (K - 2))) {
	//	mn = (N - (1 << (K - 2))) / (1 << (K - 1));
	//}

	return pair<int64_t, int64_t>(mx, mn);
}

pair<uint64_t, uint64_t> solve(uint64_t N, uint64_t K) {
	priority_queue<uint64_t> empty_sequences;
	empty_sequences.push(N);

	uint64_t r = 0, l = 0;
	while (K-- > 0) {
		uint64_t m = empty_sequences.top();
		empty_sequences.pop();
		l = m / 2;
		r = (m - 1) / 2;
		if (l != 0)
			empty_sequences.push(l);
		if (r != 0)
			empty_sequences.push(r);
	}

	return pair<uint64_t, uint64_t>(max(r, l), min(r, l));
}

int main()
{
	//string fileName = "example";
	string fileName = "C-large";
	//string fileName = "C-small-2-attempt1";

	ifstream inFile;
	inFile.open("..\\..\\" + fileName + ".in");
	ofstream outFile;
	outFile.open("..\\..\\" + fileName + ".out");

	size_t T;
	inFile >> T;
	for (size_t i = 0; i < T; i++) {
		uint64_t N;
		uint64_t K;
		inFile >> N;
		inFile >> K;

		cout << i << " " << N << " " << K << endl;
		pair<uint64_t, uint64_t> res = solve2(N, K);
		outFile << "Case #" << (i + 1) << ": " << res.first << " " << res.second << endl;
	}

	outFile.close();
	inFile.close();
	return 0;
}

