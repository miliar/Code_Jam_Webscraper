#include <stdio.h>

int numero[21];
int size;

void lee(){
	char c;
	size = 0;
	c = getchar();
	while(c != '\n'){
		numero[size++] = (int)(c-'0');
		c = getchar();
	}	
}
void proceso(){
	int j;
	for(int i = size-1;i > 0;i--){
		if(numero[i] == 0 || numero[i] < numero[i-1]){
			for(int c = i;c < size;c++){
				numero[c] = 9;
			}
			numero[i] = 9;
			j = i-1;
			while(numero[j] == 0){
				numero[j--] = 9;
			}
			numero[j]--;
		}
	}
}
void salida(int caso){
	for(int i = 0;i < size;i++){
		if(numero[i] != 0)
			printf("%d",numero[i]);
	}
	printf("\n");
}
int main(){
	freopen("in","r",stdin);
	int t;
	scanf("%d",&t);
	getchar();
	for(int i = 1;i <= t;i++){
		lee();
		proceso();
		printf("Case #%d: ",i);
		salida(i);
	}
	return 0;
}
