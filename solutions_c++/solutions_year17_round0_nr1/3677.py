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
		std::getline(a, line);
		int pos=line.find(" ");
		string pancakes(line.begin(), line.begin() + pos);
		int k = atoi(string(line.begin() + pos + 1, line.end()).c_str());

		vector<bool> t;
		for (auto i : pancakes) {
			if (i == '+') {
				t.push_back(true);
			}
			else
				t.push_back(false);
		}

		bool poss = true;
		int min = 0;
		for (int i = 0; i < t.size() && poss; i++) {
			if (!t[i]) {
				min++;
				if (i + k <= t.size())
					for (int j = i; j < i + k; j++) {
						t[j] = !t[j];
					}
				else {
					poss = false;
					break;
				}
			}
		}

		r = poss ?  to_string(min) : "IMPOSSIBLE";


		o << r << endl;
		cout << r << endl;
	}
	a.close();
	o.close();
	char c; cin >> c;
	return 0;
}

