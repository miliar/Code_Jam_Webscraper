#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
	long long n,m;
	long long a[20]={};
	int k,flag,c,t;
	cin >>t;
	for(int i=1;i<=t; ++i){
		for(int j=0;j<20;j++){
			a[i]=0;
		}
		cin >> n;
		m = n;
		k=0;
		while(1){
			if(m<10){
				a[k]=m;
				break;
			}else{
				a[k]=m%10;
				m = m/10;
				k+=1;
			}
		}
		flag =0;
		c = k;
		for(int j=k-1;j>=0;j--){
			if(a[j]>a[j+1])c=j;
			else if(a[j]<a[j+1]){
				flag = 1;
				break;
			}
		}
		if(flag==0){
			cout << "Case #" << i << ": " << n << endl;
		}else{
			cout << "Case #" << i << ": ";
			if(c==k){
				if(a[k]==1){
					for(int j=0;j<k;j++){
						cout << 9;
					}
				}else{
					cout << a[k]-1;
					for(int j=0;j<k;j++){
						cout << 9;
					}
				}
				cout << endl;
			}else{
				for(int j=k;j>c;j--){
					cout << a[j];
				}
				cout << a[c]-1;
				for(int j=c-1;j>=0;j--){
					cout << 9;
				}
				cout << endl;
			}
		}
	}
	return 0;
}