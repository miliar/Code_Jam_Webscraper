#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <map>
using namespace std;
char pan[1005] = { 0, };
int main(){
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		int k, n;
		scanf("%s %d", pan, &k);
		n = strlen(pan);
		int print = 0;
		bool flag = 1;
		for (int i = 0; i < n; i++){
			if (pan[i] == '-'){
				for (int j = 0; j < k; j++){
					if (i + j >= n){
						flag = 0;
						break;
					}
					if (pan[i + j] == '-')
						pan[i + j] = '+';
					else
						pan[i + j] = '-';
				}
				print++;
			}
		}
		if (!flag)
			printf("Case #%d: IMPOSSIBLE\n", test);
		else
		printf("Case #%d: %d\n", test, print);
	}
	return 0;
}
