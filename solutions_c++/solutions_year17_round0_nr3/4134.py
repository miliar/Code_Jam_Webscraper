#include <iostream>
#include <fstream>
#include <string>
#include <queue>

using namespace std;

int main() {
	ifstream fin("C-small-2-attempt0.in");
	ofstream fout("output1.out");
	int t;
	fin >> t;
	for (int x = 1; x <= t; x++) {
		int n, k, a = 0, b = 0, y;
		fin >> n >> k;
		if(n == k) 
			fout << "Case #" << x << ": " << 0 << " " << 0 << endl;
	     else {
			priority_queue<int> q;
		q.push(n);
		for(int i = 0; i < k; i++) {
			y = q.top();
			q.pop();
			a = y/2;
			b = a - (y%2 == 0);
			//cout << a << " " << b;
			q.push(a);
			q.push(b);
		}
		fout << "Case #" << x << ": " << a << " " << b << endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}