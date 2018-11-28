#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

typedef unsigned long long BigInt;

struct Room {
	Room(){}
	Room(BigInt space) {
		this->space = space;
		this->num = 1;
	}
	Room(BigInt space, BigInt num) { 
		this->space = space;
		this->num = num;
	}
	BigInt space;
	BigInt num;
	void debug_string(string pre = "") {
		cout << pre << "space:" << space << " num:" << num << endl;
	}
};

class Queue {
public:
	bool pop(Room &room) {
		if (rooms.size() == 0) {
			return false;
		}
		room = *(rooms.begin());
		// room.debug_string("pop ");
		rooms.erase(rooms.begin());
		return true;
	}
	void push(Room &room) {
		// room.debug_string("push ");
		if (rooms.empty()) {
			rooms.push_back(room);
			return;
		}
		size_t l = rooms.size();
		if (rooms[l - 1].space == room.space) {
			rooms[l - 1].num += room.num;
		}
		else {
			rooms.push_back(room);
		}
	}
	vector<Room> rooms;
};

void search(BigInt N, BigInt K, BigInt &max, BigInt & min) {
	BigInt num = 0;
	Queue queue;
	queue.push(Room(N, 1));
	Room tempRoom;
	BigInt maxSpace = 0;
	BigInt minSpace = -1;
	while (queue.pop(tempRoom)) {
		num += tempRoom.num;
		queue.push(Room(tempRoom.space / 2, tempRoom.num));
		queue.push(Room((tempRoom.space - 1) / 2, tempRoom.num));
		if (num >= K) {
			maxSpace = tempRoom.space / 2;
			minSpace = (tempRoom.space - 1) / 2;
			break;
		}
	}
	max = maxSpace;
	min = minSpace;
}

void run(istream &in, ostream &out) {
	int T;
	in >> T;
	for (int i = 0; i < T; ++i) {
		BigInt K, N;
		in >> N >> K;
		BigInt max, min;
		search(N, K, max, min);
		out << "Case #" << (i + 1) << ": " << max << " " << min << endl;
	}
}

int main() {
	// ifstream fin("C-large.in");
	// ofstream fout("C-large.out");
	// run(fin, fout);
	run(cin, cout);
	return 0;
}
