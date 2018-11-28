#include<iostream>
#include<cstdlib>
using namespace std;
void checkOrder(int* n,int size,int t){
	bool tidy = true;
	// for(int i=(size-1);i>=0;i--){
	// 	cout<<n[i];
	// }
	// cout<<"\n";
	for(int i=1;i<size;i++){
		if(n[i] > n[i-1]){
			tidy = false;
			break;
		}
	}
	if(tidy){
		cout<<"Case #"<<t<<": ";
		for(int i=(size-1);i>=0;i--){
			cout<<n[i];
		}
		cout<<"\n";
		return;
	}else{
		for(int i=0;i<size;i++){
			if(n[i]>0){
				n[i]=n[i]-1;
				break;
			}
			else{	
				n[i]=9;
			}
		}
		if(n[size-1]==0){
			size = size -1;
		}
		checkOrder(n,size,t);
	}
};
int main(){
	int T,N;
	cin>>T;
	int k=0;
	while(T-- >0){
		cin>>N;
		int n[4],i=0;
		while(N!=0){
			n[i] = N%10;
			N=N/10;
			i++;
		}
		k++;
		checkOrder(n,i,k);
	}
}