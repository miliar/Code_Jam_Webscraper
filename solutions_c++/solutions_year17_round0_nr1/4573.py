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
	int n;
	cin >> n;
	REP(i,n){
		int k;
		string t;
		cin >> t >> k;
		int flag = 1;
		int count=0;
		cout << "Case #"<< i+1 << ": "; 
		REP(j,t.length()){
			if(t[j]== '-'){
				if(j+k-1>=t.length()){
					flag = 0;
					break;
				}
				else{
					FOR(l,j,j+k,1){
						if(t[l]=='+'){
							t[l]='-';
						}
						else t[l]='+';
					}
					count++;
				}
			}

		}
		if(flag == 1) cout << count << endl;
		else cout << "IMPOSSIBLE" << endl;
	} 
	return 0;
}