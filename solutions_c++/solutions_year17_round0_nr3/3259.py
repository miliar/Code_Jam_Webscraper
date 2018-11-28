#include <bits/stdc++.h>

using namespace std;

void solvre(){
	long long n, k;
	long long partial, alfa, gama, a, aux, mina, maxa;

	aux = 1;
	cin>>n>>k;
	while(aux<=k){
		aux = 2*aux;
	}
	aux = aux/2;

	n = n - aux + 1;
	a = floor(1.0*n/aux);
	gama = k - (aux - 1);
	alfa = n - a*aux;

	if(alfa >= gama) partial = a;
	else partial = a-1;

	mina = partial/2;
	if(partial%2==0) maxa = mina;
	else maxa = mina+1;
	cout<<maxa<<" "<<mina<<endl;



}

int main(){
	int t;
	cin>>t;
	for(int i = 1; i<=t; i++){
		printf("Case #%d: ", i);
		solvre();
	}

}