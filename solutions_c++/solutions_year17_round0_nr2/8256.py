#include <bits/stdc++.h>
#define FILE_IN freopen("in", "r", stdin);
#define FILE_OUT freopen("out", "w", stdout);
#define endl "\n"
#define mk make_pair
#define pb push_back
#define fi first
#define se second
#define ii pair<int,int>
#define ll long long
#define For(i,x,y) for(int i=x; i<y; i++)
#define popcount(x) __builtin_popcount(x)
#define popcountll(x) __builtin_popcountll(x)
#define MOD 1000000007
#define PI acos(-1.0)
using namespace std;
const double eps = 1e-9;
#define N 100100

int digitos[22];
ll n;
ll pot[20];

int main () {

    int t;
    int test = 1;
    cin >> t;

    pot[1] = 1;
    for(int i=2;i<=19;i++) {
        pot[i] = pot[i-1] * 10;
    }

    while(t--) {
    
        cin >> n;

        for(int i=1;i<=20;i++) {
            digitos[i] = n % 10;
            n /= 10;
        }

        /*for(int i=1;i<=18;i++) {
            printf("[%d]%d ", i,digitos[i]);
        }
        printf("\n");
*/
        
        
        for(int i=20;i>1;i--) {
  //          printf("[%d] ", i);
            if(digitos[i] > digitos[i-1]) {
                digitos[i] -= 1;
                for(int j=i-1;j>=1;j--) {
                    digitos[j] = 9;
                }
                i += 2;
            }

          /*  for(int j=20;j>=1;j--) {
                printf("%d", digitos[j]);
            }
            printf("\n");
        */}

        ll res = 0;
        for(int i=1;i<=19;i++) {
            res += pot[i] * digitos[i];
        }

        printf("Case #%d: %lld\n",test++, res);

    }

}



