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
    ifstream fin("insert.in");
    ofstream fout("printo.txt");
    int test;
    fin >> test;
    for(int tr = 1; tr <= test; tr++){
        int n,k;
        fin >> n >> k;
        //cout << "LOL " << n << " " << k << endl;
        bool filled[1005];
        REP(j,1005) filled[j]=false;
        filled[0]=filled[n+1]=true;
        pair<pair<int,int>,int> endo;
        for(int pr = 0; pr < k; pr++){
            pair<pair<int,int>,int> maxp = MP(MP(-INF,-INF),-INF);
            for(int j = 1;j<=n;j++){
                if(filled[j]) continue;
                int le,ri;
                for(le = j-1;le>=0;le--){
                    if(filled[le]) break;
                }
                for(ri=j+1;ri<=n+1;ri++){
                    if(filled[ri]) break;
                }
                int d1 = j-le-1;
                int d2 = ri-j-1;
                if(d1>d2) swap(d1,d2);
                pair<pair<int,int>,int> po;
                po = MP(MP(d1,d2),-j);
                if(po>maxp) maxp=po;
            }
            maxp.second=maxp.second*-1;
            filled[maxp.second]=true;
            if(pr==k-1) endo = maxp;
        }
        fout << "Case #"<<tr<<": " << endo.first.second << " " << endo.first.first << endl;
    }
    fout.close();
}
