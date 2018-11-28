#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<list>

using namespace std;

class Solver {
public:
	Solver(ifstream& ifs, ofstream& ofs) {
		long long int N;
		long long int K;

		ifs >> N >> K;

		list<pair<long long int, long long int>> rooms;

		rooms.push_back(pair<long long int, long long int>(N, 1));

		long long int last_rooms_size;
		long long int last_rooms_num;
		long long int large_room_size;
		long long int small_room_size;
		for (; K > 0;) {
			last_rooms_size = rooms.front().first;
			last_rooms_num = rooms.front().second;

			if (last_rooms_size % 2) {
				large_room_size = (last_rooms_size - 1) / 2;
				small_room_size = (last_rooms_size - 1) / 2;
			}
			else {
				large_room_size = (last_rooms_size - 1) / 2 + 1;
				small_room_size = (last_rooms_size - 1) / 2;
			}

			K -= rooms.front().second;

			// remove largest room
			rooms.pop_front();

			// add large room
			if (large_room_size != 0) {
				bool is_exist = false;
				for (auto& room : rooms) {
					if (room.first == large_room_size) {
						room.second += last_rooms_num;
						is_exist = true;
						break;
					}
				}
				if (!is_exist) {
					rooms.push_back(pair<long long int, long long int>(large_room_size, last_rooms_num));
				}
			}

			// add small room
			if (small_room_size != 0) {
				bool is_exist = false;
				for (auto& room : rooms) {
					if (room.first == small_room_size) {
						room.second += last_rooms_num;
						is_exist = true;
						break;
					}
				}
				if (!is_exist) {
					rooms.push_back(pair<long long int, long long int>(small_room_size, last_rooms_num));
				}
			}
		}

		ofs << large_room_size << " " << small_room_size << endl;
	}
};

void main(int argc, char* argv[]) {
	string fname_i = argv[1];
	string fname_o = fname_i.substr(0, fname_i.find_last_of(".")) + ".out";
	ifstream ifs(fname_i);
	ofstream ofs(fname_o);

	int T;
	ifs >> T;
	for (int No = 1; No <= T; No++) {
		ofs << "Case #" << No << ": ";
		cout << "Case #" << No << "...";
		Solver(ifs, ofs);
		cout << endl;
	}
}
