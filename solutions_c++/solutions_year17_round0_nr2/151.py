#include <bits/stdc++.h>
using namespace std;

int T, N;
bool no[22];
char S[22];

int main()
{
	for (scanf("%d", &T);T--;){
		static int ts = 0;
		printf("Case #%d: ", ++ts);

		scanf("%s", S+1); N = strlen(S+1);
		if (N == 1){ puts(S+1); continue; }

		for (int i=1;i<=N;i++){
			no[i] = 0;
			for (int j=i;j<=N;j++){
				if (S[j] < S[i]) no[i] = 1;
				if (S[j] != S[i]) break;
			}
		}

		if (no[1] && S[1] == '1'){ for (int i=1;i<N;i++) putchar('9'); puts(""); continue; }
		bool sw = 0;
		for (int i=1;i<=N;i++){
			if (sw) putchar('9');
			else if (no[i]) sw = 1, putchar(S[i]-1);
			else putchar(S[i]);
		} puts("");
	}
}