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

int R,C;
char MX[30][30];

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
        scanf("%d%d", &R, &C);
        int lastR = -1;
        for (int i = 0; i < R; i++){
            scanf("%s", MX[i]);
            char last = '?';
            for (int j = 0; j < C; j++)
                if (MX[i][j] != '?'){
                    last = MX[i][j];
                    for (int jj = j-1; jj >= 0 && MX[i][jj] == '?'; jj--) MX[i][jj] = MX[i][j];
                }
            if (last != '?'){
                lastR = i;
                for (int j = C-1; j >= 0 && MX[i][j] == '?'; j--) MX[i][j] = last;
                for (int j = i-1; j >= 0 && MX[j][0] == '?'; j--) strcpy(MX[j], MX[i]);
            }
        }
        for (int i = lastR+1; i < R; i++) strcpy(MX[i], MX[lastR]);
        printf("Case #%d:\n", _t);
        for (int i = 0; i < R; i++) printf("%s\n", MX[i]);
        printf("\n");
    }
    return 0;
}
