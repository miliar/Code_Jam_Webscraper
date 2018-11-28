#include <tchar.h>

#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

unsigned long long int getBiggestTidyNr(unsigned long long int nr);
unsigned long long int getReverseNr(unsigned long long int nr);
int getNrOfDigits(unsigned long long int nr);
unsigned long long int myPow(int nr, int power);

int main(int argc, _TCHAR* argv[])
{
	int T,it;
    unsigned long long int nr,tidy;
    int j;
    
	// nr = 111111111111111110ULL;
	// printf("unsigned long long int max: \n%llu\n", ULLONG_MAX);
	
    FILE *in,*out;
    // in=fopen("input.txt","r");
    // out=fopen("output.txt","w");
    in=fopen("B-large.in","r");
    out=fopen("B-large.out","w");

    fscanf(in,"%d",&T);
    for(it=1;it<=T;it++){
        fscanf(in,"%llu",&nr);
        
		tidy = getBiggestTidyNr(nr);
		
        fprintf(out,"Case #%d: %llu\n",it,tidy);

		// cout<<"nr="<<nr<<endl;
		printf("Case #%d: %llu\n",it,tidy);
		
		// cout<<endl;
	}
    fclose(in);
    fclose(out);
    
    //system("pause");
    return 0;
}

unsigned long long int getBiggestTidyNr(unsigned long long int nr){
	unsigned long long int tidy;
	unsigned long long int nrAux;
	int nrOfDigits;
	int i,j,jMax;
	int digit1, digit2;
	unsigned long long int digit1Degree;
	int digit1_v2, digit2_v2;
	

	nrOfDigits = getNrOfDigits(nr);

	if(nrOfDigits<2){
		return nr;
	}

	i = 0;
	tidy = 0;
	while(i<(nrOfDigits-1)){
		digit1Degree = myPow(10,(nrOfDigits-i-1));

		digit1 = (nr/digit1Degree)%10;
		digit2 = (nr/(digit1Degree/10))%10;

		if(digit1>digit2){
			jMax = nrOfDigits-(i+1);
			for(j=0;j<jMax;j++){
				tidy = tidy*10+9;
			}
			
			if(i>0){
				nrAux = (nr/(myPow(10,nrOfDigits-i-1)))-1;
				while(nrAux>0){
					digit2_v2 = nrAux%10;
					digit1_v2 = (nrAux/10)%10;
					if(digit1_v2<=digit2_v2){
						int tidyNrOfDigitsNow = getNrOfDigits(tidy);
						unsigned long long int nrAuxTidyDegree = myPow(10,tidyNrOfDigitsNow); 
						tidy = nrAux*nrAuxTidyDegree+tidy;
						break;
					}
					tidy = tidy*10+9;
					nrAux = (nrAux/10)-1;
					//i--;
				}
			}else{
				if(digit1-1>0){
					tidy = (digit1-1)*myPow(10,nrOfDigits-i-1)+tidy;
				}
			}

			break;
		}

		i++;
	}

	// if(i==(nrOfDigits-1)){
	if(tidy==0){
		return nr;
	}

	return tidy;
}

int getNrOfDigits(unsigned long long nr){
	int result = 0;
	while(nr>0){
		result++;
		nr=nr/10;
	}
	return result;
}

unsigned long long int myPow(int nr, int power){
    unsigned long long int result=1;
    for(int i=0;i<power;i++){
        result=result*nr;
    }
    return result;
}