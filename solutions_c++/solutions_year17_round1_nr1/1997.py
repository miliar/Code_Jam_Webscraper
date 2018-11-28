#include<iostream>

char matriz[25][25];
int x, y;

void iniciar(){
	for(int i=0; i<x; i++){
		for(int j=0; j<x; j++){
			matriz[i][j]=0;
		}
	}
}
void imprime(){
		for(int i=0; i<x; i++){
			for(int j=0; j<y; j++){
				std::cout<<matriz[i][j];
			}
			std::cout << '\n';
		}
}

int main(){
	int numCasos, i, j;
	char vacia;
	char letra;
	std::cin >> numCasos;
	for(int caso = 0; caso < numCasos; caso++){
		//paricular
		std::cin >> x >> y;
		//8
		for(i=0; i<x; i++){
			for(j=0; j<y; j++){
				std::cin >> letra;
				matriz[i][j]=letra;
			}
		}
		//fila
		vacia=1;
		for(i=0; i<x && vacia==1; i++){
			for(j=0; j<y && vacia==1; j++){
				if(matriz[i][j]!='?'){
					vacia=0;
					letra=matriz[i][j];
					for(j=0;j<y;j++){
						if(matriz[i][j]=='?'){
							matriz[i][j]=letra;
						} else {
							letra=matriz[i][j];
						}
					}
				}
			}
		}
		//posible salida de matriz
		for(int z=i-2; z>=0; z--){
			for(j=0; j<y; j++){
				matriz[z][j]=matriz[z+1][j];
			}
		}
		for(i=i; i<x; i++){
			vacia=1;
			for(j=0; j<y; j++){
				if(matriz[i][j]!='?'){
					vacia=0;
					letra=matriz[i][j];
					for(j=0;j<y;j++){
						if(matriz[i][j]=='?'){
							matriz[i][j]=letra;
						} else {
							letra=matriz[i][j];
						}
					}
				}
			}
			if(vacia==1){
				for(j=0;j<y;j++){
					matriz[i][j]=matriz[i-1][j];
				}
			}
		}
		
			
		std::cout << "Case #" << caso+1 << ":\n";
		imprime();
	}
}
