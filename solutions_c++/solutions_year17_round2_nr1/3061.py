#include <iostream>
#include <fstream> 
#include <cstdlib> 
#include <algorithm>
#include <vector>
using namespace std; 

vector< pair<double,double> > info; 
double d,n; 
bool ok(double x){
	double maxval = 0;  
	for (int i = 0; i < info.size(); i++){
		double arrivetime = (d-info[i].first)/info[i].second;  
		maxval = max(maxval,arrivetime); 
	}
	return (d/x >= maxval); 
}

int main(){
	int t;
	cin >> t; 
	for (int test = 1; test <= t; test++){
		info.clear(); 
		cin >> d >> n; 
		for (int i = 0; i < n; i++){
			double k,s; 
			cin >> k >> s; 
			info.push_back(make_pair(k,s)); 
		}
		//sort(info.begin(),info.end()); 
		double l = 0, r = 1e20;  
		for (int it = 0; it < 100; it++){
			double mid = (l+r)/2; 
			if (ok(mid)){
				l = mid; 
			}else{
				r = mid; 
			}
		}
		cout.setf(ios::fixed); 
		cout.setf(ios::showpoint); 
		cout.precision(7); 
		cout << "Case #" << test << ": " << (l+r)/2 << endl;   
	}
	return 0; 
}