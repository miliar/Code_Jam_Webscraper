#include <iostream>
#include <string>
using namespace std;

int digits[20];

void print_d(int cant_dig){
	for (int i = cant_dig; i >= 0; i--) cout<<digits[i];
	cout << endl;
}
int descomponer(long long int N){
	int i=0;
	while(N)
	{
    	digits[i++]=N%10;
    	N/=10;
    }
    //print_d(i);
    return i;
}
void limpiarDigits(){
	for (int i = 0; i < 20; ++i) digits[i]=0;
}
void todos_nueves(int desde, int hasta){
	for (int i = desde; i < hasta; i++) digits[i]=9;
}
void resolve(long long int N){
	limpiarDigits();
	//cout << "Descomponer: ";
	int minimo,desde=0,hasta=1;
	int cant_dig = descomponer(N);
	
	//Este queda igual digits[0]
	for (int i = 1; i < cant_dig; i++)
	{
		minimo = min( digits[i], digits[i-1]);
		//Si es mas chico puedo restar y poner 9
		if( minimo < digits[i] ){
			todos_nueves(desde,hasta);
			//print_d(cant_dig);
			desde=i;
			digits[i]-=1;
		}
		hasta++;
	}

	//Escritura final
	//Se puede recomponer o hacer esta chanchada
	int i = cant_dig;
	while(i>=0 && digits[i]==0)	i--;
	while(i>=0) cout<<digits[i--];
	return ;
}

int main(){
	int T;
	long long int N;
	cin>>T;
	for (int i = 0; i < T; i++)
	{
		cin>>N;
		cout<<"Case #"<<i+1<<": ";
		resolve(N);
		cout<<endl;
	}
	return 0;
}