#include <iostream>
#include <cstdio>
#include <string>
#pragma warning (disable : 4996)
#define MAX_SIZE 10
using namespace std;

int main() {

	int T = 0; scanf("%d", &T); 
	int result = 0;

	for (int testcase = 1; testcase <= T; testcase++) {
		char str[MAX_SIZE + 1]; scanf("%s", str);
		int size = 0; scanf("%d", &size);
		int str_size = 0;

		for (int i = 0; i < MAX_SIZE; i++) {
			if (str[i]) str_size++;
			else break;
		}

		for (int i = 0; i <= str_size - size;i++) {
			if (str[i] == 45) {
				result++;
				for (int j = 0; j < size; j++) {
					if (str[i + j] == 45) str[i + j] = 43;
					else str[i + j] = 45;
				}
			}
		}

		int flag = 1;
		for (int i = str_size - size + 1; i < str_size; i++) {
			if (str[i] == 45) {
				flag = 0;
				break;
			}
		}
		if(flag) printf("Case #%d: %d \n", testcase, result);
		else printf("Case #%d: IMPOSSIBLE \n", testcase);
		result = 0;
	}

	return 0;
}