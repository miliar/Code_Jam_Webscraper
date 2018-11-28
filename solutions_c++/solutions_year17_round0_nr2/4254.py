#include <cstdio>
#include <cstring>

int t;
char num[20];


int main(){
	scanf("%d", &t);

	for(int i = 0; i < t ; i ++){
		scanf("%s", num);
		int l = strlen(num);

		printf("Case #%d: ", i + 1);

		bool valid = false;
		int end = l;
		while(!valid){
			valid = true;
			char pre = num[0];
			for(int i = 1; i < end; i ++){
				if(pre - '0' > num[i] - '0'){
					num[i-1] = num[i-1] - 1;
					for(int j = i; j < end; j ++){
						num[j] = '9';
					}
					end = i;
					valid = false;
					break;
				}
				pre = num[i];
			}
		}

		for(int i = 0; i < l; i++)  if(num[i] != '0') printf("%c", num[i]);
		printf("\n");
	}
}

