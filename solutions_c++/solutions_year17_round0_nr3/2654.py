#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
	long long n,k,m,p,x,y;
	int t;
	cin >>t;
	for(int i=1;i<=t; ++i){
		cin >> n >> k;
		m=0;
		p=1;
		while(p<k+1){
			p = 2*p;
			m = m+1;
		}
		p = p/2;
		x = (n-p)/p;
		y = (n-p)%p;
		k = k-p;
		cout << "Case #" << i << ": ";
		if(k<=y){
			if((x+1)%2){
				cout << (x+1)/2 << " "<< (x+1)/2 << endl;
			}else{
				cout << (x+1)/2 << " "<< (x+1)/2-1 << endl;
			}
		}else{
			if(x%2){
				cout << x/2 << " "<< x/2 << endl;
			}else{
				cout << x/2 << " "<< x/2-1 << endl;
			}
		}
	}
	return 0;
}