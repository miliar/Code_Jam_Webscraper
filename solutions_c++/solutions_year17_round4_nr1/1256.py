#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <random>

using namespace std;

typedef long long ll;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define tget(X,id) get<id>(X)

#define MAXN 1005

string FILE_IN, FILE_OUT;

int cnt[4];
int DP_2[102][102];
int DP_3[102][102][102];

int foo3(int r1, int r2){
    if (r1 < 0 || r2 < 0 || r1+r2==0) return 0;
    if (DP_2[r1][r2]) return DP_2[r1][r2]-1;
    int r = 0;
    r = 1+max(max(foo3(r1-1, r2-1), foo3(r1-3, r2)), foo3(r1, r2-3));
    return (DP_2[r1][r2] = r+1)-1;
}
int foo4(int r1, int r2, int r3){
    if (r1 < 0 || r2 < 0 || r3 < 0 || r1+r2+r3==0) return 0;
    if (DP_3[r1][r2][r3]) return DP_3[r1][r2][r3]-1;
    int r = 0;
    r = max(r, foo4(r1, r2-1, r3-2));
    r = max(r, foo4(r1, r2-2, r3));
    r = max(r, foo4(r1-1, r2, r3-1));
    r = max(r, foo4(r1-2, r2-1, r3));
    r = max(r, foo4(r1-4, r2, r3));
    r = max(r, foo4(r1, r2, r3-4));
    r++;
    return (DP_3[r1][r2][r3] = r+1)-1;
}

int main(int argc, char *argv[]){
    if (argc == 1){
        cerr<<"No input specified, using A.in"<<endl;
        FILE_IN = "A.in";
        FILE_OUT = "A.out";
    } else {
        FILE_IN = string(argv[1]);
        FILE_OUT = FILE_IN + ".out";
    }
    freopen(FILE_IN.c_str(),"r",stdin);
    freopen(FILE_OUT.c_str(),"w",stdout);
    
    int _T;
    scanf("%d", &_T);
    for (int _t = 1; _t <= _T; _t++){
        int N, P, a;
        memset(cnt,0,sizeof cnt);
        scanf("%d%d", &N, &P);
        for (int i = 0; i < N; i++)
            scanf("%d", &a), cnt[a%P]++;
        int ans = cnt[0];
        if (P == 2) ans += (cnt[1]+1)/2;
        else if (P == 3) ans += foo3(cnt[1], cnt[2]);
        else ans += foo4(cnt[1], cnt[2], cnt[3]);
        printf("Case #%d: %d\n", _t, ans);
    }
    return 0;
}
