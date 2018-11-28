#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef long long ll;

int main(){
	int t;
	scanf("%d",&t);
	for(int co=1;co<=t;co++){
		char data[50];
		scanf("%s",data);
		int len = strlen(data);
		int prev = -1;
		bool flag = false;
		for(int f=0;f<len;f++){
			if(data[f]-'0'<prev){
				flag = true;
				break;
			}
			else prev = data[f]-'0';
		}
		if(!flag){
			printf("Case #%d: %s\n",co,data);
		}
		else{
			int prev = -1;
			bool flag = false;
			for(int f=0;f<len;f++){
				if(flag) data[f] = '9';
				else if(data[f]-'0'<prev){
					flag = true;
					data[f] = '9';
					for(int g=f-1;g>=0;g--){
						data[g]--;
						if(g>0 && data[g]<data[g-1]){
							data[g]='9';
						}
						else break;
					}
				}
				prev = data[f]-'0';
			}
			bool flag2 = false;
			printf("Case #%d: ",co);
			for(int g=0;g<len;g++){
				if(flag2 == false && data[g]=='0') continue;
				else{
					flag2 = true;
					printf("%c",data[g]);
				}
			}
			printf("\n");


		}
	}

}