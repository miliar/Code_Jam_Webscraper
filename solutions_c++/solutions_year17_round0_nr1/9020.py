#include<stdio.h>
#include<string.h>
#include<conio.h>

void turn(char *,int);
bool check(char*);

int main(){
	int t, k, j ,count;
	char s[1000];
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		j = 0;
		count = 0;
		scanf("%s %d", &s,&k);
		while (s[j+k-1] != '\0'){
			if (s[j] == '+'){
			}
			else {
				turn(s + j,k);
				count++;
				//printf("%s\n", s);
			}
			j++;
		}
		if (check(s)){
			printf("case #%d: %d\n", i + 1, count);
		}
		else
			printf("case #%d: IMPOSSIBLE\n", i + 1);
	}
	_getch();
}

void turn(char *str,int k){
	for (int i = 0; i < k; i++){
		if (str[i] == '+'){
			str[i] = '-';
		}
		else{
			str[i] = '+';
		}
	}
	
}

bool check(char* s){
	int i = 0;
	while (s[i] != '\0'){
		if (s[i] == '-')
			return false;
		i++;
	}
	return true;
}