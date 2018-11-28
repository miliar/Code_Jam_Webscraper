#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
	int test, flag, count, len, flip,pos;
	char panc[1005];
	scanf("%d",&test);
	
	for(int i = 0; i < test; i++){
		flag = 0;
		count = 0;
		scanf("%s",panc);
		scanf("%d",&flip);
		len = strlen(panc);
		for(int j = 0; j < len; j++){
			
			if((panc[j] == '-') && (j+flip <= len)){
				
				
				for(int k = j; k < j+flip; k++){
					(panc[k] == '-')?(panc[k] = '+'):(panc[k] = '-');
					
				}
				
				count++;
				for(int l = j; l < j+flip; l++){
					if(panc[l]=='-'){
						j=l-1;
						break;
					}
					
					
				}
			}
			
			
			
			
			}
			for(int m = 0; m < len; m++){
				
				//printf("%c",panc[m]);
				if(panc[m] == '-'){
					flag = 1;
					break;
					}			}
				
			(flag)?printf("Case #%d: IMPOSSIBLE\n",i+1):printf("Case #%d: %d\n",i+1,count);
				
				
			
		}
	//	(flag)?printf("IMPOSSIBLE"):printf("%d\n",count);
	
	// your code goes here
	return 0;
}
