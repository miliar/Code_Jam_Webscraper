#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <queue>
#include <iomanip>

using namespace std;

struct Unicorn {
	Unicorn(int f_, char c_, bool isfirst_) :f(f_), c(c_), isfirst(isfirst_) {}
	Unicorn():f(0),isfirst(false) {}

	int f;
	char c;
	bool isfirst;

	bool operator<(const Unicorn& u) const {
		if (f == u.f && isfirst) {
			return false;
		}
		else if (f == u.f && u.isfirst) {
			return true;
		}
		return f < u.f;
	}
};

int main() {
	ifstream fin("B-small-attempt2.in");
	ofstream fout("output4.txt");

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++) {
		int n,r, o, y, g, b, v;
		fin >> n >> r >> o >> y >> g >> b >> v;

		//small set only (o=g=v=0)

		priority_queue<Unicorn> q;
		if(r != 0) q.push(Unicorn(r, 'R',false));
		if(b != 0) q.push(Unicorn(b, 'B',false));
		if(y != 0) q.push(Unicorn(y, 'Y',false));

		string answer = "";

		Unicorn toadd;
		bool f = true;

		while (!q.empty()) {
			Unicorn next = q.top();
			q.pop();
			next.f--;
			if (f) {
				next.isfirst = true;
				f = false;
			}
			answer += next.c;
			if (toadd.f > 0) q.push(toadd);
			toadd = next;
		}

		string output;
		if (answer.length() == n && answer[answer.length() - 1] != answer[0]) {
			output = answer;
		}
		else {
			output = "IMPOSSIBLE";
		}

		fout << "Case #" << to_string(t) << ": " << output << endl;
	}
	fout.close();
	return 0;
}