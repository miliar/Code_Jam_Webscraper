#include <iostream>

using namespace std;

string n;
bool a;

int main(){
	int t,p;
	cin >> t;
	p=t;
	while(t--){
		cin >> n;
		int tam = n.length();

		//si ya puse un 9 entonces no restar 1 a ese nueve
		for (int j = 0 ; j<tam ; j++ ){
			bool a = false;
			for (int i=1 ; i<tam ; i++){
				if (n[i] < n[i-1]){
					if (!a){
						a = true;
						n[i-1]--;
						n[i] = '9';
					}
					else{
						n[i] = '9';
					}
				}
					
			}
		}
		int i;
		for(i=0 ; n[i] <= '0' ; i++){
			//para que no inicie en 0;
		}
		cout << "Case #"<< p-t <<": ";
		for (int j = i; i<tam ; i++){
			cout << n[i];
		}
		cout << endl;
	}
}
		
