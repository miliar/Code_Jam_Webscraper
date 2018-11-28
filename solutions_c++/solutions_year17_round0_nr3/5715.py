#include <stdio.h>
struct shall {
	int x;
	int ls;
	int rs;
};
shall s[1010];
int max(int i, int j){
	if(i>j) return i;
	else return j;
}
int min(int i, int j){
	if(i<j) return i;
	else return j;
}
void check(int l){
	int i=1;
	while(i<=l){
		int k=i-1, c=0;
		while(s[k].x==0){
			k--;
			c++;
		}
		s[i].ls=c;
		k=i+1, c=0;
		while(s[k].x==0){
			k++;
			c++;
		}
		s[i].rs=c;
		i++;
	}
	
}
int main ()
{
	int i=0, t, n, k, j, p;
	FILE *fp1, *fp2;
	fp1=fopen("C-small-1-attempt0.in", "r");
	fp2=fopen("C.txt", "w");
	fscanf(fp1, "%d", &t);
	while(i<t){
		fscanf(fp1, "%d %d", &n, &k);
		j=0;
		while(j<=n+1){
			if(j==0 || j==n+1) s[j].x=1;
			else{
				s[j].x=0;
			}
			j++;
		}
		check(n);
		j=0;
		while(j<k){
			int r=1;
			p=0;
			while(r<=n){
				if(s[r].x==1);
				else if(min(s[r].ls, s[r].rs)>min(s[p].ls, s[p].rs)) p=r;
				else if(min(s[r].ls, s[r].rs)==min(s[p].ls, s[p].rs)){
					if(max(s[r].ls, s[r].rs)>max(s[p].ls, s[p].rs)) p=r;
				}
				r++;
			}
			s[p].x=1;
			check(n);
			j++;
		}
		j=1;
		fprintf(fp2, "Case #%d: %d %d\n", i+1, max(s[p].ls, s[p].rs), min(s[p].ls, s[p].rs));
		i++;
	}
	fclose(fp1);
	fclose(fp2);
}
