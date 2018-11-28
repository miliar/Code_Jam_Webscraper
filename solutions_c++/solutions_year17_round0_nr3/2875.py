#include <cstdlib>
#include <iostream>
#include "set"

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;

	long long N;
	long long K;
	long long N1;
	long long N2;
	long long N3;
	long long N4;
	long long Nn1;
	long long Nn2;
	long long Nn3;
	long long Nn4;
	long long NT;
	long long NnT;
	long long NT2;
	long long NnT2;
	long long NMax;
	int odd;
	long long y;
	long long z;
	
	bool Found;
	
    for (int T_i=0; T_i<T;T_i++){
    	
    	cin >> N >> K;
    	
    	Found = false;
    	N--;
    	K--;
    	
    	odd = N % 2;
    	N2 = (N- odd) /2;
    	N1 = N2 + odd;
    	
    	if (K<=0) {
    		Found = true;
    		y= N1;
    		z= N2;
		}
    	
    	Nn1 = 1;
    	Nn2 = 1;
    	while ((K>0) && (Found==false)) {
    		
    		N3 = 0;
    		Nn3 = 0;
    		N4 = 0;
    		Nn4 = 0;
    		
    		if ((N1>1) || (N2>1)) {
    		if (N1>1){

    			N1 --;
    			odd = N1 % 2;
    			N3 = (N1 - odd)/2;
    			N1 = N3 + odd;
    			Nn3 = Nn1;
    			K -= Nn1;
    			if ((K<=0) && (Found == false)) {
    				Found = true;
					y = N1;
					z = N3;    				
//					cout << "Found 1:"  << y << "-" << z << endl;  				
				}
    			
			}
			if (N2>1){
//				cout << "N2 : " << N2 <<endl;
    			N2 --;
    			odd = N2 % 2;
    			N4 = (N2 - odd)/2;
    			N2 = N4 + odd;
    			Nn4= Nn2;
    			K -= Nn2;
    			if ((K<=0) && (Found == false)) {
    				Found = true;
					y = N2;
					z = N4;   
//					cout << "Found 2:"  << y << "-" << z << endl;  				
				}
			}
			} else {
				Found = true;
				y=0;
				z =0;				
			}
			
//			cout << K << endl;
//			cout << N1 << " - " << Nn1 << endl; 
//			cout << N2 << " - " << Nn2 << endl; 
//			cout << N3 << " - " << Nn3 << endl; 
//			cout << N4 << " - " << Nn4 << endl; 
//			cout << endl;

    		NMax = 0;
			if (NMax< N1) NMax = N1;
			if (NMax< N2) NMax = N2;
			if (NMax< N3) NMax = N3;
			if (NMax< N4) NMax = N4;
			
			NT = NMax;
			NnT = 0;
			if (NMax == N1 ) NnT += Nn1;
			if (NMax == N2 ) NnT += Nn2;
			if (NMax == N3 ) NnT += Nn3;
			if (NMax == N4 ) NnT += Nn4;
			
			NT2 = NMax-1;
			NnT2 = 0;
			if (NMax-1 == N1 ) NnT2 += Nn1;
			if (NMax-1 == N2 ) NnT2 += Nn2;
			if (NMax-1 == N3 ) NnT2 += Nn3;
			if (NMax-1 == N4 ) NnT2 += Nn4;
			
			N1 = NT;
			Nn1 = NnT;
			if (NnT2 > 0 )
 			{
			 N2 = NT2;
			Nn2 = NnT2;
			} else {
				N2=0;
				Nn2 = 0;
				
			} 
		}
    	    	

        cout << "Case #" << T_i+1 << ": " << y << " " << z << endl;
    }
    return EXIT_SUCCESS;
}
