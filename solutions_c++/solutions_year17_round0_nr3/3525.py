#include <cstdlib>
#include <string>
#include <iostream>
#include <math.h>
#include <vector>
#include <queue>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int t_i = 0; t_i < t; t_i++) {

		long long int n;
		int k;

		cin >> n;
		cin >> k;

		priority_queue<long long int> p;

		p.push(n);

		for (int i = 0; i < k-1; i++) {
			long long int d = p.top();
			p.pop();
			long long int ls;
			long long int rs;
			if (d % 2 == 0) {
				ls = d/2-1;
				rs = d/2;
			} else {
				ls = d/2;
				rs = d/2;
			}
			p.push(ls);
			p.push(rs);
		}
		long long int d = p.top();
		p.pop();
		long long int ls;
		long long int rs;
		if (d % 2 == 0) {
			ls = d/2-1;
			rs = d/2;
		} else {
			ls = d/2;
			rs = d/2;
		}
		

		cout<<"Case #" <<t_i+1<<": "<<rs<<" "<<ls<<endl;
		
	}

}