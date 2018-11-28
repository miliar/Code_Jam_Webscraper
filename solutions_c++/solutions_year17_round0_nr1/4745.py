#include<stdio.h>
#include<stdlib.h>
#include<vector>

using namespace std;


const int MAXS = 1005;


// quero deixar tudo com 1;
int main () {
	int t, k, size, limit, case_count, answer;
	bool imposible;
	vector <int> string;
	vector <int> operations;
	char c;
	
	scanf("%d", &t);
	
	case_count = 0;
	
	while (t--) {
		case_count++;
		string.clear();
		operations.clear();
		for (int i=0; ; i++) {
			scanf("%c", &c);
			operations.push_back(0);
			if (c == '-') string.push_back(false);
			else if (c == '+') string.push_back(true);
			else if (c == ' ') break;
			
		}
		scanf("%d", &k);
		size = string.size();
		limit = size-k;
		
//for (int i=0; i<size; i++) printf("%d", string[i]);
//printf("\n");
		
		
		
		
		imposible = false;
		
		for (int i=0; i < limit ; i++) {
			if (string[i] == false) {
				string[i] = !string[i];
				string[i+k] = !string[i+k];
				
				operations[i] = !operations[i];
				operations[i+1] = !operations[i+1];
//for (int i=0; i<size; i++) printf("%d", string[i]);
//printf("\n");
		
//for (int i=0; i<size; i++) printf("%d", operations[i]);
//printf("\n\n");	
			}
			
		}
		
		if (string[limit] == false){
			operations[limit] = !operations[limit];
//printf("###");
		}
		

//printf("limit: %d\n\n", limit);
//for (int i=0; i<size; i++) printf("%d", string[i]);
//printf("\n");
		
//for (int i=0; i<size; i++) printf("%d", operations[i]);
//printf("\n\n");		
		
		
		for (int i=limit+1; i<size; i++) {
			if (string[i] != string[limit]) {
				imposible = true;
			}
		}
		
		if (imposible == true) {
			printf("Case #%d: IMPOSSIBLE\n", case_count);
		} else {
			answer = 0;
			for (int i=0; i<=limit; i++) {
				answer += operations[i];
			}
			printf("Case #%d: %d\n", case_count, answer);
		}
		
	}
	
	return 0;
}
