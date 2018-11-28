#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

void push_to(deque<long long> &list, long long in) {
	if (in <= 0) return;
	if (in == list.front()) list.push_front(in);
	else list.push_back(in);
}

int main() {
	int ncase = 0;
	cin >> ncase;
	for (int round = 1; round <= ncase; ++round) {
		long long n, k;
		cin >> n >> k;

		if (n == k) {
			cout << "Case #" << round << ": ";
			cout << "0 0" << endl;
			continue;
		}

		deque<long long> ls;
		deque<long long> rs;

		deque<long long> ls_temp;
		deque<long long> rs_temp;

		int new_sep = (n - 1) / 2;
		int new_rest = (n - 1) - new_sep;
		ls.push_back(new_sep);
		rs.push_back(new_rest);

		bool left = new_sep >= new_rest;
		for(int i = 1; i < k; ++i) {
			int max;
			if (left) {
				max = ls.front();
				ls.pop_front();

				new_sep = (max - 1) / 2;
				new_rest = (max - 1) - new_sep;
				push_to(ls_temp, new_rest);
				push_to(ls_temp, new_sep);
				if (ls.size() == 0) {
					ls = ls_temp;
					ls_temp.clear();
				}
			} else {
				max = rs.front();
				rs.pop_front();

				new_sep = (max - 1) / 2;
				new_rest = (max - 1) - new_sep;
				push_to(rs_temp, new_rest);
				push_to(rs_temp, new_sep);
				if (rs.size() == 0) {
					rs = rs_temp;
					rs_temp.clear();
				}
			}
			if (ls.size() == 0) left = false;
			else 
				left = ls.front() >= rs.front();
		}
		//		if (new_rest < 0) new_rest = 0;
		//		if (new_sep < 0) new_sep = 0;

		cout << "Case #" << round << ": ";
		cout << new_rest << " " << new_sep << endl;
	}
	return 0;
}
