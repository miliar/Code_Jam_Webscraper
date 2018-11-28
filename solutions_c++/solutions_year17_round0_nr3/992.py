#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main() {
	int numCases;
	ifstream fin("C-large.in");
	ofstream fout("C.out");
	fin >> numCases;
	for (int cases = 1; cases <= numCases; cases++) {
		long long n,k;
		fin >> n >> k;
		map<long long, long long> rooms;
		long long min;
		long long max;
		rooms[n] = 1;
		while (k > 0) {
			long long length = rooms.rbegin()->first;
			long long num = rooms.rbegin()->second;
			k -= num;
			min = (length - 1) / 2;
			max = length - 1 - min;
			rooms.erase(length);
			if (rooms.find(min) == rooms.end()) {
				rooms[min] = 0;
			}
			if (rooms.find(max) == rooms.end()) {
				rooms[max] = 0;
			}
			rooms[min] += num;
			rooms[max] += num;
		}
		cout << "Case #" << cases << ": " << max << " " << min << '\n';
		fout << "Case #" << cases << ": " << max << " " << min << '\n';
	}
	fin.close();
	fout.close();
	return 0;
}
