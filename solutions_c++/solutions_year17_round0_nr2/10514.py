#include<iostream>
#include<stdlib.h>
#include<string.h>
using namespace std;

int main(){
	int flag=0;
	int T;
	long long int number[100], N[100];
	
	cin>>T;
	
	for(int i=0; i<T; i++){
		cin>>N[i];
	}

	
for(int i=0; i<T; i++){
	check:	number[i] = N[i];
  			while(number[i] > 0){
				if(number[i]%10 >= (number[i]/10) % 10){
					number[i]=number[i]/10;
					flag=1;
				}
				else{
					flag=0;
					N[i]--;
					goto check;	
				}
			}
	cout<<endl<<"Case #"<<i+1<<": "<<N[i];
}
}
