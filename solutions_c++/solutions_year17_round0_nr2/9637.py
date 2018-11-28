#include<stdio.h>
#include<string.h>

int main(){
	int T;
	scanf("%d",&T);
	for(int t = 1; t <= T; t++){
		char N[20];
		scanf("%s",N);
		int len = strlen(N);
		int check = 0, always1 = 0;
		for(int i = 1; i < len; i++){
			if (check == 0){
				if (N[i] < N[i-1]){
					/*if (N[i-1] == '1'){
						always1++;
						N[0] = '0';
						for (int j = 1; j < i; j++) N[j] = '9';
					}*/
					check = 1;
					if (always1 == 0) N[i-1]--;
					N[i] = '9';
					
						for (int j = i-1; j >= 0; j--){
							if (N[j] < N[j-1]){
								//printf("///s\n");
								N[j-1]--;
								N[j] = '9';
							}
						}
					
				
				}
			}
			else {
				N[i] = '9';
			}
		}
		if (N[0] != '0') printf("Case #%d: %s\n",t,N);
		else printf("Case #%d: %s\n",t,N+1);
		for (int i = 0; i < len-1; i++){
			if (N[i] > N[i+1]) printf("false\n");
		}
	}
}
