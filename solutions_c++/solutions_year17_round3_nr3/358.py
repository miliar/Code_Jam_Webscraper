#define Federico using
#define Javier namespace
#define Pousa std;
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>
#include <unordered_map>

Federico Javier Pousa

double Ps[55];
int N, K;

int main(){
	int T;
	cin >> T;
	for(int caso=1; caso<=T; caso++){
		cin >> N >> K;
		double U;
		cin >> U;
		for(int i=0; i<N; i++){
			cin >> Ps[i];
		}
		sort(Ps,Ps+N);
		while(U>1e-6){
			Ps[0] += 0.0001;
			sort(Ps,Ps+N);
			U -= 0.0001;
		}
		double res = 1.0;
		for(int i=0; i<N; i++){
			res *= Ps[i];
		}
		printf("Case #%d: %.6lf\n", caso, res);
	}
	return 0;
}
