#include<stdio.h>
#include<math.h>
#include<string.h>
int main(){
	//definitions
	int t,i,j,k,l,r,c,k2,f12;
	char inp[25][25],out[25][25],c1;
	FILE *f1,*f2;
	f1=fopen("rla111.in","r");
	f2=fopen("ra112.out","w");
	fscanf(f1,"%d\n",&t);
	for(i=0;i<t;i++){
		fprintf(f2,"Case #%d: ",i+1);
		fscanf(f1,"%d %d\n",&r,&c);
		for(j=0;j<r;j++){
			for(k=0;k<c;k++){
				fscanf(f1,"%c",&inp[j][k]);
			}
			fscanf(f1,"%c",&c1);
		}
		for(j=0;j<r;j++){
			for(k=0;k<c;k++){
				out[j][k] = inp[j][k];
			}
		}
		for(j=0;j<r;j++){
			l=0;
			for(k=0;k<c;k++){
				if(inp[j][k] != '?'){
					for(k2=l;k2<k;k2++){
						out[j][k2] = inp[j][k];
					}
					l = k+1;
				}
			}
			l=c-1;
			for(k=c-1;k>=0;k--){
					if(inp[j][k] != '?'){
						for(k2=l;k2>k && k2>=0;k2--){
							out[j][k2] = inp[j][k];
						}
						l = k-1;
					}
			}
			f12=1;
			for(k=0;k<c && f12;k++){
				if(out[j][k] =='?'){
					f12 = 0;
				}
			}
			if(f12 == 0){
				for(k=0;k<c;k++){
					if(j>0){
						out[j][k] = out[j-1][k];
					}
				}
			}
		}
		for(j=r-2;j>=0;j--){
				if(out[j][0] == '?'){
					for(k=0;k<c;k++){
						out[j][k] = out[j+1][k];
					}
				}
		}
		fprintf(f2,"\n");
		for(j=0;j<r;j++){
			for(k=0;k<c;k++){
				fprintf(f2,"%c",out[j][k]);
			}
			fprintf(f2,"\n");
		}
	}
	return 0;
}
