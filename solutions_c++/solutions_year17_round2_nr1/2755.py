#include <bits/stdc++.h>
using namespace std;
int main(){
	int _case;
	scanf("%d", &_case);
	
	for (int casecount = 0; casecount < _case; casecount++) {
		int dest, num;
		scanf("%d%d", &dest, &num);
		double maxtime = 0.0;
		for (int i = 0; i < num; i++) {
			double tmp;
			int speed, start;
			scanf("%d%d", &start, &speed);
			tmp = ((double)(dest-start)) / speed;
			maxtime = max(tmp, maxtime);
		}
		printf("Case #%d: %f\n", casecount+1, dest/maxtime); 
	}
	
	return 0;
}