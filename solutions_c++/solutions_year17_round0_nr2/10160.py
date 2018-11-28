#include <iostream>
#include <fstream>
using namespace std;
/*
controlla se un numero e` ordinato:
PRE: i intero ha almeno una cifra
POST: dice se i e` ordinato
R: per ogni cifra C: se esiste la successiva S, cfr C e S.
	C<=S -> ordinato -> continua il controllo
	C>S -> non ordinato -> return false
	Se completo il controllo, allora tutte le cifre sono ordinate -> return true

*/

void stampa(const int c, const int i){
	cout<<"Case #" <<c <<": " <<i <<endl;
}

int contacifre(int i){
	
	// k== n cifre
	for(int k=1; ; k++){
		i=i/10;
		if(i==0) 
			return k;
	}
}

bool isTidy(int i){

	// estrai cifre dalla meno alla piu significativa
	int a0= 10 ;
	int cifre= contacifre(i);
	for(int j=1, nc=1; nc<=cifre ; j=j*10, nc++){
		int a1= ((i%(j*10))/j);  //estrai cifra di ordine j
		
		// se (a1<=a0) e` tidy, continuo il controllo. Else, 
		if(a1>a0) //not tidy
			return false;
		a0= a1; //scalo cifra
	}
	// se esco dal ciclo con break	, non si e` verificata la cond 'untidy' -> il numero e` tidy -> ret true
	return true;
}

main(){
	ifstream IN("input");
	if(IN)
	{
		int T; 	IN>>T;
		for(int c=1; c<=T; c++){
			int N; IN>>N;  		
			for(int i=N; i>0; i--){
				if( isTidy(i) )
				{
					stampa(c,i);
					break;
				}		
			}
		}
		
	} // end IN
}//end main
