#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
	ifstream fin("C-small-2-attempt0.in");
	ofstream fout("output.txt");

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++) {
		int n, k;
		fin >> n >> k;
		priority_queue<int> q;
		q.push(n);
		int lower = 0;
		int higher = 0;
		for (int i = 0; i < k; i++) {
			int v = q.top();
			q.pop();
			lower = (v - 1) / 2;
			higher = (v - 1) - lower;
			q.push(lower);
			q.push(higher);
		}
	
		fout << "Case #" << to_string(t) << ": " << to_string(higher) << " " << to_string(lower) << endl;
	}
}