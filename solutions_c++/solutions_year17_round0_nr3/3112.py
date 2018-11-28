#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

bool leftLengthSort(pair<unsigned long, unsigned long> a, pair<unsigned long, unsigned long> b) {
	return (a.first < b.first);
}

int main() {
	int T;
	unsigned long long N, K, minLength, maxLength, totalLength, middle, personCount, lowerIndex, upperIndex;
	map<unsigned long long , unsigned long long> maps;
	ifstream fin("large.in");
	ofstream fout("large.out");
	fin >> T;
	for (int i = 1; i <= T; i++) {
		maps.clear();
		fin >> N >> K;
		personCount = 0;
		totalLength = N;
		maps[totalLength] = 1L;
		while (1) {
			maxLength = totalLength / 2L;
			minLength = totalLength - maxLength - 1L;
			if (K <= personCount + maps[totalLength]) {
				fout << "Case #" << i << ": " << maxLength << " " << minLength <<endl;
				break;
			}
			else {
				personCount += maps[totalLength];
			}
			//update map
			if (maps.find(maxLength) == maps.end())
				maps[maxLength] = maps[totalLength];
			else
				maps[maxLength] += maps[totalLength];
			if (maps.find(minLength) == maps.end())
				maps[minLength] = maps[totalLength];
			else
				maps[minLength] += maps[totalLength];
			maps.erase(totalLength);
			totalLength = maps.rbegin()->first;
		}
	}
}