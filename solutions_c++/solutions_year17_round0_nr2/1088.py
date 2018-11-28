#include<stdio.h>
#include<math.h>
#include<string.h>
int main(){
	int  t,i,j,k,n,f12,f13;
	char s1[19];
	FILE *f1,*f2;
	f1=fopen("a11.in","r");
	f2=fopen("a22.out","w");
	fscanf(f1,"%d\n",&t);
	for(i=0;i<t;i++){
		fscanf(f1,"%s",s1);
		//fprintf(f2,"%s\n",s1);
		fprintf(f2,"Case #%d: ",i+1);
		n = strlen(s1);
		f12=1;
		while(f12){
			f13 = 1;
			for(j=0;j<n-1 && f13;j++){
				if(s1[j] > s1[j+1]){
					s1[j] = s1[j] - 1;
					for(k=j+1;k<n;k++){
						s1[k] = 57;
					}
					f13 = 0;
				}
			}
			if(f13){
				f12=0;
				for(k=0;k<n;k++){
					if(s1[k]=='0' && k == 0){
						//do nothing
					}
					else{
					 fprintf(f2,"%c",s1[k]);
					}
				}
				fprintf(f2,"\n");
			}
		}
	}
	return 0;
}
