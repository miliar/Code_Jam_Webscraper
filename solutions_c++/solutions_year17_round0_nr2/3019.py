#include<stdio.h>
#include<string.h>

using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out", "w", stdout);
	int t, l, may, pos;
	char num[25];
	scanf("%d", &t);
	getchar();
	for (int c = 1; c <= t; c++){
		scanf("%s", num);
		getchar();
		l = strlen(num);
		may = 0;
		pos = 0;
		bool ok = true;
		l--;
		for (int i = 0; i<l; i++){
			if (num[i]>may){
				may = num[i];
				pos = i;
			}
			if (num[i]>num[i + 1]){
				ok = false;
				break;
			}
		}
		l++;
		printf("Case #%d: ", c);
		if (ok){
			printf("%s\n", num);
		}
		else{
			for (int i = 0; i<pos; i++){
				printf("%c", num[i]);
			}
			if (num[pos] != '1'){
				printf("%c", num[pos] - 1);
			}
			for (int i = pos + 1; i<l; i++){
				printf("9");
			}
			printf("\n");
		}
	}
	return 0;
}
