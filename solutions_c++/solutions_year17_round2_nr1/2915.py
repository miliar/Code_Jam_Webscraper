#include <iostream>
#include <stdio.h>

using namespace std;

double res(){
	int D, n;
	scanf("%d %d", &D, &n);
	int k, s;
	double mx = 0;
	for (int i = 0; i < n; ++i){
		scanf("%d %d", &k, &s);
		mx = max(double(D - k)/double(s), mx);
	}
	return D/mx;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int _case = 1; _case <= T; ++_case)
		printf("Case #%d: %.6f\n", _case, res());
	return 0;
}
