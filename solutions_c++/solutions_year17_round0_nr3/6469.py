#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef unsigned int uint;

struct stalls {
	unsigned int left;
	unsigned int right;
	bool empty;
};

vector<stalls> genSeats(unsigned int n) {
	vector<stalls> out;
	for (unsigned int i = 0; i < n; i++) {
		stalls temp;
		temp.left = i;
		temp.right = n - i - 1;
		temp.empty = true;
		out.push_back(temp);
	}
	return out;
}

unsigned int getBestStall(vector<stalls> seats) {
	unsigned int bestIndex = 0;
	bool hasInitial = false;
	for (unsigned int i = 0; i < seats.size();i++) {
		if (seats[i].empty) {
			if (!hasInitial) {
				bestIndex = i;
				hasInitial = true;
			} else {
				stalls best = seats[bestIndex];
				stalls current = seats[i];
				uint Cmin = min(current.left, current.right);
				uint Cmax = max(current.left, current.right);
				uint Bmin = min(best.left, best.right);
				uint Bmax = max(best.left, best.right);
				if (Cmin > Bmin || (Cmin == Bmin && Cmax > Bmax))
				{
					bestIndex = i;
				}
			}
		}
	}
	return bestIndex;
}

void takeSeat(vector<stalls>& s, int seat) {
	unsigned int toRemove = 0;
	for (signed long i = seat - 1; i > -1 && s[i].empty; i--) {
		if (i == seat - 1) {
			toRemove = s[i].right;
			s[i].right = 0;
		}
		else {
			s[i].right = s[i].right < toRemove ? 0 : (s[i].right - toRemove);
		}
	}
	for (unsigned int i = seat + 1; i < s.size() && s[i].empty; i++) {
		if (i == seat + 1) {
			toRemove = s[i].left;
			s[i].left = 0;
		}
		else {
			s[i].left = s[i].left < toRemove ? 0 : (s[i].left - toRemove);
		}
	}
}

int main() {
	unsigned int T = 0;
	cin >> T;
	for (unsigned int i = 0; i < T; i++) {
		unsigned int N = 0;
		unsigned int K = 0;
		cin >> N >> K;

		cout << "Case #" << (i + 1) << ": ";
		vector<stalls> seats = genSeats(N);
		while (K > 1) {
			unsigned int seat = getBestStall(seats);
			seats[seat].empty = false;
			takeSeat(seats, seat);
			K--;
		}
		stalls best = seats[getBestStall(seats)];
		cout << max(best.left, best.right) << " " << min(best.left, best.right);
		cout << endl;
	}
}