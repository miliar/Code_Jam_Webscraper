#include <iostream>

using namespace std;

#define TAMLET 1000005

long long int letrinas[TAMLET];
long long int letrinasDer[TAMLET];
long long int maxRes,minRes;


long long int T,N,K;

void imprime(){
	long long int i,j;
	for(i=0;i<=N+1;i++){
		cout <<letrinas[i];
	}
	cout << endl;
	
}

void calcular(){
	long long int i,j;
	for(i=0;i<TAMLET;i++){
		letrinas[i]=0;
		letrinasDer[i]=-1;	
	}
	
	letrinas[0]=1;
	letrinasDer[0]=N+1;
	
	letrinas[N+1]=1;
	letrinasDer[N+1]=N+1;
	
	long long int mejorIzq,mejorDer,mejorMin,mejorMin2,mejorOri,mejorDest,mejorPos;
	for(i=0;i<K;i++){
		//cout << "Proceso "<<i<<endl;
		
		mejorPos=-1;
		
		//derecha actual
		long long int actDer,actIzq;
		
		for(j=0;j<N+1;j++){
			
			
			
			if(letrinas[j]==1){
				actDer=letrinasDer[j];
				actIzq=j;
				continue;
			}
				long long int posCand,izqCand,derCand,minCand,minCand2;
				long long int origen=actIzq,destino=actDer;
				posCand=j;

				izqCand=posCand-actIzq-1;
				derCand=actDer-posCand-1;
				
				// EL menor
				if(izqCand<derCand){
					minCand=izqCand;
					minCand2=derCand;
				}
				else{
					minCand2=izqCand;
					minCand=derCand;
				}
				
				
				
				//cout <<endl << posCand << " "<<izqCand<<" " <<derCand<<" minCand<< "<<minCand<<" mejorMin "<<mejorMin <<" minCand2 "<<minCand2<<" mejorMin2 "<<mejorMin2 <<endl;
				
				if(mejorPos==-1 || mejorMin<minCand || (minCand==mejorMin && mejorMin2<minCand2)){
					mejorPos=posCand;
					mejorIzq=izqCand;
					mejorDer=derCand;
					mejorMin=minCand;
					mejorMin2=minCand2;
					mejorOri=origen;
					mejorDest=destino;
				}
			
			
		}				
		
		//Actualizamos con el mejor
		
		letrinas[mejorPos]=1;
		letrinasDer[mejorPos]=mejorDest;
		letrinasDer[mejorOri]=mejorPos;
		
		//imprime();
	}
	
	minRes=mejorMin;
	maxRes=mejorMin2;	



	 
}


int main(){
	long long int i,j;
	cin >> T;
	
	for(i=0;i<T;i++){
		cin >> N >> K;
		calcular();
		cout << "Case #"<<(i+1)<<": "<<(maxRes)<<" "<<(minRes)<<endl;
	}
	
		
	return 0;
}
