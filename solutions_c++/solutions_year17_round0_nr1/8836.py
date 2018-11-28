#include <bits/stdc++.h>

#define fr(a, b, c) for(int a = b; a < c; ++a)
#define pb push_back
#define MOD 1000000007
#define fi first
#define sec second

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> pll;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef pair<double, double> dd;
typedef vector<int> vi;

char str[1010];

int main() {
 	int t;
 	
 	scanf("%d", &t);
 	
 	for(int i = 1; i <= t; i++) {
 		int k;
 		printf("Case #%d: ", i);
 		scanf(" %s", str);
 		scanf("%d", &k);
 		int sz = strlen(str);
 		
 		int cont = 0;
 		int resp = 0;
 		int s = -1;
 		for(int j = 0; j < sz; j++) {
 			if(str[j] == '-') {
 				cont++;
 				str[j] = '+';
 			} else if(cont && str[j] == '+') {
 				str[j] = '-';
 				if(s == -1) s = j;
 				cont++;
 			}
 			
 			if(cont == k) {
 				cont = 0;
 				if(s != -1) j = s-1;
 				s = -1;
 				resp++;
 			}
 		}
 		bool possible = true;
 		for(int j = 0; j < sz; j++) {
 			if(str[j] != '+') possible = false; 
 		}

 		if(cont || !possible) printf("IMPOSSIBLE\n");
 		else printf("%d\n", resp);
 	}
 		    	
    return 0;
}
