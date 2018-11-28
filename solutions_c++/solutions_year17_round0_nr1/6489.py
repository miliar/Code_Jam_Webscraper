//
// Created by Kapil Dolas on 08-04-2017.
//

#include<stdio.h>
#include<iostream>
#include<math.h>
#include<vector>
#include<map>
#include<string>
#include<string.h>
#include<algorithm>
#include<set>
#define PI acos(-1.0)
#define SZ 1007
#define Fi(a,n) for(int i=a;i<n;i++)
#define Fj(a,n) for(int j=a;j<n;j++)
#define Fk(a,n) for(int k=a;k<n;k++)
#define ri(a) scanf("%d",&a)
#define pb push_back
#define mp make_pair
using namespace std;
typedef vector<int> vi;
typedef vector<vi > vii;
typedef long long ll;
typedef vector<ll> vll;

int main() {
    int T, K, S;
    char s[SZ];
    ri(T);
    for(int t=1; t<=T; t++) {
        scanf("%s", s); ri(K);
        S = strlen(s);
        int cnt = 0;
        for(int i=0; i<=S-K; i++) {
            if(s[i]=='-') {
                cnt++;
                Fj(i, i+K) {
                    if(s[j]=='-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        //printf("%s\n", s);
        bool minus = false;
        Fj(0, S) {
            if (s[j] == '-') {
                minus = true;
                break;
            }
        }
        if(minus) {
            printf("Case #%d: IMPOSSIBLE\n", t);
        }else {
            printf("Case #%d: %d\n", t, cnt);
        }
    }
    return 0;
}