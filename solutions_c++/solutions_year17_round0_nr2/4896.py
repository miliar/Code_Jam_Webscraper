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
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++) {
		char str[30];
		scanf("%s", str);
		int l = strlen(str);
		printf("Case #%d: ",i);
		if(l<2) {
			printf("%s\n", str);
		} else {
			int x=-1;
			for(int j=1;j<l;j++) {
				if(str[j]<str[j-1]) {
					x=j;
					break;
				}
			}
			if(x==-1) {
				printf("%s\n",str);
				continue;
			}
			int val=x;
			while(x>=1 && str[x]<str[x-1]) {
				str[x]='9';
				if(str[x-1]!='0') {
					str[x-1]--;
				} else if(x!=1) {
					str[x-2]--;
					str[x-1]='9';
				}
				x--;
			}
			for(int j=0;j<=val;j++) {
				if(str[j]=='0') {
					continue;
				}
				printf("%c",str[j]);
			}
			for(int j=val+1;j<l;j++) {
				printf("9");
			}
			printf("\n");
		}
	}
	return 0;
}