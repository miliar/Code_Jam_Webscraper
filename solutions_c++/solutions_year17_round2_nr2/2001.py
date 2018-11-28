#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
int main() {
	int t,test;
	scanf("%d",&t);
	for(test=1;test<=t;test++){
		int inp[7]={0},i;
		//N 0, R 1, O 2, Y 3, G 4, B 5, and V 6.
		for(i=0;i<7;i++){
			scanf("%d",&inp[i]);
		}
		if(inp[2] > inp[5] || inp[4] > inp[1] || inp[6] > inp[3]){
			printf("Case #%d: IMPOSSIBLE\n",test);
			continue;
		}
		int numB = inp[5] - inp[2];
		int numR = inp[1] - inp[4];
		int numY = inp[3] - inp[6];
		//printf("numB = %d numR = %d numY=%d\n",numB,numR,numY);
		int first = -1;
		if(numB > 0 && numB >= numR && numB >= numY && numB <= numR + numY){
			first = 0;
		}
		if(numR > 0 && numR >= numB && numR >= numY && numR <= numB + numY){
			first = 1;
		}
		if(numY > 0 && numY >= numR && numY >= numB && numY <= numR + numB){
			first = 2;
		}
		if(numB == 0 && inp[3] == 0 && inp[1] == 0){
			first = 0;
		}
		if(numR == 0 && inp[3] == 0 && inp[5] == 0){
			first = 1;
		}
		if(numY == 0 && inp[5] == 0 && inp[1] == 0){
			first = 2;
		}
		if(first == -1){
			printf("Case #%d: IMPOSSIBLE\n",test);
			continue;
		}
		char ans[1005]={0}, str[8]={'z','B','R','V','Y','G','O','z'};
		int last = -1;
		for(i=0;i<inp[0];i++){
			if(i==0){
				ans[i] = str[1<<first];
				if(first == 0){
					inp[5]--;
				}
				else if (first == 1){
					inp[1]--;
				}
				else {
					inp[3]--;
				}
				last = (1<<first);
			}
			else if(last ==1 || last ==2 || last == 4){
				if(last == 1){
					if(inp[2]){
						last = 6;
						ans[i]='O';
						inp[2]--;
						inp[5]--;
					}
					else {
						if(inp[1] > inp[3]){
							ans[i] = 'R';
							inp[1]--;
							last = 2;
						}
						else if (inp[1] == inp[3]){
							if(first == 1){
								ans[i] = 'R';
								inp[1]--;
								last = 2;
							}
							else{
								ans[i] = 'Y';
								inp[3]--;
								last = 4;
							}
						}
						else {
							ans[i] = 'Y';
							inp[3]--;
							last = 4;
						}
					}
				}
				else if(last == 2){
					if(inp[4]){
						last = 5;
						ans[i]='G';
						inp[4]--;
						inp[1]--;
					}
					else {
						if(inp[5] > inp[3]){
							ans[i] = 'B';
							inp[5]--;
							last = 1;
						}
						else if (inp[5] == inp[3]){
							if(first == 1){
								ans[i] = 'B';
								inp[5]--;
								last = 1;
							}
							else{
								ans[i] = 'Y';
								inp[3]--;
								last = 4;
							}
						}
						else {
							ans[i] = 'Y';
							inp[3]--;
							last = 4;
						}
					}
				}
				else {
					if(inp[6]){
						last = 3;
						ans[i]='V';
						inp[6]--;
						inp[3]--;
					}
					else {
						if(inp[1] > inp[5]){
							ans[i] = 'R';
							inp[1]--;
							last = 2;
						}
						else if (inp[1] == inp[5]){
							if(first == 1){
								ans[i] = 'R';
								inp[1]--;
								last = 2;
							}
							else{
								ans[i] = 'B';
								inp[5]--;
								last = 1;
							}
						}
						else {
							ans[i] = 'B';
							inp[5]--;
							last = 1;
						}
					}
				}
			}
			else {
				int x = (7^last);
				ans[i] = str[7^last];
				last = (7^last);
			}
			//printf("i=%d B=%d R=%d Y=%d last=%d\n",i,inp[5],inp[1],inp[3],last);
		}
		ans[inp[0]]=NULL;
		printf("Case #%d: %s\n",test,ans);
	}
	return 0;
}