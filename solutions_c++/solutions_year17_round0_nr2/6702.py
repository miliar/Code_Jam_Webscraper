#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cmath>
#include <iostream>
#define INF (1<<30)
using namespace std;

int main(int argc, char* argv[]){
	int t=0, c=0;
	scanf("%d", &t);
	while(t--){
		char number[20];
		scanf("%s", number);
		for(int k=strlen(number)-2; k>=0; k--){
			if(number[k+1]<number[k]){
				number[k]--;
				for(int i=k+1; i<strlen(number); i++)
					number[i]='9';
			}
		}
		printf("Case #%d: ", ++c);
		bool leading=true;
		for(int i=0; i<strlen(number); i++){
			if(number[i]=='0'&&leading)continue;
			leading=false;
			printf("%c", number[i]);
		}
		printf("\n");
	}
	return 0;
}

