#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <time.h>
#include <bits/stdc++.h>


using namespace std;

long long pow(int n , int k){
	if(k == 0)return 1;
	long long 	u = pow(n,k/2);
	if(k %2 == 0) return u*u;
	else return u*u*n;
}

int countdig(long long n){
	int count = 0;
	while(n > 0){
		n /= 10;
		count ++;
	}
	return count;
}


void compute(int t){
	long long n;
	int i,j;
	cin >> n;
	int u = countdig(n);
	int digits[u];
	int newdig[u];
	for(i=u-1;i>=0;i--){
		digits[i] = n % 10;
		n /= 10;
	}

	int m,ind,f,ind2;
		f=0;
		for(j=0;j<u-1;j++){
			if(digits[j] > digits[j+1]){
				f = 1;
				ind = j;
				break;
			}
		}
		if(f){
			ind2 = ind;
			for(i=ind-1;i>=0;i--){
				if(digits[i] == digits[ind])ind2--;
			}
			for(j=0;j<ind2;j++)newdig[j] = digits[j];
			newdig[ind2] = digits[ind2] - 1;
			for(j=ind2+1;j<u;j++)newdig[j] = 9;
		}
		else{
			for(i=0;i<u;i++)newdig[i] = digits[i];
		}
	int flag = 0;
	cout << "Case #" << t << ": ";
	for(i=0;i<u;i++){
		if(newdig[i] > 0){
			cout << newdig[i];
			flag = 1;
		}
		else if(flag) cout << newdig[i];
	}
	cout << endl;
}

int main(){
	int t;
	//cout << countdig(161666719067);
	cin >> t;
	int i;
	for(i=1;i<=t;i++){
		compute(i);
	}
}