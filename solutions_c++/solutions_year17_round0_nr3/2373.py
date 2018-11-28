#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>

using namespace std;

int t;
long long n,k;

void read_input(){
    cin >> t;
    for(int i = 0 ; i  < t ; ++i){
	cin >> n >> k ;

	long long p = 1 ; 

	while(p <= k){
	    p*=2;
	}
	p /= 2;

	n -= p - 1;

	long long size = n / p;
	long long plus = n % p;

	long long pos = k - p + 1;
	
	if(pos <= plus)
	    size++;
	--size;

//	cout << (size+1)/2 << " " << size/2 << endl;
	cout << "Case #" << i+1 << ": " << (size+1)/2 << " " << size/2 << endl;
    }
}

int main(){
    read_input();
    return 0;
}
