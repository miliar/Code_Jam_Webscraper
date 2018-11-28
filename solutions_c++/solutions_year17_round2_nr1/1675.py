#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

int main() {
	
	int test;
	cin>>test;
	for (int testc = 1; testc<=test; testc++) {
		
		int d,n;
		cin>>d>>n;
		double mx = 0;
		
		for (int i = 0; i < n; i++) {
			int start, spd;
			cin>>start>>spd;
			double t = (double)(d-start) / (double)spd;
			mx = max(t, mx);
		}
		
		printf("Case #%d: %lf\n", testc, (double)d / mx);
	}
	return 0;
}

