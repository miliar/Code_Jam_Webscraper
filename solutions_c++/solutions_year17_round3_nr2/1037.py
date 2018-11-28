#include <iostream>
#include <algorithm>
using namespace std;

const int T = 100;
const int A = 2;
const int B = 2;

class Event {

public:

	int start, end;

	Event() : Event(0, 0) {}
	Event(int start, int end) {
		
		set(start, end);

	}

	void set(int start, int end) {

		this->start = start;
		this->end = end;

	}

	static int diff(int t1, int t2) {

		if (t1 <= t2) {
			return t2 - t1;
		}
		else {
			return t2 + 1440 - t1;
		}

	}

	friend int operator+(const Event& a, const Event& b) {

		return Event::diff(a.start, b.end);

	}

};



int main() {

	int t;
	cin >> t;

	for (int caseNo = 1; caseNo <= t; caseNo++) {

		int a, b;
		Event cameron[A], jamie[B];

		cin >> a >> b;

		for (int i = 0; i < a; i++) {
			int s, d;
			cin >> s >> d;
			cameron[i].set(s, d);
		}

		for (int i = 0; i < b; i++) {
			int s, d;
			cin >> s >> d;
			jamie[i].set(s, d);
		}

		int exchanges = 2;

		if (a == 2) {
			if (cameron[0] + cameron[1] > 720 && cameron[1] + cameron[0] > 720) {
				exchanges = 4;
			}
		}
		else if (b == 2) {
			if (jamie[0] + jamie[1] > 720 && jamie[1] + jamie[0] > 720) {
				exchanges = 4;
			}
		}

		cout << "Case #" << caseNo << ": " << exchanges << endl;

	}
}