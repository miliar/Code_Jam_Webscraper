#include <cstdio>
#include <cstdlib>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#define ll long long
#define N 111111
#define md 100000000
#define PI 2*acos(0.0)
using namespace std;

char m[1111];
int k;
void solve(int c){
    int cnt = 0;
    printf("Case #%d: ", c);
    for(int i = 0, j = k - 1; m[j]; i++, j++){
        if(m[i] == '+') continue;
        for(int r = i; r <= j; r++) m[r] = m[r] ^ '+' ^ '-';
        cnt++;
    }
    for(int i = strlen(m) - k; m[i]; i++)
        if(m[i] == '-'){
            printf("IMPOSSIBLE\n");
            return;
        }
    printf("%d\n", cnt);
}

int main(){
    
    int t;
    scanf("%d", &t);
    for(int s = 1; s <= t; s++){
        scanf("%s%d", &m, &k);
        solve(s);
    }
    
    return 0;
}
