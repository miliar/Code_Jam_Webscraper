#include <cstdio>
#include <cstring>
#define max_t 100
#define max_l 1010

char cake[max_l];
int l;
int flip;
int t;

int main(){
	scanf("%d", &t);
	for(int k = 0; k < t; k ++){
		int count = 0;

		scanf("%s %d", cake, &flip);
		l = strlen(cake);

		for(int i = 0 ; i < (l - flip) + 1 ; i ++){
			if(cake[i] == '-'){
				count ++;
				for(int j = 0; j < flip; j ++){
					int index = i + j;
					if(cake[index] == '-') cake[index] = '+';
					else cake[index] = '-';
				}
			}
		}
		
		bool possible = true;
		for(int i = l-1; i > l - flip; i--){
			if(cake[i] == '-'){
				possible = false;
				break;
			}
		}

		if(possible){
			printf("Case #%d: %d\n", k+1, count);	
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n",k+1);
		}
		
	}
}
