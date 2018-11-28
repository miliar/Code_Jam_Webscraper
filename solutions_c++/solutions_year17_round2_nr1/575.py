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
        int N, D;
        scanf("%d%d", &D, &N);
        vector<ii> H(N);
        for (int i = 0; i < N; i++)
            scanf("%d%d", &H[i].ff, &H[i].ss);
        sort(H.rbegin(), H.rend());
        double t = 0;
        for (auto x : H){
            double tt = ((double)max(D-x.ff, 0))/x.ss;
            // cout<<x.ff<<","<<x.ss<<endl;
            // cout<<tt<<endl;
            t = max(t, tt);
        }
        printf("Case #%d: %lf\n", _t, D/t);
    }
    return 0;
}
