#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	double final,initial,speed;
	int number, cases;
	vector<double> times;
	double time;
  
	cin >> cases;
	
	for(int i =0; i<cases; i++){
		
		cin >> final >> number;
		for(int j=0;j<number; j++){
			
			cin>> initial >> speed;
		//	speeds.push_back(speed);
		//	locations.push_back(initial);
			time = (final-initial)/speed;
			times.push_back(time);
			
						
		}
		double max = *max_element(times.begin(), times.end());
		double ans = final/max;
	//	cout<<final<<endl<<max<<endl;
		printf("Case #%d: %lf\n", i+1, ans);
		times.clear();
	}
	
	
	
	
	return 0;
	
}
