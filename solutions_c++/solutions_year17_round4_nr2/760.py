// q2.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <cstdint>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

size_t sum(vector<size_t>& vec) {
	size_t res = 0;
	for (size_t i : vec) {
		res += i;
	}
	return res;
}

pair<size_t, size_t> solve(size_t N, size_t C, size_t M, vector<vector<size_t>>& tickets) {
	size_t t0 = sum(tickets[0]);
	size_t t1 = sum(tickets[1]);
	size_t b = t0 > t1 ? 0 : 1;
	size_t trains = t0 > t1 ? t0 : t1;

	trains = max(trains, tickets[b][0] + tickets[1 - b][0]);

	size_t promotions = 0;
	for (size_t i = 0; i < N; i++) {
		if (tickets[0][i] + tickets[1][i] > trains) {
			promotions += (tickets[0][i] + tickets[1][i]) - trains;
		}
	}

	return pair<size_t, size_t>(trains, promotions);
}

int main()
{
	ifstream inFile;
	inFile.open("..\\..\\B-small-attempt0.in");
	ofstream outFile;
	outFile.open("..\\..\\B-small-attempt0.out");

	size_t T;
	inFile >> T;
	for (size_t i = 0; i < T; i++) {
		size_t N;
		size_t C;
		size_t M;
		inFile >> N;
		inFile >> C;
		inFile >> M;

		size_t P;
		size_t B;
		vector<vector<size_t>> tickets(2, vector<size_t>(N, 0));
		vector<size_t> second(N);
		for (size_t j = 0; j < M; j++) {
			inFile >> P;
			inFile >> B;
			tickets[B - 1][P - 1]++;
		}

		pair<size_t, size_t> res = solve(N, C, M, tickets);
		outFile << "Case #" << (i + 1) << ": " << res.first << " " << res.second << endl;
	}

	outFile.close();
	inFile.close();
	return 0;
}