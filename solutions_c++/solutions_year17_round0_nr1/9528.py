#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int T;//Test case
char pancake[1001];
int dat[1001];
int K;
vector<int> v;

int flip(int len) {
	int f_index = 0;
	int p_value = dat[0];
	int cnt = 0;
	int inval_flag = 0;
	int val_flag = 0;
	for (int i = 0; i < len; i++)
		if (dat[i] != 1)
			val_flag = 1;
	

	while (f_index != len - K+1) {
		if (dat[f_index] == -1) {
			for (int i = 0; i < K; i++)
				dat[f_index + i] = dat[f_index + i] * (-1);
			cnt++;
		}
		else
			f_index++;

	}
	if (val_flag != 0) {
		for (int i = 0; i < len; i++)
			if (dat[i] == -1)
				inval_flag = 1;
		if (inval_flag == 1)
			return -1;

		else
			return cnt;
	}
	else
		return 0;
}

int main(void) {

	FILE *fp;




	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		scanf("%s", pancake);
		scanf("%d", &K);
		for (int i = 0; i < strlen(pancake); i++) {
			if (pancake[i] == '-')
				dat[i] = -1;
			else
				dat[i] = 1;
		}
		v.push_back(flip(strlen(pancake)));
		


		for (int i = 0; i < strlen(pancake); i++)
			dat[i] = 0;
	}

	for (int i = 0; i < T; i++) {
		if (v[i] != -1)
			printf("Case #%d: %d\n", i+1, v[i]);
		else
			printf("Case #%d: IMPOSSIBLE\n", i+1);
	}






	return 0;
}