#include <iostream>
#include <fstream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int T = 0;
	long long N = 0, K = 0, max = 0, y = 0, z = 0;
	ifstream in("C-small-1-attempt1.in");
	ofstream out("C-Small_out.txt");
	in >> T;
	for (int i = 0; i < T; i++) {
		in >> N >> K;
		vector<long long> spaces(1, N);
		vector<long long>::iterator it = spaces.begin();
		for (int j = 0; j < K; j++) {
			it = max_element(spaces.begin(), spaces.end());
			long long ind = distance(spaces.begin(),it);
			max = *it;
			y = spaces[ind] / 2;
			if (spaces[ind] % 2 == 0) {
				z = y - 1;
			} else {
				z = y;
			}
			spaces[ind] = y;
			spaces.insert(spaces.begin(),z);
		}
		out << "Case #" << i + 1 << ": " << y << " " << z << "\n";
	}
}
