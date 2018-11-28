#include<iostream>
#include<algorithm>
#include<string>
#include<sstream>
#include<vector>
#include<set>
#include<iomanip>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<queue>
#include<map>
#include<fstream>
using namespace std;
bool ist(long long n){
	long long l = n % 10;;
	while (n){
		
		if (l < n % 10)
			return 0;
		l = n % 10;
		n /= 10;
	}
	return 1;
}

int main(){
	ifstream fin("B-small-attempt0.in");
	ofstream fout("A.out");

	int t , c = 0;
	fin >> t;
	while (t--){
		long long n;
		fin >> n;
		while (!ist(n)){
			n--;
		}
		fout <<"Case #"<<++c<<": "<< n << endl;
	}

	return 0;
}

