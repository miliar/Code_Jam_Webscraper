#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int main(int argc, char const *argv[]) {
	int T = 0;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		int K = 0, total = 1e9;
		long long int num = 0;
		scanf("%lld", &num);
		long long int factor = 1, temp = num, smallest_digit = 9;
		while(temp) {
			long long int digit = temp%10;
			temp = temp/10;
			if(digit > smallest_digit) {
				smallest_digit = digit - 1;
				num = ((num/factor) - 1)*factor + (factor - 1);
			} else
				smallest_digit = digit;
			factor = factor*10;
		}
		printf("Case #%d: %lld\n", (t + 1), num);	
	}
	return 0;
}