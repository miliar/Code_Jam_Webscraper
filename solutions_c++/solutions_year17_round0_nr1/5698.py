#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <iostream>
#include <vector>
#include <cstring>
#include <stack>
#include <queue>

using namespace std;

char buff[1005];

int main(){
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;test++){
		int k;
		scanf("%s %d", buff, &k);
		int len = strlen(buff);
		int result = 0;
		for(int i=len-1;i>=k-1;i--)
			if(buff[i]=='-'){
				result++;
				for(int j=0;j<k;j++)
					if(buff[i-j]=='-') buff[i-j] = '+';
					else buff[i-j] = '-';
			}
		bool found = true;
		for(int i=0;i<len;i++) if(buff[i]=='-') { found=false; break; }
		printf("Case #%d: ",test);
		
		if(!found) printf("IMPOSSIBLE");
		else printf("%d",result);
		printf("\n");
	}
	return 0;
}