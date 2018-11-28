#include <bits/stdc++.h>
using namespace std;

const int MAXN=1e3+10;
int t, k, tam, resp;
char s[MAXN];
int v[MAXN];

void convert () {
	for (int i=0; i<tam; i++) {
		if (s[i]=='+') v[i]=1;
		else v[i]=0;
	}
}

int main () {
	scanf("%d", &t);
	for (int l=1; l<=t; l++) {
		printf("Case #%d: ", l);
		resp=0;
		scanf(" %s", s);

		scanf("%d", &k);
		tam=strlen(s);
		convert();
		
		for (int i=0; i<tam; i++) {
			if (v[i]==0) {
				if (i+k-1>=tam) {
					resp=-1;
					break;
				}
				
				for (int j=i; j<i+k; j++) {
					v[j]=(v[j]+1)%2;
				}
				resp++;
			}
		}
		if (resp==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n", resp);
	}
}
