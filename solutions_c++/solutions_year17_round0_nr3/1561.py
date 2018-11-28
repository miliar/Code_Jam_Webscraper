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
typedef unsigned long long ull;

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
        cerr<<"No input specified, using C.in"<<endl;
        FILE_IN = "C.in";
        FILE_OUT = "C.out";
    } else {
        FILE_IN = string(argv[1]);
        FILE_OUT = FILE_IN + ".out";
    }
    freopen(FILE_IN.c_str(),"r",stdin);
    freopen(FILE_OUT.c_str(),"w",stdout);
    
    int _T;
    scanf("%d", &_T);
    for (int _t = 1; _t <= _T; _t++){
        ll N, K;
        cin>>N>>K;
        //~ cerr<<N<<","<<K<<endl;
        map<ll, ll> M;
        M[N] = 1;
        pair<ll,ll> ANS = mp(0,0);
        while (1){
            auto it = M.end(); it--;
            //~ cerr<<K<<":"<<it->first<<","<<it->second<<endl;
            ll a = (it->first-1)/2, b = it->first-1-a;
            K -= it->second;
            if (K <= 0){
                ANS = mp(b, a);
                break;
            }
            if (a) M[a] += it->second;
            if (b) M[b] += it->second;
            M.erase(it);
        }
        printf("Case #%d: ", _t);
        cout<<ANS.ff<<" "<<ANS.ss;
        printf("\n");
    }
    return 0;
}
