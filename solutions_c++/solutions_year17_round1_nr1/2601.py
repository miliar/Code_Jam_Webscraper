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

string grid[25];
char ans[25][25];
bool solved[26];
bool has[26];
void solve(int r1, int c1, int r2, int c2, char ch){
    //cout << r1 << " " << c1 << " " << r2 <<" " << c2 <<" " << ch << endl;
    int cnt = 0;
    int fr=-1,fc=-1;

        for(int r = r1; r <= r2; r++){
        for(int c = c1; c <= c2; c++){
            if(grid[r][c]==ch){
                fr = r; fc = c;
                cnt++; break;
            }
        }
        if(cnt>0) break;
    }
    if(cnt==0) return;
    int pr=-1,pc=-1;
    char otro;
    for(int r = r1; r <= r2; r++){
        for(int c = c1; c <= c2; c++){
            if(grid[r][c]!='?' && grid[r][c]!=ch){
                pr = r; pc = c;
                otro = grid[r][c];
                break;
            }
        }
        if(pr!=-1) break;
    }
    if(pr==-1){
        //end
        for(int r = r1; r <= r2; r++){
    for(int c = c1; c <= c2; c++){
        if(ans[r][c]!='-') return;
    }
    }
        for(int r = r1; r <= r2; r++){
            for(int c = c1; c <= c2; c++){
                ans[r][c]=ch;
            }
        }
        solved[ch-'A']=true;
        return;
    }

    //fix with d&c
    if(fr==pr && fc<pc){
        solve(r1,c1,r2,fc,ch);
        solve(r1,fc+1,r2,c2,otro);
    }
    else if(fr==pr && fc>pc){
        solve(r1,c1,r2,pc,otro);
        solve(r1,pc+1,r2,c2,ch);
    }
    else if(fc==pc && fr<pr){
        solve(r1,c1,fr,c2,ch);
        solve(fr+1,c1,r2,c2,otro);
    }
    else if(fc==pc && fr>pr){
        solve(r1,c1,pr,c2,otro);
        solve(pr+1,c1,r2,c2,ch);
    }
    else if(fr<pr && fc<pc){
        solve(r1,c1,fr,c2,ch);
        solve(fr+1,c1,r2,c2,otro);
    }
    else if(fr<pr && fc>pc){
        solve(r1,c1,fr,c2,ch);
        solve(fr+1,c1,r2,c2,otro);
    }
    else if(fr>pr && fc<pc){
        solve(r1,c1,r2,fc,ch);
        solve(r1,fc+1,r2,c2,otro);
    } else{
        solve(r1,c1,r2,pc,otro);
        solve(r1,pc+1,r2,c2,ch);
    }

}
int main() {
    ifstream fin("insert.in");
    ofstream fout("insert.txt");
    int test;
    fin >> test;
    for(int tr = 1; tr <= test; tr++){
        int n,m;
        fin >> n >> m;
        REP(i,n){
            fin >> grid[i];
        }
        REP(i,n) REP(j,m) ans[i][j]='-';
        REP(i,26) has[i]=false;
        REP(i,n) REP(j,m) has[grid[i][j]]=true;
        REP(i,26) solved[i]=false;
        char fc = '0';
        REP(i,n) REP(j,m) if(fc=='0' && (int)grid[i][j]>=(int)'A' && (int)grid[i][j]<=(int)'Z') fc = grid[i][j];
        for(int i = 'A'; i <= 'Z'; i++){

            if(has[i] && !solved[i-'A']) solve(0,0,n-1,m-1,char(i));
        }
        fout << "Case #"<<tr << ":"<<endl;
        REP(i,n){
            REP(j,m){
                fout << ans[i][j];
            }
            fout <<endl;
        }
        cout << "==="<<endl;
    }
    fout.close();

}
