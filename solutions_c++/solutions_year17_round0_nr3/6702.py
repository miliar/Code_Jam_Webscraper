#include <tchar.h>

#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

unsigned long long int getEmplyStallsNr(unsigned long long int N,unsigned long long int K);
int cmpfunc (const void * a, const void * b);

int main(int argc, _TCHAR* argv[])
{
	int T,it;
    unsigned long long int N,K,emptyStalls,max,min;
    
    FILE *in,*out;
    // in=fopen("input.txt","r");
    // out=fopen("output.txt","w");
	in=fopen("C-small-1-attempt0.in","r");
    out=fopen("C-small-1-attempt0.out","w");

    fscanf(in,"%d",&T);
    for(it=1;it<=T;it++){
        fscanf(in,"%llu",&N);
        fscanf(in,"%llu",&K);

		emptyStalls = getEmplyStallsNr(N,K);
		max=emptyStalls/2;
		min=(emptyStalls-1)/2;

        fprintf(out,"Case #%d: %llu %llu\n",it,max,min);
	}
    fclose(in);
    fclose(out);
    
    //system("pause");
    return 0;
}

int cmpfunc (const void * a, const void * b){
	if( *(long long int*)a - *(long long int*)b < 0 ){
		// return -1;
		return 1;
	}
	if( *(long long int*)a - *(long long int*)b > 0 ){
		// return 1;
		return -1;
	}
	if( *(long long int*)a - *(long long int*)b == 0 ){
		return 0;
	}
}

unsigned long long int getEmplyStallsNr(unsigned long long int N,unsigned long long int K){
	unsigned long long int result; 
	// unsigned long long int a[100000];
	unsigned long long int a[1000];
	unsigned long long int i,j;
	
	a[0]=N;
	i=1;
	j=0;
	while(i<N){
		a[i]=a[j]/2;
		i++;
		if(i==N){
			break;
		}
		a[i]=(a[j]-1)/2;
		i++;
		j++;
	}

	qsort(a,N,sizeof(unsigned long long int), cmpfunc);

	result = a[K-1];
	if(result==0){
		result=1;
	}
	
	return result;
}