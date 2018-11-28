#include<stdio.h>
#include<math.h>
#include<string.h>
int main(){
	int  t,i;
	long long int n,k,l,s,ca,cl,cs,t1,ans1,ans2;
	FILE *f1,*f2;
	f1=fopen("c11.in","r");
	f2=fopen("c22.out","w");
	fscanf(f1,"%d\n",&t);
	for(i=0;i<t;i++){
			fscanf(f1,"%lli %lli",&n,&k);
			fprintf(f2,"Case #%d: ",i+1);
			ca=0;
			l=n;
			s=n-1;
			cl=1;
			cs=0;
			ans1=-1;
			while(ca<k && l>0){
				if(l%2 == 0){
				   	l = l/2;
				   	s = l-1;
				   	cs = cl + (cs*2);
				   	ca = ca + cl;
				   	if(k <= ca){
						ans1=l;
						ans2=s;
					}
					else if(k <= ca + ((cs - cl)/2)){
								ans1=s;
								ans2=s;
							}
					ca = ca + ((cs - cl)/2);
				}
				else{
					l = (l-1)/2;
					s = l-1;
					t1 = cs + (cl*2);
					ca = ca + cl;
					if(k<= ca){
						ans1 = l;
						ans2 = l;
					}
					else if(k <= ca + cs){
						ans1 = l;
						ans2 = s;
					}
					//fprintf(f2,"\n extra %d : %lli %lli\n",i,k,ca);
					ca = ca + cs;
					cl =t1;	
				}
			}
			if(ans1 >= 0){
				fprintf(f2,"%lli %lli\n",ans1,ans2);
			}
			else{
				fprintf(f2,"0 0\n");
			}
	}
}
