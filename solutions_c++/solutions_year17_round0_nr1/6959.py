#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int minus(char ar[]);

int list[1000];

int main(){
	int t, k;
	char s[1001];
	int i, j, flip, nm, l;

	cin>>t;

	for(i = 0; i < t; i++){
		cin>>s>>k;

		nm = 0;
		flip = 0;

		for(j = 0; j < strlen(s); j++){
			if(s[j] == '-'){
				if(j + k <= strlen(s)){
					for(j = j, l = 0; l < k; l++, j++){
						if(s[j] == '+'){
							s[j] = '-';
						}else{
							s[j] = '+';
						}
					}
					flip++;
					j = 0;
				}
			}
		}

		for(j = 0; j <strlen(s); j++){
			if(s[j] == '-'){
				nm++;
			}
		}

		if(nm == 0){
			printf("Case #%d: %d\n", i + 1, flip);
		}else{
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		}

	}
}

int minus(char ar[]){
	int i;
	int k = 0;
	for(i = 0; i < strlen(ar); i++){
		if(ar[i] == '-'){
			list[k++] = i;
		}
	}
	return k;
}