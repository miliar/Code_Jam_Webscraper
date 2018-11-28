//============================================================================
// Name        : .cpp
// Author      : Omar Ahmed
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <bits/stdc++.h>
#define SMALL
//#define LARGE
//#define FILE
using namespace std;
vector<int> v;
void fill(long long n) {
	if (n == 0)
		return;
	fill(n / 10);
	v.push_back(n % 10);
}
long long check(long long n) {
	fill(n);
	bool found = false;
	int o = -1;
	for (unsigned int i = 0; i < v.size(); i++) {
		if (found) {
			v[i] = 9;
		} else if (i + 1 < v.size() && v[i] > v[i + 1]) {
			--v[i];
			found = true;
			if (o != -1)
				break;
		} else if (o == -1 && i + 1 < v.size() && v[i] == v[i + 1]) {
			o = i;
		}
	}
	if (found && o != -1) {
		v[o]--;
		for (unsigned int i = o + 1; i < v.size(); i++) {
			v[i] = 9;
		}
	}
	long long x = 1, nn = 0;
	for (int i = v.size() - 1; i >= 0; i--) {
		nn += x * v[i];
		x *= 10;
	}
	return nn;
}

int main() {
#ifdef SMALL
	freopen("C:\\Users\\HP\\Downloads\\B-small-attempt1.in", "rt", stdin);
#endif
#ifdef LARGE
	freopen("C:\\Users\\HP\\Downloads\\C-large-practice.in", "rt", stdin);
#endif
#ifdef FILE
	freopen("input.txt", "rt", stdin);
#endif
	freopen("output.txt", "wt", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		long long N;
		cin >> N;
		cout << "Case #" << t+1 << ": " << check(N) << endl;
		v.clear();
	}
	return 0;
}
