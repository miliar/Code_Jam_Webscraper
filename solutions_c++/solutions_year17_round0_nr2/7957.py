#include <bits/stdc++.h>
#define loop(i, a, b) for(i=a; i<b; i++)
#define rev(i, a, b) for(i=a; i>=b; i--)
#define x first
#define y second
#define LIM 100
#define READ(f) freopen(f, "r", stdin);
#define WRITE(f) freopen(f, "w", stdout);
using namespace std;

char cad[LIM];

int main(void){
	int nt, t, i, len, j, k;
	READ("B-large.in");
	WRITE("Bl.out");
	scanf("%d\n", &nt);
	nt++;
	loop(t, 1, nt){
		scanf("%s", cad);
		len=strlen(cad);
		if (len==1){
			printf("Case #%d: %s\n", t, cad);
			continue;
		}
		rev(j, len-2, 0){
			if (cad[j]>cad[j+1]){
				cad[j]--;
				loop(k, j+1, len) cad[k]='9';
			}
		}
		if (cad[0]=='0') 	printf("Case #%d: %s\n", t, cad+1);
		else							printf("Case #%d: %s\n", t, cad);
	}
	return 0;
}
