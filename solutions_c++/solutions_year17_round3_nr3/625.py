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
		
		int n,k;
		double u;
		vector<double> p;
		
		cin>>n>>k;
		cin>>u;
		p.resize(n);
		for (int i = 0; i < n; i++) {
			cin>>p[i];
		}
		
		sort(p.begin(), p.end());
		p.push_back(1.0);
		for (int i = 0; i < n; i++) {
			if (p[i] == p[i+1])
				continue;
			// elso i elemet nezzuk
			double goal = (double)(i+1) * (p[i+1] - p[i]);
			if (u >= goal) {
				//cout << i << "goal: " << goal << endl;
				for (int j = 0; j <= i; j++) {
					p[j] = p[i+1];
				}
				u-=goal;
			}
			else {
				double add = u / (double)(i+1);
				//cout << i << " add: " << add << endl;
				for (int j = 0; j <= i; j++) {
					p[j] += add;
				}
				break;
			}
		}
		
		double res = 1.0;
		for (int i = 0; i < n; i++) {
			res *= p[i];
		}
		
		
		
		printf("Case #%d: %.8lf\n", testc, res);
	}
	return 0;
}


