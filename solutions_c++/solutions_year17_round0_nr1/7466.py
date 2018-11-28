#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main() {
	int t,k;
	int len, ans;
	char str[1200];
	bool arr[1200];
	scanf("%d", &t);
	for(int test=1; test<=t;test++) {
		ans = 0;
		memset(arr,0, sizeof arr);
		scanf("%s %d",str,&k);
		len = strlen(str);
		//printf("%s  %d",);
		for(int i=0; i<len; i++) {
			if(str[i] == '+') {
				arr[i] = true;
			} else {
				arr[i] = false;
			}
		}
		for(int i=0; i<len && ans!=-1; i++) {
			if(arr[i] == true)  {
				continue;
			} else {
				ans++;
				for(int j=0; j<k; j++) {
					if(i+j >= len) {
						ans = -1;
						break;
					} else {
						arr[i+j] = !arr[i+j];
					}
				}
			}
		}
		if(ans>=0)
			printf("Case #%d: %d\n",test, ans);
		else 
			printf("Case #%d: IMPOSSIBLE\n",test);
		} 
	}
