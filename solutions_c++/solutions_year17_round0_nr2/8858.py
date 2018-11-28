#include<iostream>
#include <math.h>
using namespace std;
int main(){
	int T;
	cin>>T;
	freopen("output.txt","w",stdout);
	for(int t=1;t<=T;t++){
		unsigned long long N;
		cin>>N;
		if(N>=10){
			unsigned long long temp = N/10;
			int i = 1;
			int carry = 0;
			while(N/pow(10,i) >=1){
				unsigned long long tt = pow(10,i-1);
				unsigned long long tt1 = pow(10,i);
				unsigned long long tt2 = pow(10,i+1);
				int units = (N%tt1)/tt;
				int tens = (N%tt2)/tt1;
				if(carry==0){
					if(units<tens){
						if(tens!=0){
							N = tt2*(N/tt2) + (tens-1)*tt1 + (tt1-1);
							carry = 0;
						}else{
							carry=1;
							N = tt2*(N/tt2) + (tt2 - 1);
						}
					}
				}else{
					if(tens!=0){
						N = tt2*(N/tt2) + (tens-1)*tt1 + (tt1-1);
						carry = 0;
					}else{
						carry=1;
						N = tt2*(N/tt2) + (tt2 - 1);
					}
				}
				i++;
			}
			if(carry==1){
				N/=10;
			}
		}
		cout<<"Case #"<<t<<": "<<N<<endl;
	}
}