
#include <iostream>
#include <algorithm>    // std::fill
#include <sstream>
typedef unsigned long long ull;

using namespace std;

char decrementar(char n){
	switch(n){
		case '9':
			return '8';
			break;
		case '8':
			return '7';
			break;
		case '7':
			return '6';
			break;
		case '6':
			return '5';
			break;
		case '5':
			return '4';
			break;
		case '4':
			return '3';
			break;
		case '3':
			return '2';
			break;
		case '2':
			return '1';
			break;
		case '1':
			return '0';
			break;
	}
}

string reparar(string numero){
	int ref = -1;

	for(int i=0; i<numero.length(); i++){
		if(numero[i]-'0'>=ref){
			ref = numero[i] - '0';
		}else{
			fill(numero.begin()+i, numero.end(), '9');
			numero[i-1] = decrementar(numero[i-1]);
		}
	}


	return numero;
}

bool creciente(string numero){
	int ref = -1;

	for(int i=0; i<numero.length(); i++){
		if(numero[i]-'0'>=ref){
			ref = numero[i] - '0';
		}else{
			return false;
		}
	}

	return true;

}


int main() {

    int c;
    cin >> c;

    for(int k=1; k<=c; k++){
        string n;
        cin >> n;

        while(creciente(n) == false){
        	n = reparar(n);
        }

        stringstream ss;
        ss << n;

        ull in;
        ss >> in;

        cout << "Case #" << k << ": " << in << endl;

    }

	return 0;
}
