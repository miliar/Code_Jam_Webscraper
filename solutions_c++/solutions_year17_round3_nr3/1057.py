#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <utility>
#include <cmath>
#include <numeric>
using namespace std;
int main(){
	int t = 0;
	cin>>t;
	for(int l = 1; l <= t; l++){
		int n = 0, k = 0;
		cin>>n>>k;
		double u = 0;
		cin>>u;	
		vector<double> p(n, 0);
		vector<double> temp(n, 0);
		for(int i = 0; i < n; i++){
			cin>>p[i];
			temp[i] = p[i];
		}
		if(n == k){
			double avg = u;
			for(int i = 0; i < n; i++)
				avg+=p[i];
			avg/=n;
			auto m = max_element(temp.begin(), temp.end());
			double val = *m;
			while(!temp.empty()){
				m = max_element(temp.begin(), temp.end());
				val = *m;
				if(avg < val){
					temp.erase(m);
					avg = (avg*(temp.size()+1) - val)/(temp.size());
				}else
					break;
			}
			for(int i = 0; i < n; i++){
				if(p[i] <= val)
					p[i] = avg;
			}
			double res = 1;
			for(int i = 0; i < n; i++)
				res*=p[i];
			cout<<"Case #"<<l<<": ";
			printf("%.6f\n", res);
		}
	}
	return 0;
}