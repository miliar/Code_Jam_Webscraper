#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <list>


using namespace std;

char col[] = { 'R', 'O', 'Y', 'G' , 'B', 'V' };

bool check(int _a, int _b) {
	char a = col[_a];
	char b = col[_b];
	switch (a)
	{
		case 'R':
			return b!= 'R' && b != 'O' && b != 'V';
		case 'B':
			return b!= 'B' && b != 'G' && b != 'V';
		case 'Y':
			return b != 'Y' && b != 'O' && b != 'G';
		case 'O':
			return b != 'Y' && b != 'R' && b != 'O' && b != 'V' && b != 'G';
		case 'G':
			return b != 'B' && b != 'G' && b != 'V' && b != 'Y' && b != 'O';
		case 'V':
			return b != 'R' && b != 'O' && b != 'V' && b != 'B' && b != 'G';
	}
	return false;
}

bool fill(int R, int O, int Y, int G, int B, int V, vector<char>& res, int ofs) {
	if (ofs == res.size()) {
		return check(res[0], res[ofs - 1]);
	}

	bool valid = false;
	if (R > 0 && check(res[ofs - 1], 'R')) {
		res[ofs] = 'R';
		valid = fill(R - 1, O, Y, G, B, V, res, ofs+1);
	}
	if (!valid && O > 0 && check(res[ofs - 1], 'O')) {
		res[ofs] = 'O';
		valid = fill(R, O-1, Y, G, B, V, res, ofs + 1);
	}
	if (!valid && Y > 0 && check(res[ofs - 1], 'Y')) {
		res[ofs] = 'Y';
		valid = fill(R, O, Y-1, G, B, V, res, ofs + 1);
	}
	if (!valid && G > 0 && check(res[ofs - 1], 'G')) {
		res[ofs] = 'G';
		valid = fill(R, O, Y, G-1, B, V, res, ofs + 1);
	}
	if (!valid && B > 0 && check(res[ofs - 1], 'B')) {
		res[ofs] = 'B';
		valid = fill(R, O, Y, G, B-1, V, res, ofs + 1);
	}
	if (!valid && V > 0 && check(res[ofs - 1], 'V')) {
		res[ofs] = 'V';
		valid = fill(R, O, Y, G, B, V-1, res, ofs + 1);
	}
	return valid;
}

int getmin(vector<int>& q, int last) {
	int cnt = 0;
	int c;
	for (int i = 0; i < q.size(); ++i) {
		if (q[i] > cnt && (last ==-1 ||check(last, i))) {
			cnt = q[i];
			c = i;
		}
	}

	return c;
}
int main() {
#ifdef _DEBUG
	std::ifstream in("C:\\Users\\silvio.lazzeretti\\Downloads\\b-example.txt");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
#endif
	int T;
	cin >> T;
	int t = 0;
	while (++t <= T) {
		int N;
		vector<int> q(6);
		cin >> N;
		for(int i=0;i<6;++i)
			cin >> q[i];
		
		vector<int> res(N);
		bool valid = false;

		/*if (R > 0) {
			res[0] = 'R';
			valid = fill(R - 1, O, Y, G, B, V, res, 1);
		}
		if (!valid && O > 0) {
			res[0] = 'O';
			valid = fill(R, O-1, Y, G, B, V, res, 1);
		}
		if (!valid && Y > 0) {
			res[0] = 'Y';
			valid = fill(R, O, Y-1, G, B, V, res, 1);
		}
		if (!valid && G > 0) {
			res[0] = 'G';
			valid = fill(R, O, Y, G-1, B, V, res, 1);
		}
		if (!valid && B > 0) {
			res[0] = 'B';
			valid = fill(R, O, Y, G, B-1, V, res, 1);
		}
		if (!valid && V > 0) {
			res[0] = 'V';
			valid = fill(R, O, Y, G, B, V-1, res, 1);
		}*/
		
		if (q[0] <= q[2] + q[4] && q[2] <= q[0] + q[4] && q[4] <= q[0] + q[2]) {
			valid = true;

			int last = -1;
			for (int i = 0; i < N; ++i) {
				int  pos = getmin(q, last);
				last = pos;
				q[pos]--;
				res[i] = pos;
			}

			if (res[0] == res[N - 1]) {
				int i1 = N - 1;
				while (!check(res[(i1+1)%N], res[i1])) {
					swap(res[i1], res[i1 - 1]);
					i1--;
				}
			}

		}

		cout << "Case #" << t << ": ";
		if (valid) {
			for (auto c : res)
				cout << col[c];
		}
		else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}