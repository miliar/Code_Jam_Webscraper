#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

#define ll long long

string s;

void finals() {
	ll i = 0;
	ll l = s.length();
	for (i=0;i<l;i++) {
		if (s[i]!='0') {
			cout << s[i];
		}
	}
}

void setNine(ll i, ll j) {
	//cout << "again" << i << ":" << j << endl; 
	for (;i<j;i++) {
		s[i]='9';
	}
}

char getSubs(char c) {
	switch (c) {
		case '1': return '0';
		case '2': return '1';
		case '3': return '2';
		case '4': return '3';
		case '5': return '4';
		case '6': return '5';
		case '7': return '6';
		case '8': return '7';
		default : return '8';
	}
}

void calculateAns(ll i, ll j) {
	for (ll k=i;k<j-1;k++) {
		if (s[k]>s[k+1]){
			setNine(k+1,j);
			s[k] = getSubs(s[k]);
			calculateAns(i,k+1);
			return;
		}
	}
}


int main() {
	freopen("B-large.in", "r", stdin);
    freopen("B-large-output.out", "w", stdout);
	ll t;
	cin >> t;//cout << t;
	for (ll is=1;is<=t;is++) {
		cout << "Case #" << is << ": ";
		cin >> s;
		ll l = s.length();
		calculateAns(0,l);
		finals();
		cout << endl;
	}
	return 0;
}