#include <stdio.h>
#include <string.h>

char num[20];
char numcopy[20];
int len;

int isTidy(){
	int prev = 0;
	for(int i = 0; i < len; i++){
		if(prev <= num[i])
			prev = num[i];
		else
		return 0;
	}
	return 1;
}

int isSmaller(){
	for(int i = 0; i < len; i++){
		if(numcopy[i] != num[i]){
			if(numcopy[i] < num[i])
				return 0;
			return 1;
		}
	}
}

int main(){
	
	int T;
	scanf("%d",&T);
	for(int cs = 1; cs <= T; cs++){
		scanf("%s", num);
		len = strlen(num);
		strcpy(numcopy, num);
		for(int i = len - 1; i >= 1; i--){
			if(isTidy() && isSmaller())
				break;
			
			num[i] = '9';
			if(num[i - 1] == '0')
				num[i - 1] = '9';
			else
				num[i - 1] -= 1;
		}		
		char* result = num;
		if(num[0] == '0')
			result++;
		printf("Case #%d: %s\n",cs, result);
	}
	
	return 0;
}
