#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <cstdlib>
typedef long long int lld;

using namespace std;

int main() {
	// your code goes here
	lld iterNine(int);
	int T=0,count=0,iter=0,length,vi=0;
	lld number=0,powTen=0,adder=0;
	string allias = " ",allias1=" ";

	scanf("%d",&T);
	while(T--){
		scanf("%lld",&number);
		count++;
		allias1= allias;
		allias = to_string(number);
		length = allias.length();
		iter = 0;
		while(iter<length-1){

			// cout<<"checking"<<allias[iter]<<" and "<<allias[iter+1]<<"\n";
			if(allias.at(iter)<= allias.at(iter+1)){
                // cout<<"checked"<<allias[iter]<<" and "<<allias[iter+1]<<"\n";
				iter++;
			}
			else{
				powTen = pow(10,length-iter-1);
				adder = iterNine(length-iter-1);
				// cout<<"adding"<<((number/powTen) -1)*powTen<<" and "<<adder<<"\n";
				number= ((number/powTen) -1)*powTen + adder;
				allias = to_string(number);
				length = allias.length();
				iter=0;
				
                // cout<<"Number after changes"<<number<<"\n";
                // getchar();
			}

		}
		printf("Case #%d: %lld\n",count,number);
	}
	return 0;
}

lld iterNine(int count){
	lld number = 0,adder=0;
	while(count>0){
		// cout<<"checking at "<<count<<"\n";
		// cout<<"adding "<<9*pow(10,count-1)<<'\n';
		adder = pow(10,count-1);
		number += 9*adder;
		if(number%adder != 0){
		number = number- number%adder;
		}
		// cout<<number<<"\n";

		count--;
	}
	// cout<<"added number"<<number<<"\n";
	if(number%10 == 0) {
			number--;
		}
	return number;
}
