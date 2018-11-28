#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <vector>
#include <bits/stdc++.h>
#include <time.h>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <iostream>
#include <bitset>
#include <algorithm>
using namespace std;
#define MP make_pair
#define PB push_back
#define mst(a,b) memset((a),(b),sizeof(a))
typedef long long LL;
typedef unsigned long long uLL;
typedef pair<int, int> Pii;
typedef vector<int> Vi;
typedef vector<Pii> Vii;
const int inf = 0x3f3f3f3f;
const LL INF = (1uLL << 63) - 1;
const LL mod = 1000000007;
const int N = 1e5 + 7;
const double Pi = acos(-1.0);
const int maxn = 1e4 + 5;
const uLL Hashmod = 29050993;
LL La,Lb;
void Div(LL l,LL r,LL num){
    LL len = r - l + 1;
    LL mid = (l + r)/2;
    if(num == 1){
        if(len&1){
            La = len / 2;
            Lb = len / 2;
        }
        else {
            La = len / 2;
            Lb = La - 1;
        }
        return;
    }
    if(len & 1){
        if(num & 1)Div(mid + 1,r,(num - 1)/2);
        else Div(l,mid - 1,num / 2);
    }
    else {
        if(num & 1)Div(l,mid - 1,(num - 1)/2);
        else Div(mid + 1,r,num / 2);
    }
}
int main() {
#ifdef local
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("w", "w", stdout);
#endif
  //  ios::sync_with_stdio(0);
  //  cin.tie();
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; ++cas) {
        printf("Case #%d: ", cas);
        int n,k;
        cin>>n>>k;
        Div(1,n,k);
        cout<<La<<" "<<Lb<<endl;
    }
}
