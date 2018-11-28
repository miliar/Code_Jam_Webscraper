#include <iostream>
#include <stack>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main(int argc, char *argv[]) {
	freopen("A.in","r",stdin);
	freopen("A-salidaSmall.out","w",stdout);
	int caso=1, cantidad,vueltas, totalSwap=0;
	cin>>cantidad;
	string input;
	bool bandera=true;
	
	

	while(cantidad>0){
		cin>>input>>vueltas;
		stack<int> letras;
		
		for(int i=input.size()-1; i>=0;i--){
			letras.push((int)input.at(i));
		}
		//mientras se pueda seguir swapeando
		while(letras.size()>=vueltas){
			vector<int> auxiliar;
			
			if(letras.top()=='+'){
				letras.pop();
			}else{
				letras.pop();
				//swapeo vueltas-1 pankekes, el top ya lo saque porque queda + seguro.
				//lo pongo en auxiliar
				for(int i=0; i<vueltas-1 ;i++){
					if(letras.top()=='-'){
						auxiliar.push_back('+');
					}else{
						auxiliar.push_back('-');
					}
					letras.pop();
				}
				//de auxiliar a la cola
				for(int i=auxiliar.size()-1; i>=0; i--){
					letras.push(auxiliar.at(i));
				}
				
				totalSwap++;
			}
			
		}
		
		while(!letras.empty()){
			if(letras.top()=='-'){
				bandera=false;
				break;
			}
			letras.pop();
		}
		
		cout<< "Case #" << caso << ": ";
		if(bandera){
			cout<< totalSwap <<endl;
		}else{
			cout<< "IMPOSSIBLE"<<endl;
		}
		
		
		
		
		bandera=true;
		caso++;
		totalSwap=0;
		cantidad--;
	}
	
	
	return 0;
}

