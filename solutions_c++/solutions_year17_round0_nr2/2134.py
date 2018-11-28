#include<iostream>
#define ull unsigned long long
using namespace std;



ull dig1[20];
ull dig[20];

int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		ull N;
		cin>>N;
		int d=0;
		while(N) {
			dig1[d] = N%10;
			N /=10;
			d++;
		}
		for(int i=0;i<d;i++){
			dig[i] = dig1[d-i-1];
		}
		/*
		   for(int i=0;i<d;i++){
		   cout<<dig[i];
		   }
		   cout<<endl;
		 */
		cout<<"Case #"<<t<<": ";
		int flag =0;
		int i=0;
		for(i=0;i<d-1;i++){
			if(dig[i]>dig[i+1]){
				flag=1;
				break;
			}
		}
		if(flag){
			for(int j=i-1;j>=0;j--){
				if(dig[i]!=dig[j])
					break;
				i--;
			}
			dig[i] -= 1;
			for(int j=i+1;j<d;j++){
				dig[j]=9;
			}
		}
		for(int j=0;j<d;j++){
			if(dig[j]!=0){
				i=j;
				break;
			}
		}
		for(int j=i;j<d;j++){
			cout<<dig[j];
		}
		cout<<endl;
	}
	return 0;
}
