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
		string t;
		cin >> t;
		cout << "Case #"<< i+1 << ": "; 
		int p =0;
		int flag = 1;
		FOR(i,0,t.length()-1,1){
			if(t[i]>t[i+1]){
				p = i;
				flag = 0;
				break;
			}
		}
		if(flag == 0){
			int x =p;
			char z = t[x];
			while(x>=0){
				if(z == t[x-1])x--;
				else break;
			}
			t[x]=t[x]-1;
			FOR(i,x+1,t.length(),1){
				t[i]='9';
			}
		}
		if(t[0] == '0')cout << t.substr(1,t.length()-1) << endl;
		else cout << t << endl;
	}
	return 0;
}
