#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
double pi = acos(-1);
	
double add_area(double curr_r, double r){
	if (r > curr_r)
		return pi * r * r - pi * curr_r * curr_r;
	return 0;
}

double side_area(double r, double h){
	return 2 * pi * r * h;
}

int main(){
	int tc, n, k;
	cin >> tc;
	for (int t= 1; t<= tc; t++){
		cin >> n >> k;
		double r, h;
		vector<pair<double, double > > v(n);
		double ans = 0;

		for (int i=0;i<n;i++){
			cin >> r >> h; 
			v[i] = make_pair(r,h);
		}

		double curr_r = 0;
		vector<double> A(n);
		vector<bool> used(n);
			
		while (k--){
			vector<double> A(n);
			for (int i=0;i<n;i++) if (!used[i]){
				r = v[i].first;
				h = v[i].second;
				A[i] = add_area(curr_r, r) + side_area(r, h);
			}

			int index= (max_element(A.begin(), A.end()) - A.begin());
			used[index] = true;
			ans = ans + A[index];
			curr_r = max(curr_r, v[index].first);
		}
		printf("Case #%d: %.9f\n", t, ans);
 	}
	return 0;
}
