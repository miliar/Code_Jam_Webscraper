#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

pair<unsigned long long, unsigned long long> solve(unsigned long long n, unsigned long long k){
	map<unsigned long long, unsigned long long> map;
	vector<unsigned long long> elements;
	unsigned long long a, b;

	elements.push_back(n);
	map.insert(make_pair(n, 1));
	
	unsigned long long count = 0;
	while(true) {
		auto cur = elements.front();
		auto cur_map = map.find(cur);
		auto cur_count = cur_map->second;

		a = cur / 2;
		b = cur / 2 + (cur & 1) - 1;

		if(count + cur_count >= k) {
			return make_pair(a, b);
		}

		elements.erase(elements.begin());
		map.erase(cur_map);

		if(find(elements.begin(), elements.end(), a) == elements.end()) {
			elements.push_back(a);
			map.insert(make_pair(a, 0));
		}

		if(a == b) {
			map[a] += 2 * cur_count;
		}
		else {
			if(find(elements.begin(), elements.end(), b) == elements.end()) {
				elements.push_back(b);
				map.insert(make_pair(b, 0));
			}

			map[a] += cur_count;
			map[b] += cur_count;			
		}

		count += cur_count;
	}

	return make_pair(-1, -1);
}

int main() {
	int t;
	unsigned long long n, k;

	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> n;
		cin >> k;
		auto p = solve(n, k);
		cout << "Case #" << (i + 1) << ": " << p.first << " " << p.second << endl;
	}

	return EXIT_SUCCESS;
}
