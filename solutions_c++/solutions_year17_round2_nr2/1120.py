#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <math.h>
#include <stack>
#include <unordered_set>
#include <set>
#include <iomanip>
using namespace std;

struct node {
	set<node*> out;
	set<node*> in;
};

bool inRange(int p, int n, int c) {
	double range = (double)p / (n * c);
	return (range >= 0.9 && range <= 1.1);
}

int findC(double p1, double n1) {
	return round(p1 / n1);
}

int findC(double p1, double n1, double p2, double n2) {
	if (p1 / n1 > p2 / n2) {
		return ceil((p1 / (n1 * 1.1)));
	}
	else {
		return floor(p1 / (n1 * 0.9));
	}
}

bool findPathAndRevert(node *start, node *end) {
	if (start == end) return true;
	if (start->out.empty()) return false;
	auto it = start->out.begin();
	while (it != start->out.end()) {
		node *e = *it;
		start->out.erase(e);
		if (findPathAndRevert(e, end)) {
			return true;
		}
		start->out.insert(e);
		it = start->out.find(e);
		it++;
	}
	return false;
}

int main() {
	ifstream in;
	ofstream out;

	in.open("C:\\works\\in.txt");
	out.open("C:\\works\\out.txt");
	int n;

	in >> n;

	for (int caseN = 0; caseN < n; caseN++) {
		bool possible = true;
		vector<int> colors(6);
		vector<char> symbols = { 'R', 'O', 'Y', 'G', 'B', 'V' };
		string rv;
		int t, r, o, y, g, b, v;
		in >> t;
		in >> colors[0];
		in >> colors[1];
		in >> colors[2];
		in >> colors[3];
		in >> colors[4];
		in >> colors[5];
		int curIdx = -1;
		int nxtIdx = -1;
		int initIdx = -1;
		out << "Case #" << caseN + 1 << ": ";
		while (t > 0) {
			for (int i = 0; i < 6; i++) {
				if (colors[i] > 0 && i != curIdx && (nxtIdx == -1 || (colors[i] > colors[nxtIdx] || (colors[i] == colors[nxtIdx] && i == initIdx))))
					nxtIdx = i;
			}
			if (initIdx == -1)
				initIdx = nxtIdx;
			if (nxtIdx < 0) {
				possible = false;
				break;
			}
			rv += symbols[nxtIdx];
			colors[nxtIdx]--;
			t--;
			curIdx = nxtIdx;
			nxtIdx = -1;
		}
		if (rv.size() >= 2 && rv[0] == rv[rv.size() - 1])
			possible = false;
		if (!possible)
			out << "IMPOSSIBLE";
		else
			out << rv;
		out << endl;
	}
}