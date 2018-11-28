#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
#include "math.h"
using namespace std;

/*
void problemaA(){
	string palabra;
	cin >> palabra;
	vector<int> ascii;
	for (int i = 0; i < palabra.size(); ++i){
		ascii.push_back((int )palabra[i] - (int )'a');
	}

	int res = 0;
	int desde = 0;
	for (int i = 0; i < palabra.size(); ++i){
		res += min(max(ascii[i],desde)-min(ascii[i],desde), 26-max(ascii[i],desde)+min(ascii[i],desde));
		desde = ascii[i];
	}
	cout << res << endl;
	return;
}

void problemaB(){
	int n;
	cin >> n;
	vector<int> dias;
	for (int i = 0; i < n; i++){
		int val;
		cin >> val;
		dias.push_back(val);
	}
	int excedente = 0;
	for (int i = 0; i < n-1; i++){
		excedente = dias[i]%2;
		dias[i+1] -= excedente;
		if (dias[i+1] < 0){
			cout << "NO" << endl;
			return;
		}
	}
	if(dias[n-1]%2 == 1){
		cout << "NO" << endl;
		return;
	}
	cout << "YES" << endl;
	return;
}

/*
void problemaC(){
	int n,m,k;
	cin >> n;
	cin >> m;
	cin >> k;
	vector<int> colores;
	for(int i = 0; i<n; i++){
		int val;
		cin >> val;
		colores.push_back(val);
	}
	vector<int> diasLeft;
	vector<int> diasRight;
	for(int i = 0; i<n; i++){
		int izq,der;
		cin >> izq;
		cin >> der;
		diasLeft.push_back(izq);
		diasRight.push_back(der);
	}

	vector<int> coloresPorDiaIzq;
	vector<int> coloresPorDiaDer;
	for(int i = 0; i<n; i++){
		coloresPorDiaIzq.push_back(colores[diasLeft[i]-1]);
		coloresPorDiaDer.push_back(colores[diasRight[i]-1]);
	}

	int res = 0;

	vector<int> mediasUso(n,0);
	vector<int> mediasConflicto(n,0);
	bool encontreSol = true;
	for(int i = 0; i<n; i++){
		if (coloresPorDiaIzq[i] == coloresPorDiaDer[i]){
			mediasUso[diasLeft[i]-1]++;
			mediasUso[diasRight[i]-1]++;
		} else {
			encontreSol = false;
			mediasConflicto[diasLeft[i]-1]++;
			mediasConflicto[diasRight[i]-1]++;
		}
	}

	if(encontreSol){
		cout << res << endl;
		return;
	}

	int maxConflicto = 0;
	int mediaMaxConflicto = -1;

	for(int i = 0; i<n; i++){
		if (maxConflicto<mediasConflicto[i]){
			maxConflicto = mediasConflicto[i];
			mediaMaxConflicto = i;
		}
	}


}

void problemaD(){
	int n,c;
	cin >> n;
	cin >> c;
	vector< vector<int> > palabras;
	for(int i = 0; i<n; i++){
		int cant;
		cin >> cant;
		vector<int> vec;
		for (int j = 0; j < cant; ++j){
			int val;
			cin >> val;
			vec.push_back(val);
		}
		palabras.push_back(vec);
	}

	//for(int i = 0; i<)
}
*/
void swapPanc(string& p, int i){
	if (p[i]=='-'){
		p[i]='+';
	} else {
		p[i]='-';
	}
}

