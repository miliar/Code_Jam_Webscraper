#include <cstdio>
#include <cstring>
using namespace std;

char str[1001];
int k;

int main(){
	int cases;
	scanf("%d", &cases);
	
	for(int z=1; z<=cases; z++){
		scanf("%s %d", str, &k);
		
		int flip = 0;
		int i;
		for(i=k-1; str[i] != '\0'; i++){
			if(str[i-k+1] == '-'){
				for(int j=i-k+1; j<=i; j++){
					if(str[j] == '-') str[j] = '+';
					else str[j] = '-';
				}
				flip++;
			}
		}
		bool no = false;
		for(int j=i-k+1; j<i; j++){
			if(str[j] == '-'){
				no = true;
				break;
			}
		}
		if(no){
			printf("Case #%d: IMPOSSIBLE\n", z);
		}else{
			printf("Case #%d: %d\n", z, flip);
		}
	}
	return 0;
}