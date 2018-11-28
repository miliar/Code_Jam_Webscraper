#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;
typedef long long ll;

ll N;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC; scanf("%d", &TC);
	for(int t=1; t<=TC; t++) {
		scanf("%lld", &N);
		ll Ans = 0;
		int last = 0;
		for(int i=17; i>=0; i--) {
			for(int p=9; p>=last; p--) {
				ll test = Ans;
				for(int j=i; j>=0; j--) test *= 10, test += p;
				if(test <= N) {
					last = p; 
					break;
				}
			}
			Ans *= 10, Ans += last;
		}

		printf("Case #%d: %lld\n", t, Ans);
	}
	return 0;
}