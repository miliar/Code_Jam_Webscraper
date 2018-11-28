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


void flip(char &c){
    c = (c == '+') ? '-' : '+';
}
char ch[1011];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, tcase = 0;
    cin>>t;
    while (t--){
        int n, k;
        scanf("%s%d", ch + 1, &k);
        n = strlen(ch + 1);
        int lastflip = 0, ans = 0;
        for (int i = 1; i + k - 1 <= n; i++){
            if (lastflip == 1)
                flip(ch[i]);
            if (ch[i] == '-'){
                if (lastflip == 1){
                    flip(ch[i + k - 1]);
                    lastflip = 0;
                }
                else{
                    lastflip = 1;
                }
                ch[i] = '+';
                ans++;
            }
            else{
                if (lastflip == 1){
                    flip(ch[i + k - 1]);
                }
            }
        }
        bool Imp = 0;
        for (int i = n - k + 2; i <= n; i++)
            if ((lastflip == 1 && ch[i] == '+') || (lastflip == 0 && ch[i] == '-'))
                Imp = 1;
        printf("Case #%d: ", ++tcase);
        if (Imp) printf("Impossible\n");
        else printf("%d\n", ans);
    }
    return 0;
}
