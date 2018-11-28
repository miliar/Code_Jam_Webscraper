#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
#define pi           3.14159265358979323846

struct p {
	int r;
	int h;

	double myh() const{
		return double(h) * 2 * double(r) * pi;
	}

	double myr() const {
		return double(r) * double(r) * pi;
	}

	double mys() const {
		return myr() + myh();
	}

	bool operator<(const p& other) {
		if (myh() != other.myh())
			return myh() < other.myh();
		else
			return r < other.r;
	}
};

double ccc(vector<p>& ps, int k, int ind, int ii) {
	swap(ps[ind], ps[ii]);
	double h = 0;
	double r = 0;
	for (int i = 0; i < k; i++) {
		h += ps[i].myh();
		if (ps[i].myr() > r) {
			r = ps[i].myr();
		}
	}
	swap(ps[ind], ps[ii]);
	return r + h;
}

int main()
{
	ifstream a("D:\\gcj\\example.txt");
	ofstream o("D:\\gcj\\output.txt");
	int nr; a >> nr;
	std::string line;
	std::getline(a, line);
	string r("");
	for (int ii = 0; ii<nr; ii++) {
		o << "Case #" << (ii + 1) << ": ";
		cout << "Case #" << (ii + 1) << ": ";
		int n; a >> n;
		int k; a >> k;
		vector<p> r;

		for (int i = 0; i < n; i++) {
			p rr; a >> rr.r;
			a >> rr.h;
			r.push_back(rr);
		}

		sort(r.begin(), r.end());
		reverse(r.begin(), r.end());

		int ind = -1;
		int minH = INT_MAX;
		double H = 0;
		for (int i = 0; i < k; i++) {
			if (r[i].myh() < minH) {
				ind = i;
				minH = r[i].r;
			}
			if (r[i].myh() == minH && ind!=-1 && r[i].r < r[ind].r) {
				ind = i;
				minH = r[i].r;
			}
			H += r[i].myh();
		}

		double ret = ccc(r, k, ind, ind);


		for (int i = k; i < n; i++) {
			for (int j = 0; j < k; j++) {
				double cc = ccc(r, k, j, i);
				if (cc > ret) {
					ret = cc;
				}
			}
		}

		o << fixed << ret << endl;
		cout << fixed << ret << endl;
	}
	a.close();
	o.close();
	char c; cin >> c;
	return 0;
}

