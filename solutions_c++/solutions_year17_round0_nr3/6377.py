#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>

using namespace std;

void get_sequence(int n, vector<int> &bigs, vector<int> &smalls) {
	deque<int> d;
	d.push_back(n); 
	while(!d.empty()) {
		int current = d[0];
		int b;
		int s;
		d.pop_front();

		if (current % 2 == 0) {
			s = (current-1)/2;
			b = s+1;
		} else {
			s = current/2;
			b = s;
		}
		if (b > 0) {
			d.push_back(b);
		}
		if (s > 0) {
			d.push_back(s);
		}
		bigs.push_back(b);
		smalls.push_back(s);
	}
	sort(bigs.begin(), bigs.end());
	reverse(bigs.begin(), bigs.end());
	sort(smalls.begin(), smalls.end());
	reverse(smalls.begin(), smalls.end());
}


int main() {
	vector<int> bigs;
	vector<int> smalls;
	int t;
	int *N;
	int *K;

	cin >> t;
	N = new int[t];
	K = new int[t];
	for (int i = 0; i < t; i++) {
		cin >> N[i];
		cin >> K[i];
	}

	for (int i = 0; i < t; i++) {
		bigs.clear();
		smalls.clear();
		get_sequence(N[i], bigs, smalls);
		cout << "Case #" << i+1 << ": " << bigs[K[i]-1] << " " << smalls[K[i]-1] << endl;
	}
}