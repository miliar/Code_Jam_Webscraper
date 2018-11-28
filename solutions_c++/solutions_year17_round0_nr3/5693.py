// bathroom-stalls.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

struct StallDivision {
	StallDivision(long long _start, long long _end) : start(_start), end(_end) {
		size = end - start + 1;
	}
	StallDivision() : start(0), end(0) {
		size = 0;
	}
	void print() const { cout << "start[" << start << "], end[" << end << "]: size = " << size << endl; }
	long long size;
	long long start, end;
};

struct Compare {
	bool operator() (const StallDivision& a, const StallDivision& b) const {
		return (a.size < b.size) || ((a.size == b.size) && (a.start > b.start));
	}
};

pair<long long, long long> bathroomStalls(long long N, long long K) {
	priority_queue<StallDivision, vector<StallDivision>, Compare > queue;
	queue.push(StallDivision(1, N));
	StallDivision top;
	long long stallPicked;
	for (long long i = 1; i <= K; ++i) {
		top = queue.top();
		queue.pop();

		stallPicked = (top.size % 2 == 0) ? (top.start + (top.size / 2) - 1) : top.start + (top.size / 2);
		if (stallPicked - 1 >= top.start) {
			StallDivision remaningStallLeft(top.start, stallPicked - 1);
			queue.push(remaningStallLeft);
		}
		if (stallPicked + 1 <= top.end) {
			StallDivision remaningStallRight(stallPicked + 1, top.end);
			queue.push(remaningStallRight);
		}
	}
	return make_pair(max(stallPicked - top.start, top.end - stallPicked), min(stallPicked - top.start, top.end - stallPicked));
}

int main()
{
	ifstream inputFile("C:/Users/jnambiar/Documents/main/code-jam/bathroom-stalls/input.txt");
	ofstream outputFile("C:/Users/jnambiar/Documents/main/code-jam/bathroom-stalls/output.txt");

	int testCases = 0;
	inputFile >> testCases;
	inputFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for (int i = 0; i < testCases; i++) {
		long long N, K;
		inputFile >> N >> K;
		pair<long long, long long> finalStall = bathroomStalls(N, K);
		outputFile << "Case #" << i + 1 << ": " << finalStall.first << " " << finalStall.second << endl;
	}

	inputFile.close();
	outputFile.close();
	return 0;
}

