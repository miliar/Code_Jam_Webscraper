#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <stack>
#include <utility>

using namespace std;
//Global Variable goes here

double ans;
int T;
int num_of_horse, dest;
double slowest = 0;


int main(void){
	cin >> T;
	for(int t = 0; t < T; t++){
		slowest = 0;
		cin >> dest >> num_of_horse;
		for(int q = 0; q < num_of_horse; q++){
			int a, b;
			cin >> a >> b;
			slowest = max(slowest, (double)(dest-a)/b);
		}
		printf("Case #%d: %.6f\n", t+1, dest / slowest);

	}
	return 0;
}