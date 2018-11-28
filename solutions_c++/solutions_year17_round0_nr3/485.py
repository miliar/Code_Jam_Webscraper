#include <iostream> 
#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <map>

using namespace std;

int main() {
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	
	int T;
	fin >> T;
	for (int caseNo = 1; caseNo <= T; caseNo++) {
		long long N, K=0;
		fin >> N >> K;
		
		map<long long, long long> map;
		map.insert(pair<long long, long long>(N, 1));

		long long lastL, lastR;
		while (K != 0) {
			//find greatest element in list
			pair<long long, long long> a = *(--map.end());

			//num split
			long long num_split = min(K, a.second);

			map[a.first] -= num_split;
			if (a.first % 2LL == 1LL) {
				map[(a.first - 1) / 2] += 2 * num_split;
				lastL = (a.first - 1) / 2; lastR = (a.first - 1) / 2;
			}
			else {
				map[a.first / 2] += num_split;
				map[a.first / 2 - 1] += num_split;
				lastL = a.first / 2 -1; lastR = a.first / 2;
			}

			K -= num_split;
			if (map[a.first] == 0)
				map.erase(a.first);

			/*for (auto &a : map)
				cout << a.first << " " << a.second << endl;
			cout << endl;*/
		}

		fout << "Case #" << caseNo << ": " << lastR << " " << lastL << endl;
		cout << "Case #" << caseNo << ": " << lastR << " " << lastL << endl;
	}
}