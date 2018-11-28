#include <cstdio>

char fld[29][29];
int main() {
	int T;
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++) {
		int R,C;
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;i++) scanf("%s",fld[i]);
		//left
		for(int i=0;i<R;i++) for(int j=C-2;j>=0;j--) if(fld[i][j]=='?') fld[i][j]=fld[i][j+1];
		//right
		for(int i=0;i<R;i++) for(int j=1;j<C;j++) if(fld[i][j]=='?') fld[i][j]=fld[i][j-1];
		//down
		for(int j=0;j<C;j++) for(int i=1;i<R;i++) if(fld[i][j]=='?') fld[i][j]=fld[i-1][j];
		//up
		for(int j=0;j<C;j++) for(int i=R-2;i>=0;i--) if(fld[i][j]=='?') fld[i][j]=fld[i+1][j];
		printf("Case #%d:\n",cases);
		for(int i=0;i<R;i++) printf("%s\n",fld[i]);
	}
	return 0;
}
