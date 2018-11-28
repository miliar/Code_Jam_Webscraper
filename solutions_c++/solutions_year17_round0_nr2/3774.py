#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define s second
#define f first
#define mp make_pair

using namespace std;
const int maxn = 1e6+123;
const int mod = 1e9+7;


int a[44];

int main() {
 //	#ifndef ONLINE_JUDGE
 //	freopen("in","r",stdin);
// 	freopen("out","w",stdout);
 //	#endif
 	int tt;
 	cin >> tt;
 	for (int ii = 1, sz; ii <= tt; ii++) {
 		ll n;
 		cin >> n;    
 		sz = 0;
 		while (n) {
 			a[++sz] = n % 10;
 			n /= 10;	
 		}
 //		cerr << sz << endl;
 		for (int i = 2; i <= sz; i++) {
 		 	if (a[i] > a[i-1]) {
 		 		a[i]--;
 		 		for (int j = 1; j < i; j++)
 		 			a[j] = 9; 	
 		 	}
 		}
 		while (!a[sz]) sz--;
 		printf("Case #%d: ", ii);
 		for (int i = sz; i >= 1; i--)
 			cout << a[i];
 		cout << endl;
 	}
 	return 0;
}