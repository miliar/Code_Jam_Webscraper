

#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
	int test, flag;
	long int cnt, l, fp,pj;
	char sanid[1005];
	scanf("%d",&test);
	
	for(int i = 0; i < test; i++){
		flag = 0;
		cnt = 0;
		scanf("%s",sanid);
		scanf("%d",&fp);
		l = strlen(sanid);
		for(int j = 0; j < l; j++){
			
			if((sanid[j] == '-') && (j+fp <= l)){
				
				
				for(int k = j; k < j+fp; k++){
					(sanid[k] == '-')?(sanid[k] = '+'):(sanid[k] = '-');
					
				}
				
				cnt++;
				for(int li = j; l < j+fp; li++){
					if(sanid[l]=='-'){
						j=li-1;
						break;
					}
					
					
				}
			}
			
			
			
			
			}
			for(int m = 0; m < l; m++){
				
				
				if(sanid[m] == '-'){
					flag = 1;
					break;
					}			}
				
			(flag)?printf("Case #%d: IMPOSSIBLE\n",i+1):printf("Case #%d: %d\n",i+1,cnt);
				
				
			
		}
	
	return 0;
}

