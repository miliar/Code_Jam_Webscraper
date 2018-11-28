#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <vector>
#include <cmath>

using namespace std;
typedef vector<vector<char> > vvc;
typedef vector<vector<bool> > vvb;

int main()
{
	ifstream a("D:\\gcj\\example.txt");
	ofstream o("D:\\gcj\\output.txt");
	int nr; a >> nr;
	std::string line;
	std::getline(a, line);
	
	for (int ii = 0; ii<nr; ii++) {
		o << "Case #" << (ii + 1) << ": ";
		cout << "Case #" << (ii + 1) << ": ";
		int D; a >> D;
		int N; a >> N;
		vector<double> t = vector<double>(N, 0);
		for (int i = 0; i < N; i++) {
			int Ki; a >> Ki;
			int Si; a >> Si;
			int d = D - Ki;
			t[i] = double(d) / double(Si);
		}
		double maxT = *(max_element(t.begin(), t.end()));
		double speed = double(D) / maxT;


		cout << fixed << speed << endl;
		o << fixed << speed << endl;
	}
	

	a.close();
	o.close();
	char c; cin >> c;
	return 0;
}

