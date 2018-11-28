#include <stdio.h>
#include <string.h>

int main() {

	int T;
	scanf("%d", &T);

	for(int i = 0; i < T; i++) {
		char n[20];
		scanf("%s", &n);
		
		int length = strlen(n);

		int index = 0; 
		bool isTidy = true;
		for(int j = 0, k = 1; k < length; j++, k++) {
			if(n[j] < n[k])
				index = k;
			else if(n[j] > n[k]) {
				isTidy = false;
				break;
			}
		}

		printf("Case #%d: ", (i+1));
		if(isTidy) {
			printf("%s\n", n);
		}
		else {
			for(int i = 0;i < index; i++) {
				printf("%c", n[i]);
			}
			if(!(index == 0 && n[index] == '1'))
				printf("%d", (n[index]-'0')-1);
			for(int i = index+1; i < length; i++) {
				printf("9");
			}

			printf("\n");
		}
	}

	return 0;
}