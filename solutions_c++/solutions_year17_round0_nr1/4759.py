#include <stdio.h>

char palabra[1002];
int size,k,r;

void lee(){
	char c;
	size = 0;
	r = 0;
	c = getchar();
	c = getchar();
	while(c != ' '){
		palabra[size++] = c;
		c = getchar();
	}
	scanf("%d",&k);
}
void proceso(){
	for(int i = 0;i < size -k +1;i++){
		if(palabra[i] != '+'){
			r++;
			for(int j = i;j < i + k;j++){
				if(palabra[j] == '+')
					palabra[j] = '-';
				else
					palabra[j] = '+';
			}
		}
	}
}
void salida(int caso){
	for(int i = 0;i < size;i++){
		if(palabra[i] == '-'){
			printf("Case #%d: IMPOSSIBLE\n",caso);
			return;
		}
	}
	printf("Case #%d: %d\n",caso,r);
}
int main(){
	freopen("in.txt","r",stdin);
	int t;
	scanf("%d",&t);
	for(int i = 1;i <= t;i++){
		lee();
		proceso();
		salida(i);
	}
	return 0;
}
