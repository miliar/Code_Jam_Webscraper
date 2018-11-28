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
map<tuple<char,char,  short,short,short,short,short,short>, bool> M;
// R,O,Y,G,B,V
// 1 2 3 4 5 6
int HEAD = 0;
char SEQ[1005];
int N;

bool foo(char tail, short R, short O, short Y, short G, short B, short V){
    // printf("%d: %d,%d,%d,%d,%d,%d\n", tail, R, O, Y, G, B, V);
    int sm = R+O+Y+G+B+V;
    if (Y+B+2 < R) return 0;
    if (B+R+2 < Y) return 0;
    if (Y+R+2 < B) return 0;
    if (sm == 0){
        // cout<<"HEAD:"<<HEAD<<endl;
        if (HEAD == 1 && (tail != 6 && tail != 1 && tail != 2)){ SEQ[0] = 'R'; return 1;}
        if (HEAD == 2 && (tail != 1 && tail != 2 && tail != 3)){ SEQ[0] = 'O'; return 1;}
        if (HEAD == 3 && (tail != 2 && tail != 3 && tail != 4)){ SEQ[0] = 'Y'; return 1;}
        if (HEAD == 4 && (tail != 3 && tail != 4 && tail != 5)){ SEQ[0] = 'G'; return 1;}
        if (HEAD == 5 && (tail != 4 && tail != 5 && tail != 6)){ SEQ[0] = 'B'; return 1;}
        if (HEAD == 6 && (tail != 5 && tail != 6 && tail != 1)){ SEQ[0] = 'V'; return 1;}
        return 0;
    } 
    if (M.count(make_tuple(HEAD,tail,R,O,Y,G,B,V))){
        // printf("%d: %d,%d,%d,%d,%d,%d => CACHE %d\n", tail, R, O, Y, G, B, V, M[make_tuple(HEAD,tail,R,O,Y,G,B,V)]);
        return M[make_tuple(HEAD,tail,R,O,Y,G,B,V)];
    }
    bool t = 0;
    char C = 0;
    // R
    if (t==0 && R && (tail != 6 && tail != 1 && tail != 2)){
        if (sm == N) HEAD = 1;
        C = 'R';
        t = foo(1, R-1, O, Y, G, B, V);
    }
    // O
    if (t==0 && O && (tail != 1 && tail != 2 && tail != 3)){
        if (sm == N) HEAD = 2;
        C = 'O';
        t = foo(2, R, O-1, Y, G, B, V);
    }
    // Y
    if (t == 0 && Y && (tail != 2 && tail != 3 && tail != 4)){
        if (sm == N) HEAD = 3;
        C = 'Y';
        t = foo(3, R, O, Y-1, G, B, V);
    }
    // G
    if (t == 0 && G && (tail != 3 && tail != 4 && tail != 5)){
        if (sm == N) HEAD = 4;
        C = 'G';
        t = foo(4, R, O, Y, G-1, B, V);
    }
    // B
    if (t == 0 && B && (tail != 4 && tail != 5 && tail != 6)){
        if (sm == N) HEAD = 5;
        C = 'B';
        t = foo(5, R, O, Y, G, B-1, V);
    }
    // V
    if (t == 0 && V && (tail != 5 && tail != 6 && tail != 1)){
        if (sm == N) HEAD = 6;
        C = 'V';
        t = foo(6, R, O, Y, G, B, V-1);
    }
    if (t){
        SEQ[sm] = C;
        // printf("%d: %d,%d,%d,%d,%d,%d => Yep\n", tail, R, O, Y, G, B, V);
        return M[make_tuple(HEAD,tail,R,O,Y,G,B,V)] = 1;
    }

    // printf("%d: %d,%d,%d,%d,%d,%d => Nope\n", tail, R, O, Y, G, B, V);
    return M[make_tuple(HEAD,tail,R,O,Y,G,B,V)] = 0;
}
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
        cerr<<_t<<endl;
        M.clear();
        int R, O, Y, G, B, V;
        scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
        printf("Case #%d: ", _t);
        if (foo(0,R,O,Y,G,B,V)){
            SEQ[N] = 0;
            printf("%s\n", SEQ);
        } else
            puts("IMPOSSIBLE");
    }
    return 0;
}
