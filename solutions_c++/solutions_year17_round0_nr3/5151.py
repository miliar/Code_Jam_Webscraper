#include <iostream>
#include <cstdio>
#include <sstream>
#include <string>
using namespace std;

int main(){
	freopen("output.txt", "w", stdout);
	freopen("input.in", "r", stdin);
	int t, c = 1;
	long long max, min, k, n;
	scanf("%d", &t);
	while (t--){
		scanf("%lld%lld", &n, &k);
		while (k > 1){
			if ((k - 1) % 2 == 0){
				n = (n - 1) >> 1;
			}
			else{
				n = n >> 1;
			}
			k = k >> 1;
		}
		min = (n - 1) >> 1;
		max = n >> 1;
		printf("Case #%d: %lld %lld\n", c++ ,max, min);
	}
	return 0;
}