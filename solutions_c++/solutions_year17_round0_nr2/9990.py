#include <stdio.h>
int main(void){
	int T, t;
	FILE *fi=fopen("B-large.in", "r");
	//FILE *fi=fopen("B-small-attempt2.in", "r");
	//FILE *fi=fopen("input.txt", "r");
	FILE *fo=fopen("output.txt", "w");
	fscanf(fi, "%d\n", &T);
	for(t=0; t<T; t++){
		char N[20]="", ans[20]="";
		int len;
		fscanf(fi, "%s\n", N);
		for(len=0; N[len]!=NULL; ++len);

		int i, k=-1;
		for(i=1; i<len; i++){
			if(N[i] < N[i-1]){
				k=i;
				break;
			}
		}
		if (k==-1) {
			for(i=0; i<len; i++)
				ans[i] = N[i];
		} else {
			for(i=k-1; i>0; i--){
				N[i] = ((N[i]=='0' || N[i-1]>(N[i]-1))? '9': N[i]-1);
				if(N[i-1] <= N[i] && N[i]!='9'){
					break;
				}
			}
			if(i==0)
				N[0]--;

			if(N[0]=='0') {
				k=0;
				len--;
			} else {
				for(i=0; i<k; i++)
					ans[i] = N[i];
			}
			for(i=k; i<len; i++)
				ans[i] = '9';
		}
		fprintf(fo, "Case #%d: %s\n", t+1, ans);
	}
	fclose(fi);
	fclose(fo);
	return 0;
}