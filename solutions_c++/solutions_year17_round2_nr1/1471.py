#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;


int pos[2000];
int speed[2000];
int D,N;

void testcase(int ncase){
	cout << "Case #" << ncase << ": ";
	int min_sp = 1000000;
	int idx = -1;
	for (int i = 0; i < N; ++i){
		if(min_sp >= speed[i]){
			idx = i;
			min_sp = speed[i];
		}
	}
	double T = ((double)D-pos[idx])/(min_sp);
	// cout << T <<endl;
	double ans = T;
	for (int i = N-1; i > 0 ; --i)
	{	
		int dist = pos[i] - pos[i-1];
		int df = speed[i-1] - speed[i];
		if( df>0 ){
			double t = ((double)dist)/df;
			if(t<=T){
				continue;
			}
			else{
				ans = max(ans, ((double)D-pos[i-1])/speed[i-1]);
			}
		}
		else{
			ans = max(ans, ((double)D-pos[i-1])/speed[i-1]);
		}
	}
	printf("%.6f\n", D/ans);
}

int main(){
	int T;

	cin >> T;
	
	
	for (int cases = 0; cases < T; ++cases)
	{
		cin >> D >> N;
		for (int i = 0; i < N; ++i){	
			cin >> pos[i] >> speed[i];
		}		
		
		testcase(cases+1);
	}

	return 0;
}