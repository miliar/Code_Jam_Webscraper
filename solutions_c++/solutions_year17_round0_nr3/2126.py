#include <cstdio>
#include <iostream>
#include <map>
#include <functional>


using namespace std;

map<unsigned long long, unsigned long long, greater<unsigned long long>> LRSMap;

pair<unsigned long long, unsigned long long> solve(unsigned long long n, unsigned long long k) {
	LRSMap[n]++;

	unsigned long long occupied = 0ull;
	for (auto entry = LRSMap.begin (); entry != LRSMap.end ();) {
		if (entry->first == 0ull)
			return { 0ull, 0ull };
		
		unsigned long long ls = (entry->first - 1ull) / 2ull;
		unsigned long long rs = entry->first / 2ull;

		occupied += entry->second;

		if(k <= occupied) {
			return { rs, ls };
		}

		LRSMap[ls] += entry->second;
		LRSMap[rs] += entry->second;

		entry = LRSMap.erase (entry);
	}
	
	return { 0ull, 0ull };
}

int main () {
	ios_base::sync_with_stdio (false), cin.tie (nullptr);

	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int t;
	scanf ("%d", &t);
	for (int tc = 0; tc < t; tc++) {
		unsigned long long n, k;
		scanf ("%llu %llu", &n, &k);

		auto result = solve (n, k);

		printf ("Case #%d: %llu %llu\n", tc + 1, result.first, result.second);

		LRSMap.clear ();
	}


	fflush (stdout);
	fclose (stdin);
	fclose (stdout);

	return 0;
}
