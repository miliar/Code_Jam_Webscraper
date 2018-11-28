#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include <algorithm>

using namespace std;

int main(){
    int T,it;
    int N, K;
	int i;
    
	double trainingUnits;
	
	double p[50];
	double result;
	
    FILE *in,*out;
    // in=fopen("input.txt","r");
    // out=fopen("output.txt","w");
    in=fopen("C-small-1-attempt0.in","r");
    out=fopen("C-small-1-attempt0.out","w");
    
    fscanf(in,"%d",&T);
    for(it=1;it<=T;it++){
        fscanf(in,"%d",&N);
        fscanf(in,"%d",&K);
        fscanf(in,"%lf",&trainingUnits);
        
		for(i=0;i<N;i++){
			fscanf(in,"%lf",&p[i]);
		}
		
		if(N>1){
			sort(p,p+N);
			
			double min, nextMin;
			int nrOfMinAparitions;
			
			while(trainingUnits>0){
				if(trainingUnits<=0){
					break;
				}
				
				min = p[0], nextMin=p[0];
				nrOfMinAparitions = N;
				for(i=1;i<N;i++){
					if(p[i]>min){
						nextMin=p[i];
						nrOfMinAparitions = i;
						break;
					}
				}
				
				double differenceBetweenMinAndNextMin = nextMin-min;
				
				if(nrOfMinAparitions!=N && trainingUnits>=(differenceBetweenMinAndNextMin*nrOfMinAparitions)){
					double addedUnits = differenceBetweenMinAndNextMin/nrOfMinAparitions;
					for(i=0;i<nrOfMinAparitions;i++){
						p[i]+=differenceBetweenMinAndNextMin;
					}
					trainingUnits-=differenceBetweenMinAndNextMin*nrOfMinAparitions;
					
					// printf("1- trainingUnits=%lf, differenceBetweenMinAndNextMin=%lf, nrOfMinAparitions=%d\n", trainingUnits, differenceBetweenMinAndNextMin, nrOfMinAparitions);
					// system("pause");
				}else{
					double addedUnits = trainingUnits/nrOfMinAparitions;
					for(i=0;i<nrOfMinAparitions;i++){
						p[i]+=addedUnits;
					}
					trainingUnits = 0;
					break;
				}
			
			}
			
			result = p[0];
			for(i=1;i<N;i++){
				result = result*p[i];
			}
        }else{
			result = p[0]+trainingUnits;
		}
		
		fprintf(out,"Case #%d: %lf\n",it,result);
    }
    fclose(in);
    fclose(out);
    
    system("pause");
    return 1;
}
