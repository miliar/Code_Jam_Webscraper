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


struct occc {
	int s;
	int f;
};

struct iv {
	int s;
	int f;
	double v;
	int l() const{
		return f - s;
	}
	int val() const{
		return l() * v;
	}

	bool operator<(const iv& other) {
		return s < other.s;
	}
};

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
		int ac; a >> ac;
		int aj; a >> aj;
		
		vector<iv> intervals;
		int occJ = 0;
		int occC = 0;

		for (int i = 0; i < ac; i++) {
			iv occ;
			a >> occ.s;
			a >> occ.f;
			occ.v = 0;
			intervals.push_back(occ);
			occC += occ.l();
		}

		for (int i = 0; i < aj; i++) {
			iv occ;
			a >> occ.s;
			a >> occ.f;
			occ.v = 1;
			intervals.push_back(occ);
			occJ += occ.l();
		}

		if (intervals.empty()) {
			o << 2 << endl;
			cout << 2 << endl;
			continue;
		}

		sort(intervals.begin(), intervals.end());
		
		int switches =0;
		int freeBoth=0;
		int freeJ=0;
		int freeC=0;
		vector<int> freeJV, freeCV;

		if (intervals[0].v != intervals[intervals.size()-1].v) {
			switches++;
			freeBoth += intervals[0].s + 1440 - intervals[intervals.size() - 1].f;
		}
		else {
			if (intervals[0].v == 1) {
				freeJ += intervals[0].s + 1440 - intervals[intervals.size() - 1].f;
				freeJV.push_back(intervals[0].s + 1440 - intervals[intervals.size() - 1].f);
			}
			else if (intervals[0].v == 0) {
				freeC += intervals[0].s + 1440 - intervals[intervals.size() - 1].f;
				freeCV.push_back(intervals[0].s + 1440 - intervals[intervals.size() - 1].f);
			}

		}

		for (auto it = intervals.begin(); it != intervals.end(); it++) {
			auto it2 = it; it2++;
			if (it2 == intervals.end())
				break;

			if ((*it).v != (*it2).v) {
				switches++;
				freeBoth += it2->s - it->f;
			}
			else {
				if (it->v == 1) {
					freeJ += it2->s - it->f;
					freeJV.push_back(it2->s - it->f);
				}
				else if (it->v == 0) {
					freeC += it2->s - it->f;
					freeCV.push_back(it2->s - it->f);
				}
			}
		}

		sort(freeCV.begin(), freeCV.end());
		sort(freeJV.begin(), freeJV.end());
		reverse(freeCV.begin(), freeCV.end());
		reverse(freeJV.begin(), freeJV.end());

		if (freeC + occC > 720) {
			int kellmeg = freeC + occC - 720;
			for (int i = 0; kellmeg > 0; i++) {
				switches += 2;
				kellmeg -= min(kellmeg, freeCV[i]);
			}
		}

		if (freeJ + occJ > 720) {
			int kellmeg = freeJ + occJ - 720;
			for (int i = 0; kellmeg > 0; i++) {
				switches += 2;
				kellmeg -= min(kellmeg, freeJV[i]);
			}
		}

		o << switches << endl;
		cout << switches << endl;
	}
	a.close();
	o.close();
	char c; cin >> c;
	return 0;
}

