#include <bits/stdc++.h>
#define loop(i, a, b) for(i=a; i<b; i++)
#define rev(i, a, b) for(i=a; i>=b; i--)
#define x first
#define y second
#define LIM 1005
#define READ(f) freopen(f, "r", stdin);
#define WRITE(f) freopen(f, "w", stdout);
using namespace std;

char cad[LIM];

int main(void){
	int nt, t, i, j, len, k, ans;
	READ("A-large.in");
	WRITE("Al.out");
	scanf("%d\n", &nt);
	nt++;
	loop(t, 1, nt){
		ans=0;
		scanf("%s %d", cad, &k);
		len=strlen(cad);
		loop(i, 0, len-k+1){
      if (cad[i]=='-'){
				ans++;
				loop(j, 0, k) cad[i+j]=(cad[i+j]=='+')?'-':'+';
      }
		}
		//printf("*%s*\n", cad);
		loop(i, 0, len && cad[i]=='+');
		if (i==len) printf("Case #%d: %d\n", t, ans);
		else				printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}
