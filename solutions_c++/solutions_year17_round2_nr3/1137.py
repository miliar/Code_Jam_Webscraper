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

void floyd(int nCity, vector<vector<int>> &disCity) {
	for (int i = 0; i < nCity; i++) {
		disCity[i][i] = 0;
	}
	for (int k = 0; k < nCity; k++) {
		for (int i = 0; i < nCity; i++) {
			for (int j = 0; j < nCity; j++) {
				if (disCity[i][k] >= 0 && disCity[k][j] >= 0) {
					if (disCity[i][j] < 0 || disCity[i][j] > disCity[i][k] + disCity[k][j]) {
						disCity[i][j] = disCity[i][k] + disCity[k][j];
					}
				}
			}
		}
	}
}

void floyd(int nCity, vector<vector<double>> &disCity) {
	for (int i = 0; i < nCity; i++) {
		disCity[i][i] = 0;
	}
	for (int k = 0; k < nCity; k++) {
		for (int i = 0; i < nCity; i++) {
			for (int j = 0; j < nCity; j++) {
				if (disCity[i][k] >= 0 && disCity[k][j] >= 0) {
					if (disCity[i][j] < 0 || disCity[i][j] > disCity[i][k] + disCity[k][j]) {
						disCity[i][j] = disCity[i][k] + disCity[k][j];
					}
				}
			}
		}
	}
}

int main() {
	ifstream in;
	ofstream out;

	in.open("C:\\works\\in.txt");
	out.open("C:\\works\\out.txt");
	int n;

	in >> n;

	for (int caseN = 0; caseN < n; caseN++) {
		int nCity, q;
		in >> nCity;
		in >> q;
		vector<int> disHorse(nCity);
		vector<int> speedHorse(nCity);
		for (int i = 0; i < nCity; i++) {
			in >> disHorse[i];
			in >> speedHorse[i];
		}
		vector<vector<int>> disCity(nCity, vector<int>(nCity));
		for (int i = 0; i < nCity; i++) {
			for (int j = 0; j < nCity; j++) {
				in >> disCity[i][j];
			}
		}
		floyd(nCity, disCity);
		vector<vector<double>> timeCity(nCity, vector<double>(nCity, -1));
		for (int i = 0; i < nCity; i++) {
			for (int j = 0; j < nCity; j++) {
				if (i != j) {
					if (disCity[i][j] > disHorse[i] || disCity[i][j] < 0)
						timeCity[i][j] = -1;
					else {
						timeCity[i][j] = (double)disCity[i][j] / (double)speedHorse[i];
					}
				}
			}
		}
		floyd(nCity, timeCity);
		int start, end;
		out << "Case #" << caseN + 1 << ": ";
		for (int i = 0; i < q; i++) {
			in >> start;
			in >> end;
			out << setprecision(10) << timeCity[start - 1][end - 1] << ' ';
		}
		out << endl;
	}
}