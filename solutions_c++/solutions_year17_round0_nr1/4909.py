#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <sstream>
#include <cstring>
#include <set>
using namespace std;
char str[1003];
int main() {
	int t,k;
	scanf("%d",&t);
	for(int i=1;i<=t;i++) {
		scanf("%s",str);
		scanf("%d",&k);
		int l = strlen(str);
		int temp=0;
		for(int j=0;j<(l-k+1);j++) {
			if(str[j]=='-') {
				for(int m=j;m<(j+k);m++) {
					if(str[m]=='+') {
						str[m]='-';
					} else {
						str[m]='+';
					}
				}
				temp++;
			}
		}
		int flag=1;
		for(int j=l-k;j<(l-1);j++) {
			if(str[j]!=str[j+1]) {
				flag=0;
				break;
			}
		}
		printf("Case #%d: ",i);
		if(flag==0) {
			printf("IMPOSSIBLE\n");
		} else {
			if(str[l-1]=='-') {
				temp++;
			}
			printf("%d\n",temp);
		}
	}
	return 0;
}