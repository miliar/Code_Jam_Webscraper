#include <stdio.h>
#include <string.h>


bool isTinyNumber(char S[])
{
	if (strlen(S) == 1)
		return true;

	for (int i = 0; i < strlen(S) - 1; i++) {
		if (S[i] > S[i + 1])
			return false;
	}
	return true;
}

void getTinyNumber(char S[], int test_num)
{
	if (isTinyNumber(S))
		return;

	int index;
	for (int i = 0; i < strlen(S) - 1; i++) {
		if (S[i] > S[i + 1]) {
			index = i;
			break;
		}
	}

	while (index > 0) {
		if (S[index] != '0' && S[index] != '1')
			break;

		index--;
	}

	if (index == 0 && S[0] == '1') {
		for (int i = 0; i < strlen(S) - 1; i++)
			S[i] = '9';
		S[strlen(S) - 1] = '\0';
		return;
	}
	else {
		S[index]--;
		for (int i = index + 1; i < strlen(S); i++) {
			S[i] = '9';
		}
	}

	getTinyNumber(S, test_num);
}

char S[50];

int main()
{
	int T;

	FILE *fp = fopen("B-small-attempt0.in", "r");

	scanf("%d", &T);
	//fscanf(fp, "%d", &T);

	for (int w = 0; w < T; w++) {
		
		scanf("%s", S);
		//fscanf(fp, "%s", S);

		if (strlen(S) == 1) {
			printf("Case #%d: %s\n", w + 1, S);
			continue;
		}

		getTinyNumber(S, w);
		printf("Case #%d: %s\n", w + 1, S);
	}

	return 0;
}