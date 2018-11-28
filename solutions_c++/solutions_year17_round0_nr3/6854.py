#include <iostream>
#include <algorithm>
#include <string>
#include <unordered_map>

using namespace std;

void process(int count, int people) {
//	cerr << "count=" << count << " people=" << people << endl;
	bool rooms[count+2];
	rooms[0] = true;
	rooms[count+1] = true;
	for(int i = 1; i <=count; ++i) rooms[i] = false;
	int minmax, maxmax;
	for (int p = 0; p < people; ++p) {
		minmax = 0;
		maxmax = 0;
		using Status = pair<int,int>; // L,R
		using Candidates = unordered_map<int, Status>;
		Candidates candidates;
		for (int i = 1; i <= count; ++i) {
			if (!rooms[i]) {
//cerr << "room #" << i << " free" << endl;
				int l = 0, r =0;
				auto j = i;
				do {
					--j;
					if (rooms[j]) {
						l = i-j-1;
//cerr << "room L #" << j << "@" << l << endl;
						break;
					}
				} while (j >= 0);
				j = i;
				do {
					++j;
					if (rooms[j]) {
						r = j-i-1;
//cerr << "room R #" << j << "@" << r << endl;
						break;
					}
				} while (j < count+2);
				auto m = min(l,r);
				if (m > minmax) {
					candidates.clear();
					minmax = m;
				} else if (m < minmax) {
					continue;
				}
				candidates[i] = {l,r};
			}
		}
		for(auto it = candidates.begin(); it != candidates.end(); ) {
			auto m = min(it->second.first, it->second.second);
			if (m == minmax) {
//cerr << "minmax=" << minmax << " room= "<< it->first << endl;
				m = max(it->second.first, it->second.second);
				if (m > maxmax) {
					maxmax = m;
				}
				++it;
			} else {
//cerr << " discard min room #" << it->first << endl;
				it = candidates.erase(it);
			}
		}
		int r = count;
		for (auto c: candidates) {
			auto m = max(c.second.first, c.second.second);
			if (m == maxmax && c.first<r) {
//cerr << "maxmax=" << maxmax << " room=" << c.first << endl;
				r = c.first;
			} else {
//cerr << " discard max room #" << c.first << endl;
			}
		}
		//minmax = candidates[r].second;
		//maxmax = candidates[r].first;
		rooms[r] = true;
//		cerr << "people #" << p+1 << " takes room #" << r << " max=" << maxmax << " min=" << minmax << endl;
	}
	cout << maxmax << ' ' << minmax << endl;
}

int main(int argc, char** argv) {
	size_t inputCount;
	cin >> inputCount;
	for (size_t inputNumber = 1; inputNumber <= inputCount; ++inputNumber) {
		int count, people;
		cin >> count >> people;
		cout << "Case #" << inputNumber << ": ";
		process(count, people);
	}
	return 0;
}
