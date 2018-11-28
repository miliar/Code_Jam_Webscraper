#include <bits/stdc++.h>
using namespace std;

const int N = 30;

char str[N];

int main(){
	int t, tt = 0;
	scanf("%d", &t);
	
	while(t--){
		scanf("%s", str);

		int n = strlen(str);
		int idx = -1;

		for(int i=0; i<n-1; i++){
			if(str[i] > str[i+1]){
				idx = i;
				break;
			}
		}

		// printf("-> %d\n", idx);

		printf("Case #%d: ", ++tt);

		if(idx == -1){
			for(int i=0; i<n; i++)
				printf("%c", str[i]);
		}
		else if(str[idx] == '1'){
			for(int i=0; i<n-1; i++)
				printf("9");
		}
		else{
			
			int id = 0;

			for(int i=idx; i>=0; i--){
				if(str[i] == str[idx])
					id = i;
			}

			for(int i=0; i<id; i++)
				printf("%c", str[i]);

			printf("%c", str[id] - 1);

			for(int i=id+1; i<n; i++)
				printf("9");
		}

		puts("");
	}
}