#include <iostream>
#include <map>

using namespace std;

using num = long long int;

pair<num, num> splitint(num len) {
	len--;
	num small = len/2;
	num large = len - small;
	return make_pair(small, large);
}

int main() {
	int cases;
	cin >> cases;
	for (int casei=0; casei<cases; casei++) {
		num n, k;
		cin >> n >> k;
		map<num, num> ma;
		ma[n] = 1;
		num todo = k - 1;
		while (todo) {
			num curint = ma.rbegin()->first;
			//if (!ma[curint]) {
			//	ma.erase(curint);
			//	continue;
			//}
			num howmany = min(todo, ma[curint]);
			ma[curint] -= howmany;
			todo -= howmany;
			if (ma[curint] == 0) ma.erase(curint);
			//cout << "splitting " << howmany << " of " << curint << endl;
			pair<num, num> p = splitint(curint);
			ma[p.first] += howmany;
			ma[p.second] += howmany;
		}
		pair<num, num> p = splitint(ma.rbegin()->first);
		cout << "Case #" << casei+1 << ": " << p.second << " " << p.first << endl;
	}
}
