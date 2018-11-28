#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <iomanip>
#include <stdio.h>
#include <queue>
#include <cmath>

using namespace std;

int main(){
	int q;
	cin >> q;
	for (int z = 0; z < q; z++){
		double d, n;
		cin >> d >> n;
		vector <double> pos;
		vector <double> speed;
		for (int i = 0; i < n; i++){
			double p, s;
			cin >> p >> s;
			pos.push_back(p);
			speed.push_back(s);
		}
		
		double slowest = 0;
		
		for (int i= 0; i < n; i++){
			double t = (d - pos[i])/ speed[i];
			if (t > slowest){
				slowest = t;
			}
		}
		
		double ans = d / slowest;
		cout << "Case #" << z+1 << ": " << setprecision(10) << ans << endl;
	}
}