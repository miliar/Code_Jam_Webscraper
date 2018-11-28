#include <bits/stdc++.h>
using namespace std;
#define MAX 1e18
long long int power[100];
int rec(){
	long long int temp = 1,g = 0;
	while(temp < MAX){
		power[g] = temp;
		// cout << "Power of " << g << " " << power[g] << endl;
		temp*=2;g+=1;
	}
	return 0;
}
int main(){
	rec();
	long long int t;
	cin >> t; 
	for(long long int h=1;h<=t;h++){
		int d,x,ind=0,n,k;cin >> n >> k;
		for(int i=0;i<63;i++){
			if(power[i] > k){
				ind = i;
				break;
			}
		}
		x = power[ind - 1];
		d = (n-k)/x;
		cout << "Case #" << h << ": ";
		cout << d/2 + d%2 << " " << d/2 << endl;;
	}
	return 0;
}