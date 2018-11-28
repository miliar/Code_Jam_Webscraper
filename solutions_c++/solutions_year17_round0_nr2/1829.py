#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;
int list[20], ans[20];
long long x;
int main(){
	int T;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	for (int tt = 1;tt <= T;tt++){
		printf("Case #%d: ", tt);
		cin >> x;
		int num = 0;
		for (;x;num++){
			list[num] = x % 10;
			x /= 10;
		}
		int flag = 0;
		for (int i = num - 1;i >= 0;i--){
			for (int j = i - 1;j >= 0;j--){
				if (list[j] < list[i]){
					flag = 1;
					ans[i] = list[i] - 1;
					for (int k = i - 1;k >= 0;k--) ans[k] = 9;
					break;
				}else if (list[j] > list[i]){
					ans[i] = list[i];
					break;
				}
			}
			if (flag) break;
			ans[i] = list[i];
		}
		flag = 0;
		for (int i = num - 1;i >= 0;i--){
			if (flag == 0 && ans[i] == 0) continue;
			flag = 1;
			printf("%d", ans[i]);
		}
		printf("\n");
	}
}
