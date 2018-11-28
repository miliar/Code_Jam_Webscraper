#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <map>
#include <cassert>

using namespace std;

typedef long long ll;

template <typename KeyT, typename ValueT>
void add_count(map<KeyT, ValueT>& m, KeyT key, ValueT value) {
	auto it = m.find(key);
	if (it == m.end()) {
		m[key] = value;
	}
	else {
		it->second += value;
	}
}

template <typename KeyT, typename ValueT> 
void sub_count(map<KeyT, ValueT>& m, KeyT key, ValueT value) {
	m[key] -= value;
	assert(m[key] >= 0);
	if (m[key] == 0) {
		m.erase(key);
	}
}

int main()
{
	int T;
	cin >> T;
	for (int casen = 1; casen <= T; ++casen) {
		long long N, K;
		cin >> N >> K;
		map<long long, long long> stalls;   // a map size -> number of empty intervals of stalls
		stalls[N] = 1;
		ll active_size = N; // get pair with maximal key from the map
		ll active_count = N; // see above
		while (K > 0) {
			auto largest = stalls.rbegin();
			active_size = largest->first; // get pair with maximal key from the map
			active_count = largest->second; // see above
			ll place_guests = min(active_count, K);
			K -= place_guests;
			sub_count(stalls, active_size, place_guests);
			if ((active_size - 1) % 2 == 0) add_count(stalls, (active_size - 1) / 2, place_guests * 2);
			else {
				add_count(stalls, (active_size - 1) / 2, place_guests);
				add_count(stalls, (active_size - 1) / 2 + 1, place_guests);
			}
		}
		ll mn = (active_size - 1) / 2;
		cout << "Case #" << casen << ": " << (active_size - 1 - mn) << ' ' << mn << '\n';
	}
	return 0;
}

