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
typedef pair<int,int> pii;
//head

const int N = 222;
struct slot{
    int l, r, col;
}t[N];
bool cmp(slot a, slot b){
    return a.l < b.l;
}
int n, m;

vector<int>c1, c0;
int c10;
int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, tcase = 0;
    cin>>T;
    while (T--){
        scanf("%d%d", &n, &m);
        int sum0, sum1;
        sum0 = sum1 = 0;
        rep(i, 1, n){
            int l, r;
            scanf("%d%d", &l, &r);

            t[i].l = l; t[i].r = r;
            t[i].col = 0;
            sum0 += t[i].r - t[i].l;
        }
        rep(i, n + 1, n + m){
            int l, r;
            scanf("%d%d", &l, &r);

            t[i].l = l; t[i].r = r;
            t[i].col = 1;
            sum1 += t[i].r - t[i].l;
        }
        printf("Case #%d: ", ++tcase);
        int s = n + m;
        sort(t + 1, t + s + 1, cmp);
        t[s + 1] = t[1];
        t[s + 1].l += 1440;
        c0.clear(); c1.clear(); c10 = 0;
        int ans = 0;
        rep(i, 1, s){
            if (t[i + 1].col == 0 && t[i].col == 0)
                c0.push_back(t[i + 1].l - t[i].r);
            else if (t[i + 1].col == 1 && t[i].col == 1)
                c1.push_back(t[i + 1].l - t[i].r);
            else{
                c10 += t[i + 1].l - t[i].r;
                ans++;
            }
        }
        sort(all(c0));
        sort(all(c1));
        //cout<<sum0<<" "<<sum1<<endl;
        //cout<<SZ(c0)<<" "<<SZ(c1)<<endl;
        for (int i = 0; i < SZ(c0); i++){
            if (sum0 + c0[i] <= 720){
                sum0 += c0[i];
            }
            else{
                ans += 2;
            }
        }
        for (int i = 0; i < SZ(c1); i++){
            if (sum1 + c1[i] <= 720){
                sum1 += c1[i];
            }
            else{
                ans += 2;
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
