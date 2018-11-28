#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

int su[101];

int main(){
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		int n, p,print=0;
		int mod[5] = { 0, };
		scanf("%d %d", &n,&p);
		for (int i = 0; i < n; i++){
			int a;
			scanf("%d", &a);
			mod[a % p]++;
		}

		int c = 0;
		if (p == 2){
			for (int i = 0; i < mod[0]; i++)
				su[c++] = 0;
			for (int i = 0; i < mod[1]; i++)
				su[c++] = 1;
		}
		else if (p == 3){
			for (int i = 0; i < mod[0]; i++)
				su[c++] = 0;
			if (mod[1] >= mod[2]){
				for (int i = 0; i < mod[2]; i++){
					su[c++] = 2;
					su[c++] = 1;
				}
				for (int i = 0; i < mod[1] - mod[2]; i++){
					su[c++] = 1;
				}
			}
			else{
				for (int i = 0; i < mod[1]; i++){
					su[c++] = 2;
					su[c++] = 1;
				}
				for (int i = 0; i < mod[2] - mod[1]; i++){
					su[c++] = 2;
				}
			}
		}
		else if (p == 4){
			for (int i = 0; i < mod[0]; i++)
				su[c++] = 0;

			for (int i = 0; i < mod[2] / 2; i++){
				su[c++] = 2;
				su[c++] = 2;
			}

			if (mod[1] >= mod[3]){
				for (int i = 0; i < mod[3]; i++){
					su[c++] = 3;
					su[c++] = 1;
				}

				if (mod[2] % 2 == 1)
					su[c++] = 2;
				for (int i = 0; i < mod[1] - mod[3]; i++){
					su[c++] = 1;
				}
			}
			else{
				for (int i = 0; i < mod[1]; i++){
					su[c++] = 3;
					su[c++] = 1;
				}

				if (mod[2] % 2 == 1)
					su[c++] = 2;
				for (int i = 0; i < mod[3] - mod[1]; i++){
					su[c++] = 3;
				}
			}
		}

		int sum = 0;
		for (int i = 0; i < n; i++){
			if (sum == 0)
				print++;
			sum += su[i];
			sum %= p;
		}

		if (c%n != 0)
			printf("-1\n");

		printf("Case #%d: %d\n", test, print);
	}
	return 0;
}
