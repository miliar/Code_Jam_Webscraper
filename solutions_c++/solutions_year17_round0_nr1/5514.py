#include <stdio.h>
char s[1010];
int num[1010];
int main ()
{
	int i=0, n, k;
	FILE *fp1, *fp2;
	fp1=fopen("A-large.in", "r");
	fp2=fopen("A.txt", "w");
	fscanf(fp1, "%d", &n);
	while(i<n){
		fscanf(fp1, "%s", s);
		fscanf(fp1, "%d", &k);
		int j=0, p=0;
		while(j<k){
			num[j]=0;
			j++;
		}
		j=0;
		while(s[j]!=NULL){
			if(s[j]=='+') num[p]++;
			if(s[j]=='-') num[p]--;
			j++;
			p++;
			if(p>=k) p=p%k;
		}
		int q=1, x=((j+k-1)/k-num[0])%4, check=0; 
		while(q<k){
			if(q+1<=j%k){
				if(x!=(j/k+1-num[q])%4){
					check=1;
					break;
				}
			}
			else{
				if(x!=(j/k-num[q])%4){
					check=1;
					break;
				}
			}
			q++;
		}
		if(check==1){
			fprintf(fp2, "Case #%d: IMPOSSIBLE\n", i+1);
		}
		else{
			int t=0, count=0;
			while(t<=j-k){
				if(s[t]=='-'){
					int x=0;
					while(x<k){
						if(s[t+x]=='-') s[t+x]='+';
						else if(s[t+x]=='+') s[t+x]='-';
						x++;
					}
					count++;
				}
				t++;
			}
			fprintf(fp2, "Case #%d: %d\n", i+1, count);
		}
		i++;
	}
	fclose(fp1);
	fclose(fp2);
}
