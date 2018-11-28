#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
	
	int test,len;
	char num[30];
	scanf("%d",&test);
	for(int i = 0; i < test; i++){
		scanf("%s",&num);
		int index = strlen(num), l=0;
		
		len = strlen(num) ;
		for(int j = len-1; j > 0; j--){
			if(num[j] < num[j-1]){
				num[j-1] = num[j-1]-1;
				num[j] = '9';
				index = j;
			}
		}
		for(int k = index; k < len; k++){
			num[k] = '9';
		}
		if(num[0] == '0')
			 l = 1;
		printf("Case #%d: ",i+1);
		for(int k = l; k < len; k++)
			printf("%c",num[k]);
		
		printf("\n");
		
		
		
	}
	
	
	// your code goes here
	return 0;
}
