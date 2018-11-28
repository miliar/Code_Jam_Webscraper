#include<stdio.h>
#include<math.h>
#include<string.h>
int main(){
	int t,i,j,ac,aj,s1,e1,s2,e2,tot;
	int cs[15],ce[15],js[15],je[15];
	FILE *f1,*f2;
	f1=fopen("prg211.in","r");
	f2=fopen("prg322.out","w");
	fscanf(f1,"%d\n",&t);
	for(i=0;i<t;i++){
		fprintf(f2,"Case #%d: ",i+1);
		fscanf(f1,"%d %d",&ac,&aj);
		for(j=0;j<ac;j++){
			fscanf(f1,"%d %d",&cs[j],&ce[j]);
		}
		for(j=0;j<aj;j++){
			fscanf(f1,"%d %d",&js[j],&je[j]);
		}
		if((ac == 1 && aj == 1) || (ac + aj) < 2){
			fprintf(f2,"2\n");
		}
		else{
			if(ac == 0){
				s1 = js[0];
				s2 = js[1];
				e1 = je[0];
				e2 = je[1];
			}
			else{
				s1 = cs[0];
				s2 = cs[1];
				e1 = ce[0];
				e2 = ce[1];
			}
			tot = (e1 - s1) + (e2 - s2);
			if( (s1 >= e2 && (s1 - e2) > (720 - tot) && (s2 - e1 + 1440) > (720 - tot)) || (s2 >= e1 && (s2 - e1) > (720 - tot) && (s1 - e2 + 1440) > (720 - tot)) ){
				fprintf(f2,"4\n");
			}
			else{
				fprintf(f2,"2\n");
			}
		}
	}
	return 0;
}
