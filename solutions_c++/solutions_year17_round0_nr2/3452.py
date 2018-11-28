#include<stdio.h>
#include<string.h>
int t, n,idx;
char s[100];

int main()
{
	scanf("%d", &t);
	for (int test = 1; test <= t; test++){
		scanf("%s", s+1);
		s[0] = s[1]-1;
		idx = 0;
		for (int i = 1; s[i]; i++){
			if (s[i] < s[i - 1]){
				idx = i;
				for (int j = i-1; j > 0; j--){
					s[j] = s[j] - 1;
					if (s[j] < s[j - 1]){
						idx = j;
					}
					else break;
				}
				break;
			}
		}
		printf("Case #%d: ", test);
		if (strlen(s) == 2 || !idx){
			for (int i = 1; s[i]; i++)printf("%c", s[i]);
		}
		else{
			int sidx = 1;
			if (s[1] == '0')sidx++;
			for (int i = sidx; i < idx; i++)printf("%c", s[i]);
			for (int i = idx; s[i]; i++)printf("9");
			
		}
		printf("\n");
	}
	return 0;
}