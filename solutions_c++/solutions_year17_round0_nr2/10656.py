#include <stdio.h>
#include <assert.h>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text


FILE *input, *output;

int IsTidy(long N){
	int k = N % 10;
	N /= 10;
	while(N>0){
		if( N % 10 > k) return 0;
		else{
			k= N % 10;
			N/=10;
		}
	}
	return 1;
}


long Esercizio(long N){
	while(N>0)
		if(IsTidy(N)) return N;
		else --N;
}

int main() {
    int Cases,i,K;

    input = fopen("input.txt ", "r");
    output = fopen("output.txt ", "w");
    
    assert(1 == fscanf(input, "%d", &Cases));
    for(i=1;i<=Cases;++i){
    	fscanf(input,"%d",&K);
    	fprintf(output,"Case #%d: %d\n",i,Esercizio(K));
	}    
    
    fclose(input);
    fclose(output);
    return 0;
}
