/*#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
#include<stdio.h>
#include<string.h>
#include<map>
#include<set>*/

#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define per(i,a,b) for (int i=(b);i>=(a);i--)
#define fi first
#define se second
#define all(x) (x).begin(),(x).end()
#define SZ(x) ((int)x.size())
typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;
//head


char ch[1011], ans[1011];
int n;


bool dfs(int p){
    if (p > n) return 1;
    for (char i = ch[p]; i >= ch[p - 1]; i--){
        ans[p] = i;
        if (i < ch[p]){
            rep(j, p + 1, n)
                ans[j] = '9';
            return 1;
        }
        if (dfs(p + 1)) return 1;
    }
    return 0;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, tcase = 0;
    cin>>t;
    while (t--){
        scanf("%s", ch + 1);
        printf("Case #%d: ", ++tcase);
        n = strlen(ch + 1);
        ch[0] = '1';
        if (dfs(1))
            rep(i, 1, n) printf("%c", ans[i]);
        else
            rep(i, 2, n) printf("9");
        printf("\n");
    }
    return 0;
}
