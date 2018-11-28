#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

#define ll long 

char A[30][30];

ll findAlongRow(ll i, ll j, ll c) {
	while (j<c) {
		if (A[i][j] != '?') return j;
		j++;
	}
	return -1;
}

void setAlongRow(ll i, ll jst, ll jen, char c) {
	for (;jst<jen;jst++) {
		A[i][jst] = c;
	}
}

ll findAlongColumn(ll j, ll i, ll r) {
	while (i<r) {
		if (A[i][j] != '?') return i;
		i++;
	}
	return -1;
}

void setAlongColumn(ll j, ll ist, ll ien, char c) {
	for (;ist<ien;ist++) {
		A[ist][j] = c;
	}
}

int main() {
	freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-output.out", "w", stdout);
    ll t, r, c, io, i, j, R[30], C[30];
    cin >> t;

    for (io=1;io<=t;io++) {
    	for (i=0;i<30;i++) {
    		R[i] = 0;
    		C[i] = 0;
    	}
    	cout << "Case #" << io << ":" << endl;
    	cin >> r >> c;
    	ll rcount = 0, ccount = 0;
    	for (i=0;i<r;i++) {
    		for (j=0;j<c;j++) {
    			cin >> A[i][j];
    			if (A[i][j] != '?') {
    				if (R[i] == 0) {
    					R[i] = 1; rcount++;
    				}
    				if (C[j] == 0) {
    					C[j] = 1; ccount++;
    				}
    			}
    		}
    	}
//cout<< "r1";
    	if (rcount == r) {
    		for (i=0;i<r;i++) {
    			ll pos = findAlongRow(i, 0, c);
    			j = pos;
    			setAlongRow(i,0,pos,A[i][pos]);
    			while (j<c) {
    				ll pos1 = findAlongRow(i, j+1, c);
    				if (pos1 == -1) {
    					setAlongRow(i, pos+1, c, A[i][pos]);
    					j = c;
    				}
    				else {
    					setAlongRow(i, pos+1, pos1, A[i][pos1]);
    					pos = pos1;
    					j = pos;
    				}
    				//cout<< "r2";
    			}
    		}
    	}

    	else if (ccount == c) {
    		for (j=0;j<c;j++) {
    			ll pos = findAlongColumn(j, 0, r);
    			i = pos;
    			setAlongColumn(j,0,pos,A[pos][j]);
    			while (i<r) {
    				ll pos1 = findAlongColumn(j, i+1, r);
    				if (pos1 == -1) {
    					setAlongColumn(j, pos+1, r, A[pos][j]);
    					i = r;
    				}
    				else {
    					setAlongColumn(j, pos+1, pos1, A[pos1][j]);
    					pos = pos1;
    					i = pos;
    				}

//cout<< "r3";
    			}
    		}
    	}

    	for (i=0;i<r;i++) {
    		for (j=0;j<c;j++) {
    			cout << A[i][j];
    		}
    		cout << endl;
    	}
    }
    return 0;
}