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

char S[1005];

int main(int argc, char *argv[]){
    if (argc == 1){
        cerr<<"No input specified, using B.in"<<endl;
        FILE_IN = "B.in";
        FILE_OUT = "B.out";
    } else {
        FILE_IN = string(argv[1]);
        FILE_OUT = FILE_IN + ".out";
    }
    freopen(FILE_IN.c_str(),"r",stdin);
    freopen(FILE_OUT.c_str(),"w",stdout);
    
    int _T;
    scanf("%d", &_T);
    //~ _T = 10000;
    for (int _t = 1; _t <= _T; _t++){
        int len;
        scanf("%s", S);
        //~ sprintf(S,"%d",_t); 
        len = strlen(S);
        for (int i = len-1; i > 0; i--){
            if (S[i] < S[i-1]){
                S[i] = '9';
                S[i-1]--;
            }
        }
        char mx = '0';
        int skip0 = 0;
        for (int i = 0; i < len; i++){
            S[i] = mx = max(S[i], mx);
            if (S[i] == '0' && skip0 == i) skip0++;
        }
        printf("Case #%d: ", _t);
        printf("%s", S+skip0);
        printf("\n");
        
        //~ int aans = atoi(S+skip0);
        //~ cerr<<_t<<": "<<aans<<" vs ";
        //~ break;
        
        //~ int ttt = _t;
        //~ while (1){
            //~ int check = 0;
            //~ sprintf(S,"%d",ttt); 
            //~ len = strlen(S);
            //~ for (int i = 0; i < len-1; i++)
                //~ if (S[i] > S[i+1]){
                    //~ check = 1;
                    //~ break;
                //~ }
            //~ if (check){
                //~ ttt--;
                //~ continue;
            //~ }
            //~ break;
        //~ }
        //~ cerr<<ttt<<endl;
        //~ if (aans != ttt){
            //~ cerr<<"Ops!"<<endl;
            //~ break;
        //~ }
    }
    return 0;
}
