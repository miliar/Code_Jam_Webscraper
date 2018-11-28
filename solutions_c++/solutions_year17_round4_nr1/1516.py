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

typedef long long ll;
typedef long double ldb;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;


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

		int N; a >> N;
		int P; a >> P;

		int fcs = 0;

		int c[4] = {0,0,0,0};

		for (int j = 0; j < N; j++) {
			int curr; a >> curr;
			c[curr%P]++;
		}

		fcs += c[0];

		for (int i=1; i<P; i++)
			for (int j = i; j < P; j++) {
				if ((i + j) % P == 0) {
					int k = min(c[i], c[j]);
					while (k > 0) {
						c[i] --;
						if (c[j] > 0) c[j]--; else { c[i]++;  break; };
						fcs++;
						k = min(c[i], c[j]);
					}
				}
			}

		for (int i = 1; i<P; i++)
			for (int j = i; j < P; j++) 
				for (int m = j; m < P; m++) {
					if ((i + j + m) % P == 0) {
						int k = min(min(c[i], c[j]), c[m]);
						while (k > 0) {
							c[i] --;
							if (c[j] > 0) c[j]--; else { c[i]++;  break; };
							if (c[m] > 0) c[m]--; else { c[i]++; c[j]++;  break; };
							fcs++;
							k = min(min(c[i], c[j]), c[m]);
						}

					}
				}

		for (int i = 1; i<P; i++)
			for (int j = i; j < P; j++)
				for (int m = j; m < P; m++)
					for (int n = j; n < P; n++) {
						if ((i + j + m + n) % P == 0) {
							int k = min(min(c[i], c[j]), min(c[m], c[n]));
							while (k > 0) {
								c[i] --;
								if (c[j] > 0) c[j]--; else { c[i]++;  break; };
								if (c[m] > 0) c[m]--; else { c[i]++; c[j]++;  break; };
								if (c[n] > 0) c[n]--; else { c[i]++; c[j]++; c[n]++;  break; };
								fcs++;
								k = min(min(c[i], c[j]), min(c[m], c[n]));
							}
						}
					}

		if (c[1] + c[2] + c[3] > 0)
			fcs++;

		o << fcs << endl;
		cout << fcs << endl;
	}
	a.close();
	o.close();
	char c; cin >> c;
	return 0;
}

