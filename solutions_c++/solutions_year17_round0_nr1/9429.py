#include <stdio.h>
#include <string.h>

char s[10];
int changeChar (char *s, int k);
void checkChange(int index, int k);
bool checkTruth(char *s, int k);

int main(void){

	FILE *pFile = NULL;
	FILE *out = NULL;

	out = fopen("result_large.out", "w");

	pFile = fopen("A-large.in", "r");

	int n;
	fscanf(pFile, "%d\n", &n);

	for(int i = 0; i < n; i++){

		s[0] = '\0';
		int k;

		fscanf(pFile, "%s %d\n", s, &k);

		bool truth = true;
		int count = 0;

		count = changeChar(s, k);
		truth = checkTruth(s, k);

		if(truth == true){
			if(s[0] == '-')
				count ++;
			else;
		}
		else
			count = -1;

		if(count == -1){
			//printf("Case #%d: IMPOSSIBLE\n", i+1);
			fprintf(out, "Case #%d: IMPOSSIBLE\n", (i+1));
		}
		else //printf("Case #%d: %d\n", (i+1), count);
			fprintf(out, "Case #%d: %d\n", (i+1), count);
	}
	fclose(pFile);
	fclose(out);
}

int changeChar (char *s, int k){
	int count = 0;
	for(int i = 0; i < strlen(s) - k; i++){
		switch(s[strlen(s)-i-1]){
		case '+':
			break;
		case '-':
			s[strlen(s)-i-1] = '+';
			checkChange(strlen(s)-i-1, k);
			count++;
			break;
		}
//		printf("%s %d\n",s, count);
	}
	return count;
}

void checkChange(int index, int k){

	for(int i = 1; i < k; i++){
		if(s[index-i] == '+')
			s[index-i] = '-';
		else
			s[index-i] = '+';
	}
}

bool checkTruth(char *s, int k){

	bool truth = true;

	for(int i = 0;i < k-1; i++){

		if(s[i] == s[i+1]);
		else {
			truth = false;
			break;
		}
	}
	return truth;
}