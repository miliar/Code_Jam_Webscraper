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
		double maxT = 0;
		int dis, nHorse;
		in >> dis;
		in >> nHorse;
		for (int i = 0; i < nHorse; i++) {
			int hDis, s;
			in >> hDis;
			in >> s;
			hDis = dis - hDis;
			if ((double)hDis / (double)s > maxT) {
				maxT = (double)hDis / (double)s;
			}
		}
		out << "Case #" << caseN + 1 << ": ";
		out << setprecision(10) << (double)dis / (double)maxT;
		out << endl;
	}
}