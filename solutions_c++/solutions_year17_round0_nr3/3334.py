// Google Code Jam.cpp : Defines the entry point for the console application.
//
#include <algorithm>
#include <iostream>
#include <set>
#include <map>

using namespace std;	//Yeah, yeah, it's just a competition. I'm gonna stick this here.

struct Division {
public:
	Division(int64_t size, int64_t count) {
		Size = size;
		Count = count;
	}

	int64_t Size;
	int64_t Count;
};

int main()
{
	int testCount;
	cin >> testCount;

	for (int i = 0; i < testCount; i++) {
		int64_t k, n;
		cin >> n >> k;

		if (n == k) {
			cout << "Case #" << i + 1 << ": " << 0 << " " << 0 << endl;
			continue;
		}

		int64_t nextDiv = 1;
		int64_t used = 1;
		
		//For one person:
		int64_t y = n / 2;
		int64_t z = n / 2 - (n % 2 == 0 ? 1 : 0);

		auto comp = [](const Division& a, const Division& b) { return a.Size > b.Size; };
		set<Division, decltype(comp)> divisions(comp);

		if (y == z) {
			divisions.insert(Division(y, 2));
		}
		else {
			divisions.insert(Division(y, 1));
			divisions.insert(Division(z, 1));
		}

		map<int64_t, int64_t> tempDivs;

		while (used < k) {
			tempDivs.clear();
			nextDiv *= 2;

			int64_t rem = k - used;

			for (auto it = divisions.begin(); it != divisions.end(); ++it) {
				auto division = *it;
				y = division.Size / 2;
				z = division.Size / 2 - (division.Size % 2 == 0 ? 1 : 0);

				if (y > 0) {
					if (tempDivs.find(y) == tempDivs.end()) {
						tempDivs[y] = division.Count;
					}
					else {
						tempDivs[y] += division.Count;
					}
				}

				if (z > 0) {
					if (tempDivs.find(z) == tempDivs.end()) {
						tempDivs[z] = division.Count;
					}
					else {
						tempDivs[z] += division.Count;
					}
				}
				
				rem -= division.Count;
				if (rem <= 0)
					break;
			}
			divisions.clear();

			if (rem <= 0)
				break;

			for (auto it = tempDivs.begin(); it != tempDivs.end(); ++it) {
				int64_t size = (*it).first;
				int64_t count = (*it).second;
				divisions.insert(Division(size, count));
			}

			used += nextDiv;
		}

		cout << "Case #" << i + 1 << ": " << y << " " << z << endl;
	}

    return 0;
}

