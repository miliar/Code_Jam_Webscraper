#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

constexpr int halfday = 720;
constexpr int day = halfday*2;

int potentials[2];
vector<int> reserves[2];
int changes;

struct act {
	int start;
	int end;
	int person;

	void read(int per) {
		cin >> start >> end;
		person = per;
	}

	void eat(act other) {
		potentials[person] += (end-start);
		if (other.start <= start) {
			other.start += day;
			other.end += day;
		}
		int len = other.start - end;
		if (person == other.person) {
			potentials[person] += len;
			reserves[1-person].push_back(len);
		} else {
			potentials[0] += len;
			potentials[1] += len;
			changes++;
		}
	}
};

bool operator<(const act a, const act b) {
	return a.start < b.start;
}

int main() {
	int cases;
	cin >> cases;
	for (int casei=1; casei<=cases; casei++) {
		int n1, n2;
		cin >> n1 >> n2;
		act arr[n1+n2];
		for (int i=0; i<n1; i++) {
			arr[i].read(0);
		}
		for (int i=n1; i<n1+n2; i++) {
			arr[i].read(1);
		}
		sort(arr, arr+n1+n2);
		for (auto& x : potentials) x = 0;
		for (auto& x : reserves) x.clear();
		changes = 0;
		for (int i=0; i<n1+n2; i++) {
			arr[i].eat(arr[(i+1)%(n1+n2)]);
		}
		assert(changes%2 == 0);
		//cerr << potentials[0] << " : " << potentials[1] << " (ch:) " << changes << endl;
		assert(potentials[0] + potentials[1] >= day);
		for (int p=0; p<2; p++) {
			sort(reserves[p].rbegin(), reserves[p].rend());
			for (int x : reserves[p]) {
				if (potentials[p] < halfday) {
					potentials[p] += x;
					changes += 2;
				}
			}
		}
		//cerr << potentials[0] << " : " << potentials[1] << " (ch:) " << changes << endl;
		assert(changes%2 == 0);
		cout << "Case #" << casei << ": " << changes << endl;
	}
}
