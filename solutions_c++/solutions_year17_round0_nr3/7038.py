#include <iostream>
#include <stdio.h>
#include <set>

using namespace std;

int main(int argc, char *argv[]) {
	
	int cantCasos, caso = 1;
	
	freopen("C-small.in","r",stdin);
	freopen("C-salidaSmall.out","w",stdout);
	multiset<long long> resultado;
	
	cin >> cantCasos;
	
	while(cantCasos--){
		long long escalones, personas;
		
		cin >> escalones >> personas;
		
		resultado.clear();
		
		for(int i = 0; i < personas-1; i++){
			if(escalones%2 == 0){
				resultado.insert(escalones /2);
				resultado.insert((escalones /2) - 1);
			
			}
			else{
				resultado.insert(escalones /2);
				resultado.insert(escalones /2);
			}
			// escalones = resultado.at(i);
			int j = 0;
			for (std::multiset<long long>::iterator it=resultado.begin(); it!=resultado.end(); ++it){
				if(j == resultado.size()-i-1){
					escalones = *it;
					break;
				}
				else j++;
			}

			//cout << escalones << " " ;
		}
		
		if(escalones%2 == 0){
			cout << "Case #"<<caso<<": "<< escalones /2 << " " <<  escalones /2 - 1 << endl;
		}
		else{
			cout << "Case #"<<caso<<": "<< escalones /2 << " " <<  escalones /2 << endl;
		}
		
		caso++;
	}
	
	return 0;
}

