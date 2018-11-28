#include <stdio.h>
#include <string.h>

char arr[25];
char output[25];
int len;

bool Work(int id, int prev){
	if(id == len) return true;
	
	int digit = arr[id] - '0';
	if(digit < prev) return false;
	
	bool canDo = Work(id+1, digit);
	if(canDo){ 
		output[id] = arr[id];
		return true;
	}
	else if(digit == prev) return false;
	
	output[id] = digit-1 + '0';
	for(int i=id+1; i<len; i++) output[i] = '9';
	return true;
}

int main(){
	int jcase;
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%s", arr);
		len = strlen(arr);
		
		output[len] = 0;
		Work(0, -1);
		
		int leadZero = 0;
		for(int i=0; i<len; i++){
			if(output[i] == '0') leadZero++;
			else break;
		}
		
		printf("Case #%d: %s\n", icase+1, output + leadZero);
	}
	
	return 0;
}
