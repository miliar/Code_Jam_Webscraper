#include <iostream>
#include <map>
#include <functional>

using namespace std;


int main() {
	int tsts;
	cin >> tsts;
	for (int tst = 1; tst <= tsts; ++tst) {
		map<long long int, long long int, greater<long long int> > empty_rooms;
		long long int n, k;
		cin >> n >> k;
		--k; //the last one we check individualy
		empty_rooms[n] = 1;
		while (k) {
			auto biggest = empty_rooms.begin();
			if (biggest->second > k)
				k = 0; //doesn't matter if we 
			else {
				k -= biggest->second;
				long long int empty_room_size = biggest->first - 1;
				if (empty_room_size % 2 == 0) {
					empty_rooms[empty_room_size / 2] += biggest->second * 2;
				}
				else {
					empty_rooms[empty_room_size / 2] += biggest->second;
					empty_rooms[empty_room_size / 2 + 1] += biggest->second;
				}
				empty_rooms.erase(biggest);
			}
		}
		long long int empty_space = empty_rooms.begin()->first - 1;
		cout << "case #" << tst << ": " <<  empty_space/2 + empty_space % 2 << " " << empty_space / 2  << "\n";
	}
	return 0;
}