void problemaA(int t){
	int res = 0;
	bool canDo = true;
	string pancakes;
	int flipper;
	cin >> pancakes;
	cin >> flipper;

	for (int i = 0; i < pancakes.size()-flipper+1; ++i){
		if(pancakes[i] == '-'){
			res++;
			for (int j = i; j < min((int )pancakes.size(),i+flipper); ++j){
				swapPanc(pancakes,j);
			}
		}
	}
	for (int i = pancakes.size()-flipper; i < pancakes.size(); ++i){
		if (pancakes[i] == '-'){
			canDo = false;
			break;
		}
	}

	cout << "Case #" << t << ": ";
	if (canDo){
		cout << res << endl;
	} else {
		cout << "IMPOSSIBLE" << endl;
	}

}
/*
void problemaB(int t){
	long long int input;
	cin >> input;
	int quantityDigits = floor(log10(input))+1;
	vector<int> number(quantityDigits,0);
	vector<int> result(quantityDigits,0);
	long long int res = 0;

	for (int i = 0; i < quantityDigits; ++i){

		number[quantityDigits-1-i] = input%10;
		input = input/10;
	}

	for (int i = 0; i < quantityDigits-1; ++i){
		if (number[quantityDigits-i-1] == 0 || number[quantityDigits-i-1] == -1){
			number[quantityDigits-i-1] = 9;
			number[quantityDigits-i-2]--;
		}
	}



	int i;
	for (i = 0; i < quantityDigits; ++i){
		if (i == quantityDigits-1){
			result[i] = number[i];
			break;
		}
		if (number[i] <= number[i+1]){
			result[i] = number[i];
		} else {
			result[i] = number[i]-1;
			break;
		}
	}

	for (i = i+1; i < quantityDigits; ++i){
		result[i] = 9;
	}

	for (i = 0; i < quantityDigits; ++i){
		long long int d = pow(10,quantityDigits-i-1);
		res += result[i]*d;
	}

	cout << "Case #" << t << ": ";
	cout << res << endl;
}
*/
void volverIgual(vector<int>& n, int index){
	for (int i = index-1; i >= 0; ++i){
		if (i == 0){
			n[i]--;
			break;
		}
		if(n[i] == n[index] && i!=0){
			n[i] = 9;
		} else {
			n[i+1]--;
			break;
		}
		
	}
}
void problemaB(int t){
	long long int input;
	cin >> input;
	int quantityDigits = floor(log10(input))+1;
	vector<int> number(quantityDigits,0);
	vector<int> result(quantityDigits,0);
	long long int res = 0;

	for (int i = 0; i < quantityDigits; ++i){

		number[quantityDigits-1-i] = input%10;
		input = input/10;
	}


	int i;
	for (i = 0; i < quantityDigits; ++i){
		if (i == quantityDigits-1){
			result[i] = number[i];
			break;
		}
		if (number[i] <= number[i+1]){
			result[i] = number[i];
		} else {
			if(i!=0 && number[i] == number[i-1]){
				result[i] = number[i];
				volverIgual(result,i);
				result[i] = 9;
			} else {
				result[i] = number[i]-1;
			}
			
			break;
		}
	}

	for (i = i+1; i < quantityDigits; ++i){
		result[i] = 9;
	}

	for (i = 0; i < quantityDigits; ++i){
		long long int d = pow(10,quantityDigits-i-1);
		res += result[i]*d;
	}

	cout << "Case #" << t << ": ";
	cout << res << endl;
}


void problemaC(int t){
	long long int k,n;
	cin >> n;
	cin >> k;
	long long int res = n+2;
	int sobra = 0;
	long long int hasta = floor(log2(k))+1;
	for (int i = 0; i < hasta; ++i){
		if (i == floor(log2(k))){
			sobra = (res+1)%2;
			res = (res+1)/2;
		} else {
			res = (res+1)/2+(res+1)%2;
		}
	}

	
	//int resMin = floor((float)(res-2)/2);
	long long int resMin = res-2;
	long long int resMax = resMin+sobra;

	cout << "Case #" << t << ": ";
	cout << resMax << " " << resMin << endl;
	
}

int main(){
	int cantTest;
	cin >> cantTest;
	for (int i = 0; i < cantTest; ++i){
		problemaB(i+1);
	}
	

	return 0;
}
