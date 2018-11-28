#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
int loc[1001], speed[1001],n,d;

int main(){
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		scanf("%d %d", &d, &n);
		for (int i = 0; i < n; i++){
			scanf("%d %d", &loc[i], &speed[i]);
		}

		double max = 0;
		for (int i = 0; i < n; i++){
			if (max<double(1.0)*(d - loc[i]) / speed[i])
				max = double(1.0)*(d - loc[i]) / speed[i];
		}

		printf("Case #%d: %.7lf\n", test,d/max);
	}
	return 0;
}
