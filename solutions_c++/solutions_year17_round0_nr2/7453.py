#include<stdio.h>
#include<sstream>
#include<iostream>
#define repn(i,a,b) for(int i=a; i<b; i++)
#define repnr(i,a,b) for(int i=a; i>=b; i--)
using namespace std;

bool increasing ( string num ) {
	repn(i,0,num.size()-1) {
		if ( num[i]>num[i+1] ) return false;
	} return true;
}

int main ( ) {
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-output2.out", "w", stdout);
	
	int qq; scanf("%d", &qq);
	repn(tt,1,qq+1) { 
		string num; 
		cin >> num; 
		
		bool max = false;
		if ( num.size()!=1 && !increasing(num) ) { 
			repn(i,0,num.size()) {
				if ( max ) num[i]='9';
				else if ( num[i]>num[i+1] ) {
					max = true;
					num[i]--;
					if ( i>=1 && num[i-1]>num[i] ) {
						num[i] = '9';
						num[i-1]--;
					}
				}
			}
		}
		
		if ( num[0]=='0' ) num = num.substr(1, num.size()-1);
		printf("Case #%d: %s\n", tt, num.c_str());
	}
}
