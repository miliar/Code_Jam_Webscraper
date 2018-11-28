#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <map>
using namespace std;
char su[25] = { 0, };
int main(){
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		int n;
		scanf("%s", su);
		n = strlen(su);
		for (int i = n - 2; i >= 0; i--){
			if (su[i] > su[i + 1]){
				for (int j = i + 1; j < n; j++)
					su[j] = '9';
				su[i]--;
			}
		}
		long long print = _atoi64(su);
		printf("Case #%d: %lld\n", test, print);
	}
	return 0;
}
