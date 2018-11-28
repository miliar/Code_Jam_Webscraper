#include <iostream>
#include <fstream>

using namespace std  ;

int main (){
	
	ifstream cin("B-small-attempt3.in");
    ofstream cout("output.txt");
	
	int T;
	long  N;
	string Num ;
	cin >> T; 

	for (int i=1 ; i<=T ; i++){
		cin >> N ;	
		while( N != 0 ){
			Num =  to_string(N) ;
            bool tidy = true ;
			for(int j=1 ; j<Num.size() ; j++){
               if(Num[j-1] > Num[j]){
                  tidy = false ; 
                  break;  
               }
			}
			if(tidy){
				cout << "Case #" + to_string(i) + ": " + to_string(N) <<  "\n";
				break ;
			}
            N-=1;
		}
		
	}

	return 0 ;
}