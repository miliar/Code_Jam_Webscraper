#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include <iomanip>  

using namespace std;

bool comp(double a, double b){
	return a > b;
}
double pi = 3.141592653589793;

int main(){
	int tt;
	cin >> tt;
	
	int n, k;
	
	for(int it = 0; it < tt; it ++){		
		cin >> n >> k;
		
		vector<double> r(n);
		vector<double> h(n);
		
		double max = -1.0;
		
		for(int i = 0; i < n; i ++){
			cin >> r[i] >> h[i];
		}
		
		for(int i = 0; i < n; i ++){
			vector<double> q;
			for(int j = 0; j < n; j ++){
				if(j == i)continue;
				q.push_back(r[j] * h[j]);
			}
			double res = pi * (r[i] * r[i]) + 2*pi*r[i]*h[i];
			sort(q.begin(), q.end(), comp);
			for(int j = 0; j < k-1; j ++)res += 2*pi*q[j];
			if(res > max)max = res;
		}
		cout << fixed << setprecision(9) << "Case #" << it + 1 << ": " << max << endl;
		
	}
	return 0;
} 
