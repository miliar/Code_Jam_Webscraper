//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<int(n); ++i)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

string P;
int k;

int extra() {
    cin >> P >> k;
    int pocet = 0;
    For(i, P.size() - k + 1) {
        if (P[i] != '+') {
            For(j, k) {
                P[i + j] = (P[i + j] == '+') ? '-' : '+';
            }
            pocet++;
        }
        //cout << P << endl;
    }
    For(i, P.size()) if (P[i] != '+') {
        printf("IMPOSSIBLE\n");
        return 0;
    }
    printf("%d\n", pocet);
}

int main() {
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
