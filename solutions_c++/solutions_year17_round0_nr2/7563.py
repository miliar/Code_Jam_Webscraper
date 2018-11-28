
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char pos[] = "0123456789";

void printNext(char *z) {
	int N = strlen(z);
	if (N == 1) {
		printf("%s\n",z);
	} else {
		int idx =-1;
		for (idx =0 ; idx < N-1; ++idx) {
			if (z[idx] > z[idx+1] ) break;
		}

		if (idx == N-1) {
			printf("%s\n",z);
		} else  if (idx >= 0  && idx < N) {
			
			//find first duplicate
			while (idx > 0  && (z[idx] == z[idx -1])) {
					--idx;
			}

			//printf("from %d: %c",idx, z[idx]);
			z[idx] = pos[ z[idx] -pos[0] -1];
			//printf("to %d : %c\n",idx , z[idx]);
			
			for (int  k = idx+1; k < N ; ++k) {
					//printf("from %d : %c",k,z[k]);
					z[k] = pos[9];
				//	printf("to %d: %c\n",k,z[k]);

			}

			for (int i = 0 ; i < N ; ++i) {
				if (i == 0 && z[i] == pos[0]) continue;
				printf("%c",z[i]);
			}
			printf("\n");
			
		}
		
	}

	
}
int main()

{
		int T = 0 ;

		scanf("%d",&T);
		int c = 1;
		while (T--) {
				char in[20] ={0};
				scanf("%s",in);
				//printf("%s\n", in);
				printf("Case #%d: ",c++);
				printNext(in);
		}
		return 0;

}
