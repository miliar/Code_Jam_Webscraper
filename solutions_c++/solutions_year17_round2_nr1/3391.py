// Template for Codejam
// use ./a.out < smallQ#.in > smallQ#.txt

#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <cstdlib>
#include <vector>
#include <sstream>
#include <utility> // for pair
#define REP(i,n) for(ll i=0;i<(n);i++)
#define FOR(i,a,b,c) for(int i=a;i<b;i += c)
#define FORd(i,a,b,c) for(int i=a;i>=b;i -=c)
#define vi vector<ll>
#define vii vector<vector<ll> >
#define ll long long int //range -> –9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
#define ui unsigned int // range -> 0 to 4,294,967,295
#define ull unsigned long long
using namespace std;


int main(){
	int t;
	cin >> t;
	REP(i,t){
		int D,N;
		cin >> D >> N;
		int k[N],s[N];
		double max =0;
		REP(j,N){
			cin >> k[j]>>s[j];
			if(((float)(D-k[j])/(float)s[j]) > max) max =((float)(D-k[j])/(float)s[j]); 
		}
		cout << "Case #"<< i+1 << ": "; 
		printf("%f\n",(double)(D/max));
	} 
	return 0;
}