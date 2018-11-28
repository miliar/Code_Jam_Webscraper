#include <fstream>
#include <algorithm>
#include <vector>
#include <iostream>
#include <math.h>

using namespace std;
int D, N;
double process(vector<pair<int, int> > horses) {
	int i;
	double mx = -1;
	for (i = 0; i < N; i++) {
		pair<int, int> horse = horses[i];
		double re = (double)(D - horse.first) / horse.second;
		if (mx < re) {
			mx = re;
		}
	}
	return (double)D / mx;
}

int main() {
    ifstream in("input.in");
    ofstream out("output.out");

    int C, k, s;
    out << fixed;
    out.setf(ios::showpoint); 
    out.precision(6);
    in >> C;
    for (int c = 1; c <= C; c++) {
    	in >> D >> N;
    	vector<pair<int, int> > horses;
    	for (int i = 0; i < N; i++) {
    		in >> k >> s;
    		horses.push_back(make_pair(k, s));
    	}
    	out << "Case #" << c << ": " << process(horses) << endl;
    }
    return 0;
}