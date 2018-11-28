#include <iostream>
#include <cstring>
using namespace std;


char pancake[10000];

long long int N;
long long int K;




long long int esCorrectoPancake()
{
	long long int i;
	long long int tam=strlen(pancake);
	
	for(i=0;i<tam;i++){
		if(pancake[i]=='-'){
			return 0;
		}
	}
	return 1;
}


void flip(long int a,long int b){
	
	long long int i,j;
	
	for(i=a;i<=b;i++){
		if(pancake[i]=='-'){
			pancake[i]='+';
		}
		else{
			pancake[i]='-';		
		}
	}
	
	
}




long long int contarMenos(long int a,long int b){
	
	long long int i,j,res=0;
	
	for(i=a;i<=b;i++){
		if(pancake[i]=='-'){
			res++;
		}
	}
	
	return res;
	
	
}



long long int contarPrimerosMenosSeguidos(long int a,long int b, long long int KComparar){
	
	long long int i,j;
	long long int res=0,pos=-1;
	
	for(i=a;i<=b;i++){
		if(pancake[i]=='-'){
			
			// Guardo la posicion donde empieza le primer grupo de unos
			pos=i;
			// Cuento los - y  cierro el bucle
			for(j=i;j<=b;j++){
				if(pancake[j]=='-'){
					res++;
				}
				else{
					break;
				}
				
			}
			break;
		}
	}
	
	if(res>=KComparar)
		return pos;
	else	
		return -1;
	
}



long long int calcula(){
	long long int i,j;
	long long int tam=strlen(pancake);
	int nOper=0;
	int menosAcum=0;
	
	for(i=0;i<tam;i++){
		//cout << "i " << i << " "<<pancake << endl;
		// Si el tamanyo del final sobrepasa el tamanyo de la cadena, paramos
		if(i+K-1>=tam)
			break;
			
		// Si encuentro K menos, les doy la vuelta y sumo una operacion
		if(pancake[i]=='-'){
			flip(i,i+K-1);
			nOper++;
		}	
	
			
		
	}
	
	// Si es correcto devolvemos cuantas operaciones
	if(esCorrectoPancake()){
		return nOper;
	}
	return -1;
	
	
}


int main(){
	long long int i,j;
	
	cin >> N;
	
	for(i=0;i<N;i++){
		cin >> pancake >> K;
		long long int res=calcula();
		
		if(res==-1){
			cout << "Case #"<<(i+1) <<": IMPOSSIBLE" << endl;
		}else{
			
			cout << "Case #"<<(i+1)<<": "<<res <<endl;			
		}
	}	
	
}
