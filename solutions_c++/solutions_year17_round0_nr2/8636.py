#include <cstdio>  
#include <algorithm>  
#include <cstring>  
using namespace std;
bool isTidy(int n) {
	if ( n < 10) {
		return true;
	} else if (n < 100) {
		int temp = n / 10;
		int temp2 = n % 10;
		return temp <= temp2;
	} else if (n == 1000){
		return false;
	} else {
		int temp = n / 100;
		int temp2 = n / 10 % 10;
		int temp3 = n % 10;
		return temp <= temp2 && temp2 <= temp3;
	}
}
int main() {
	int t, n;
	freopen("B-small-attempt0.in", "r", stdin);
 	freopen("outputB.out", "w", stdout);  
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d", &n);
		for (int j = n; j >=0; j--) {
			if (isTidy(j)) {
				printf("Case #%d: %d\n", i, j);
				break;
			}
		}
	}
    return 0;     
}   