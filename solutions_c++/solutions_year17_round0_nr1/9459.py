#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define fi "A-large.in"
#define fo "a.out"
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

void input();
void output(int r);
bool check();

void input()
{
	int ntest;
	int kFlip;
	char s[1010];
	scanf("%d", &ntest);
	for(int i = 1 ; i <= ntest; i++){
		scanf("%s %d", &s, &kFlip);
		int kq = 0;
		int flag = 0;
		for(int j = 0 ; j < strlen(s) - kFlip + 1 ; j++){
			if(s[j] == '-'){
				for(int k = 0; k < kFlip; k++){
					if(s[j + k] == '-')
						s[j + k] = '+';
					else
						s[j + k] = '-';
				}
				kq++;
			}
		}
		
		for(int j = strlen(s) - kFlip; j < strlen(s); j++)
			if(s[j] == '-'){
				flag = 1;
				break;
			}
		
		printf("Case #%d: ", i);
		
		if(flag == 1){
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", kq);
		}
	}
}

void output(int r)
{
	printf("%d\n",r);
}

int main() {
	
	//freopen(fi,"r",stdin);
	//freopen(fo,"w",stdout);
	
	input();
	
	return 0;
}
