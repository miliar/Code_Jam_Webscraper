//============================================================================
// Name        : CODE.cpp
// Author      : RICHARD
// Version     :
// Copyright   : Your copyright notice
// Description : CODE JAM A in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;
string cambio(string a,int j,int k){
	for(int i=j;i<j+k;i++){
		if (a[i]=='-'){
			a[i]='+';
		}
		else {
			a[i]='-';
		}
	}
	return a;
}

int main() {
	int t , k[100] , l[100] , verdad[100], cont[100];
	string a[100];
	cin >> t;
	for(int i=0;i<t;i++){
		cont[i]=0;
		cin >> a[i] >> k[i];
		l[i]=0;
		int m=0;
		while(a[i][m] != '\0'){
					l[i]++;
					m++;
				}
		l[i]=l[i]-k[i]+1;
		for(int j=0;j<l[i];j++){
			if(a[i][j]=='-'){
				a[i]= cambio(a[i],j,k[i]);
				cont[i]++;
			}
		}
		l[i]=l[i]+k[i]-1;
		verdad[i]=0;
		for(int j=0;j<l[j];j++){
			if(a[i][j]=='+'){
				verdad[i]=2*verdad[i];
			}
			else{
				verdad[i]=-1;
			}
		}
	}
	for(int i=0;i<t;i++){
		if(verdad[i]==0){
			cout << "Case #" << i+1 << ": " << cont[i] << endl;
		}
		else{
			cout << "Case #" << i+1 <<": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}

