#include <bits/stdc++.h>
using namespace std;

long long val(vector<int> q) {
	long long ret = 0;
	for (int i = (int)q.size() - 1; i >= 0; i--)
		ret = ret*10 + q[i];
	return ret;
}

void main2() {
	long long n;
	cin >> n;
	vector<int> d;
	while(n) {
		d.push_back(n%10);
		n/=10;
	}
	int pnt = (int)d.size() - 1;
	while (pnt > 0 && d[pnt-1] >= d[pnt])
		pnt--;
	if (pnt == 0) {
		cout << val(d) << endl;
	} else {
		while (pnt+1 < (int)d.size() && d[pnt] == d[pnt+1])
			pnt++;
		d[pnt]--;
		for (int i = 0; i < pnt; i++)
			d[i] = 9;
		cout << val(d) << endl;
	}
}

int main() {
	int t;
	cin >> t;
	for (int o = 1; o <= t; o++) {
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
