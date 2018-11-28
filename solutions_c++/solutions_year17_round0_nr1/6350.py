#include<iostream>
#include<string>

int tortitas, paleta;
std::string pilaFin;
char pila[1000];

void cambiar(int pos){
	for(int i=pos; i<pos+paleta; i++){
		if(pila[i]=='+'){
			pila[i]='-';
		} else {
			pila[i]='+';
		}
	}
}

void iniPila(){
	for(int i=0; i<tortitas; i++){
		pila[i]='+';
	}
}

int main(){
	int casos, cont;
	char bien;
	std::cin >> casos;
	for(int i = 0; i<casos; i++){
		std::cin >> pilaFin >> paleta;
		tortitas = pilaFin.length();
		iniPila();
		cont = 0;
		bien = 1;

		//cambios time
		for(int j = 0; j<=tortitas-paleta; j++){
			if(pila[j]!=pilaFin[j]){
				cont++;
				cambiar(j);
			}
		}

		//comproba time
		for(int j = tortitas-paleta+1; j<tortitas; j++){
			if(pila[j]!=pilaFin[j]){
				std::cout << "Case #" << i+1 << ": IMPOSSIBLE\n";
				bien = 0;
				break;
			}
		}
		if(bien==1){
			std::cout << "Case #" << i+1 << ": " << cont << '\n';
		}
	}
}
