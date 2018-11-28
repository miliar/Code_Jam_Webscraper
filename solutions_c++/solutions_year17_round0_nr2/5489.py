#include <stdio.h>
#include <string.h>
char x[100];
int z(int i, int l){
	return x[l-i]-48;
}
int f(int l){
	if(l==1) return 1;
	else if(z(1, l)>=z(2, l)) return f(l-1);
	else return 0;
}
void shift(int l){
	int i=0;
	while(i<l){
		x[i]=x[i+1];
		i++;
	}
}
int m(int l){
	int j=1;
	while(x[l-j]==48){
		x[l-j]=57;
		j++;
	}
	x[l-j]--;
	if(j==l && x[l-j]==48) return 1;
	else if(j>1) return 2;
	else return 0;
}
int main ()
{
	int i=0, n, l;
	FILE *fp1, *fp2;
	fp1=fopen("B-large.in.txt", "r");
	fp2=fopen("B.txt", "w");
	fscanf(fp1, "%d", &n);
	while(i<n){
		fscanf(fp1, "%s", x);
		l=strlen(x);
		int t=l;
		while(t>=1){
			if(f(l)==1) break;
			else{
				int w=m(t);
				if(w==1){
					shift(l);
					l--;
					t=l;
				}
				else if(w==2) t=l;
			}
			while(x[t-1]=='9') t--;
		}
		fprintf(fp2, "Case #%d: %s\n", i+1, x);
		i++;
	}
	fclose(fp1);
	fclose(fp2);
}
