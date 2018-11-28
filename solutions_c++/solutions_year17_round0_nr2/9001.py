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

int main() {
 	int t;
 	scanf("%d", &t);
 	char num[20];
 	for(int j = 1; j <= t; j++) {
 		printf("Case #%d: ", j);
 		scanf(" %s", num);
 		
 		int sz = strlen(num);
 		bool already = true;
 		for(int i = sz - 1; sz > 1 && i > 0; i--) {
 			if(num[i] < num[i - 1]) {
 				already = false;
 			}
 		}
 		
 		if(already) printf("%s\n", num);
 		else {
 			bool achou = 0;
 			for(int i = 0; i < sz; i++) {
 				if(!achou && num[i] >= num[i + 1]) {
 					num[i]--;
 					if(num[i] == '0') {
 						num[i] = '9';
 						sz--;
 						num[sz] = '\0';
 					}
 					achou = 1;
 				} else if(achou) {
 					num[i] = '9';
 				}
 			}
 			printf("%s\n", num);
 		}
 	}
 		    	
    return 0;
}
