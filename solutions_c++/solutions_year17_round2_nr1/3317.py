#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
#include <string>
using namespace std;



int main() {

	int NumberOfTestCases;
	scanf("%d", &NumberOfTestCases);



	for (int i = 1; i <= NumberOfTestCases; i++) {
		int N, D;
		scanf("%d %d", &D, &N);
		vector<int> pos(N), speed(N);
		int temp_pos, temp_speed;
		for (int j = 0; j < N; j++) {
			scanf("%d %d", &pos[j], &speed[j]);
		}

		double max_speed = DBL_MAX;
		for (int j = 0; j < N; j++)
			max_speed = min(max_speed, D / ((D - pos[j])*1.0)*speed[j]);
		printf("Case #%d: %f\n", i, max_speed);
		
	}
	return 0;
}