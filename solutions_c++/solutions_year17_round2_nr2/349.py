#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

// r,y,b / o,g,v
int orig[3] = { 0, }, mix[3] = { 0, };
char print[1005] = { 0, };
void color(int idx, int c){
	if (c == 0){
		print[idx] = 'R';
		orig[0]--;
	}
	else if (c == 1){
		print[idx] = 'Y';
		orig[1]--;
	}
	else{
		print[idx] = 'B';
		orig[2]--;
	}
}

int main(){
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		memset(print, 0, sizeof(print));
		int n;
		scanf("%d", &n);
		
		for (int i = 0; i < 3; i++)
			scanf("%d %d", &orig[i], &mix[i]);

		printf("Case #%d: ", test);
		if (orig[0] == mix[1] && orig[0] + mix[1] == n){
			for (int i = 0; i < orig[0]; i++){
				printf("RG");
			}
			printf("\n");
			continue;
		}
		else if (orig[1] == mix[2] && orig[1] + mix[2] == n){
			for (int i = 0; i < orig[1]; i++){
				printf("YV");
			}
			printf("\n");
			continue;
		}
		else if (orig[2] == mix[0] && orig[2] + mix[0] == n){
			for (int i = 0; i < orig[2]; i++){
				printf("BO");
			}
			printf("\n");
			continue;
		}

		if ((mix[1] !=0 && orig[0] <= mix[1]) || (mix[2] != 0 && orig[1] <= mix[2]) || (mix[0] != 0  && orig[2] <= mix[0])){
			printf("IMPOSSIBLE\n");
			continue;
		}
		orig[0] -= mix[1];
		orig[1] -= mix[2];
		orig[2] -= mix[0];

		int big = max(max(orig[0], orig[1]), orig[2]);
		if (n - big < big){
			printf("IMPOSSIBLE\n");
			continue;
		}

		int len = 0;
		for (len = 0;; len++){
			if (orig[0] + orig[1] + orig[2] == 0) break;
			int big = max(max(orig[0], orig[1]), orig[2]);
			if (orig[0] == big){
				if (len == 0 || print[len - 1] != 'R')
					color(len, 0);
				else if (orig[1] > orig[2])
					color(len, 1);
				else 
					color(len, 2);
			}
			else if (orig[1] == big){
				if (len == 0 || print[len - 1] != 'Y')
					color(len, 1);
				else if (orig[0] > orig[2])
					color(len, 0);
				else
					color(len, 2);
			}
			else{
				if (len == 0 || print[len - 1] != 'B')
					color(len, 2);
				else if (orig[0] > orig[1])
					color(len, 0);
				else
					color(len, 1);
			}
		}

		if (print[0] == print[len - 1]){
			char c = print[len - 1];
			print[len - 1] = print[len - 2];
			print[len - 2] = c;
		}

		bool check[3] = { 0, };
		for (int i = 0; i < len; i++){
			printf("%c", print[i]);
			if (!check[0] && print[i] == 'R'){
				check[0] = 1;
				for (int j = 0; j < mix[1]; j++)
					printf("GR");
			}
			if (!check[1] && print[i] == 'Y'){
				check[1] = 1;
				for (int j = 0; j < mix[2]; j++)
					printf("VY");
			}
			if (!check[2] && print[i] == 'B'){
				check[2] = 1;
				for (int j = 0; j < mix[0]; j++)
					printf("OB");
			}
		}
		printf("\n");
	}
	return 0;
}
