#include <iostream>
#include <fstream>
/*
Voglio conoscere max(L,R) e min(L,R) dell'ultima persona che si siede == la k-esima

ordine di scelta della cabina:
	1)	min(L,R) is maximal
	2)	max(L,R) is maximal
	3)	leftmost stall
*/

void stampaArr(bool* B, const int N){
	for(int i=0; i<N; i++)
		std::cout<<B[i]<<' ';
	std::cout<<'\n';

}

void stampa(const int T,const int m,const int M)
{
	std::cout<<"Case #"<<T <<": " <<M <<' ' <<m <<'\n';
}


int min(const int a, const int b){
	if(a<=b) return a;
	return b;
} //POST: ritorna il minimo tra a,b

int max(const int a, const int b){
	if(a>=b) return a;
	return b;
} //POST: ritorna il massimo tra a,b


int calcL(bool*B,int i,int N){
	int ris=0;
	
	for(int j=-1; i+j>=0 && B[i+j]==false; j--){ //scorri
		ris++; 
		//decrementa finche cella vuota e sono nell'array
		//se sforo o cella piena, esco
	}
	return ris;
}

int calcR(bool*B,int i,int N){
	int ris=0;
	
	for(int j=1; i+j<N && B[i+j]==false; j++){ //scorri
		ris++; 
		//incrementa finche cella vuota e sono nell'array
		//se sforo o cella piena, esco
	}
	return ris;
}

int choose(bool* B, int N, int& m, int& M){
	
	// al primo giro i due val qui sotto vengono sost
	int minLR= -1;
	int maxLR= -1;
	int index=-1;
	
	for(int i=0; i<N; i++){ //scorri array
		int L= calcL(B,i,N); //calcola posti vuoti a sx
		int R= calcR(B,i,N); // a dx
		int cmin= min(L,R); //current min
		int cmax= max(L,R); //current max
		
		if(cmin> minLR && B[i]==false) // (1)
		{
			index=i;
			minLR= cmin;
			maxLR= cmax;
		}
		else
			if(cmin==minLR && B[i]==false)
			{
				if(cmax>maxLR) // (2)
				{
					index=i;
					minLR=cmin;
					maxLR=cmax;
				}
				// (3): In caso di ulteriore parita` si sceglie indice minore. Siccome scorro a sx, non sostituisco-> non fai nulla.
			}
	}//POST: minLR, maxLR, index sono i valori richiesti. In particolare, index e` l'indice dove si segna l'array
	
	m= minLR;
	M= maxLR;
	return index;
	
}// POST: ritorna l'indice, e ha modificato m e M per riferimento.


using namespace std;
main(){
	ifstream IN("input");
	if(IN)
	{
		int T; 	IN>>T;
		for(int c=1; c<=T; c++){
			int N; IN>>N; // N cabine
			int K; IN>>K; // K persone
			bool B[N]= {false}; // array delle cabine
			int index; // dove si siede
			
			for(int i=1; i<=K; i++) // persona i sceglie il posto nell'array
			{
				int m=-1; //min(LR)
				int M=-1; //max(LR)
				index= choose(B,N,m,M); // sceglie indice dell array per la k-esima persona

				B[index]= true; // marca cella array
				if(i==K) //ultimo a sedersi
					stampa(c,m,M);
			}
			
			
		}
		
	} // end IN
}//end main
