#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	// Vars
	int ncases;
	int s, k;
	int max, maxi, len, left, right;
	vector<int> arr;

	// Input/Output
	ifstream in;
	ofstream out;

	in.open("C_files/C-small-1-attempt0.in");
	out.open("C_files/C-small-1-results.out");

	// Solution
	in >> ncases;

	for (int t = 1; t <= ncases; t++)
	{
		out << "Case #" << t << ": ";
		arr.clear();
		left = 0;
		right = 0;
		in >> s;
		in >> k;

		if (s != k) {
			arr.push_back(s);
			for (int i = 0; i < k; i++) {
				len = arr.size();
				// find node
				maxi = 0;
				max = arr.at(maxi);
				for (int i = 1; i < len; i++) {
					if (max < arr.at(i)) {
						maxi = i;
						max = arr.at(maxi);
					}
				}

				// left - right leafs
				if (max % 2 == 0) {
					left = (max / 2) - 1;
					right = left + 1;
				}
				else {
					left = (max - 1) / 2;
					right = left;
				}

				// update tree
				arr.at(maxi) = left;
				arr.insert(arr.begin() + maxi + 1, right);
			}

			if (right > left) {
				out << right << " " << left;
			}
			else {
				out << left << " " << right;
			}
		}
		else {
			out << "0 0";
		}

		if (t < ncases)
			out << endl;
	}

	in.close();
	out.close();
	return 0;
}