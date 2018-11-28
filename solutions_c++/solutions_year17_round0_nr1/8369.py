

#include <iostream>
#include <string>
#include <map>
#include <queue>

using namespace std;

string flip(int a, int b, string toflip){
	for(int i=a; i<=b; i++){
		if(toflip[i]=='+'){
			toflip[i] = '-';
		}else{
			toflip[i] = '+';
		}
	}

	return toflip;
}

bool todosmas(string palabra){

	for(int i=0; i<palabra.length(); i++){
		if(palabra[i] == '-')
			return false;
	}

	return true;
}


struct registro{
	string toflip;
	int c;
};

int main() {

	int casos;
	cin >> casos;

	for(int i=1; i<=casos; i++){
		string fila;
		cin >> fila;

		int k;
		cin >> k;

		map <string, bool> mymap;

		queue <registro> cola;
		registro first;
		first.toflip = fila;
		first.c = 0;

		cola.push(first);

		int min = -1;

		while(!cola.empty()){
			registro aux = cola.front();
			cola.pop();

			if(!mymap[aux.toflip]){
				mymap[aux.toflip] = true;

				if(todosmas(aux.toflip) == false){
					for(int i=0; i<aux.toflip.length(); i++){
						int j = i+k-1;
						if(j>=aux.toflip.length())
							break;

						string ntoflip = flip(i, j, aux.toflip);

						registro nuevo;
						nuevo.toflip = ntoflip;
						nuevo.c = aux.c + 1;

						cola.push(nuevo);
					}
				}else{
					min = aux.c;
					break;
				}

			}


		}


		if(min==-1){
	        cout << "Case #" << i << ": IMPOSSIBLE"  << endl;
		}else{
	        cout << "Case #" << i << ": " << min  << endl;
		}



	}

	return 0;
}
