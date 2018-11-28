#include <queue>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <fstream>
#include <cstring>
#include <string>
#include <climits>
#include <unordered_map>

using namespace std;

//macros
typedef long long ll;
typedef complex<double> point;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;




#define FOR(k,a,b) for(int k=(a); k<=(b); ++k)
#define REP(k,a) for(int k=0; k<(a);++k)
#define SZ(a) int((a).size())
#define ALL(c) (c).begin(),(c).end()
#define PB push_back
#define MP make_pair
#define INF 1000000001
#define INFLONG 1000000000000000000
#define MOD 1000000007
#define MAX 100
#define ITERS 100
#define MAXM 200000
#define MAXN 1000000
#define _gcd __gcd
#define eps 1e-7
#define PI 3.1415926535897932384626
using namespace std;

int main() {
    int tests;
    ifstream fin("insert.in");
    ofstream fout("printo.txt");
    fin >> tests;
    for(int tr=1;tr<=tests;tr++){
        string str;
        fin >> str;
        int k;
        fin >> k;
        int par = 0;
        int use = 0;
        int len = str.length();
        int save[2005];
        REP(pro,2005) save[pro]=0;
        REP(i,len-k+1){
            par = (par+save[i])%2;
            //cout << "?"<<i << " " << par << endl;
            if(str[i]=='+' && par==1){
                use++;
                par++;
                save[i+k]=1;
            } else if(str[i]=='-' && par==0){
                use++;
                par++;
                save[i+k]=1;
            }
            par=par%2;
             //cout << "?"<<i << " " << par << endl;
        }
        bool got = false;
        for(int i = len-k+1; i < len; i++){
            par = (par+save[i])%2;
            if((str[i]=='+' && par==1) || (str[i]=='-' && par==0)){
                fout << "CASE #"<<tr<<": IMPOSSIBLE"<<endl;
                got=true; break;
            }
        }
        if(got) continue;
        fout << "CASE #"<<tr<<": " << use << endl;
    }
    fout.close();
}
