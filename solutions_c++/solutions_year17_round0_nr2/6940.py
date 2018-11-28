#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int istidy(char*);

int main(){
	int i, t, j, k;
	char n[19];

	cin>>t;

	for(i = 0; i < t; i++){
		strcpy(n, "");
		cin>>n;
		if(strlen(n) == 1){
			printf("Case #%d: %s\n", i + 1, n);
		}else if(n[0] == '1' && n[1] == '0' && n[2] == '\0'){
			printf("Case #%d: 9\n", i + 1);
		}else{
			while(istidy(n) != 1){
				for(j = 0; j < strlen(n) - 1; j++){
					if(n[j] > n[j + 1]){
						n[j]--;
						for(k = j + 1; k < strlen(n); k++){
							n[k] = '9';
						}
					}
					
				}
			}
			for(j = 0; j < strlen(n) - 1; j++){
				if(n[j] > n[j + 1]){
					n[j]--;
				}
			}

			if(n[0] == '0'){
				for(j = 0; j < strlen(n); j++){
					n[j] = n[j + 1];
				}
			}
			
			printf("Case #%d: %s\n", i + 1, n);
			
		}
	}

	return 0;
}

int istidy(char ar[]){
	int i, flag = 0;

	for(i = 0; i < strlen(ar) - 1; i++){
		if(ar[i] <= ar[i + 1]){
			flag = 1;
		}else{
			flag = 0;
			break;
		}
	}
	return flag;
}