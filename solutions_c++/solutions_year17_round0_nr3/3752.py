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

using namespace std;
typedef unsigned long long ull;

struct d {
	ull left;
	ull right;
	ull dist() const
	{
		return right - left;
	}
	bool operator<(const d& rhs) {
		if (dist()==rhs.dist()){
			return left < rhs.left;
		}
		return dist() < rhs.dist();
	}
};

int main()
{
	ifstream a("D:\\gcj\\example.txt");
	ofstream o("D:\\gcj\\output.txt");
	int nr; a >> nr;
	std::string line;
	//std::getline(a, line);
	string r("");
	for (int ii = 0; ii<nr; ii++) {
		o << "Case #" << (ii + 1) << ": ";
		cout << "Case #" << (ii + 1) << ": ";
		
		unsigned long long n; a >> n;
		unsigned long long k; a >> k;
		
		vector<d> v;
		d d1;
		d1.left = 0;
		d1.right = n + 1;
		v.push_back(d1);
		std::make_heap(v.begin(), v.end());

		ull Ls, Rs;
		for (ull i = 0; i < k; i++) {
			d curr = v.front();
			std::pop_heap(v.begin(), v.end()); v.pop_back();
			ull middle = curr.left + (curr.right - curr.left) / 2;
			Ls = middle - curr.left - 1;
			Rs = curr.right - middle - 1;
			d d1;
			d1.left = curr.left;
			d1.right = middle;
			if (d1.dist() > 0) {
				v.push_back(d1);
				std::push_heap(v.begin(), v.end());
			}
			d d2;
			d2.left = middle;
			d2.right = curr.right;
			v.push_back(d2);
			std::push_heap(v.begin(), v.end());
		}


		o << max(Ls, Rs) << " " << min(Ls, Rs) << endl;
		cout << max(Ls, Rs) << " " << min(Ls, Rs) << endl;
	}
	a.close();
	o.close();
	char c; cin >> c;
	return 0;
}

