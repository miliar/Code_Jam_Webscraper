#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cstdarg>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;

#if __cplusplus > 199711L
    void read(){}
    template<typename... T>
    void read(int& head, T&... tail) {scanf("%d",&head); read(tail...);}

    #define DB(args...) { cerr << __LINE__<< ": "; vector<string> _v = split(#args, ','); err(_v.begin(), args); }
    vector<string> split(const string& s, char c) {
        vector<string> v;stringstream ss(s);string x;
        while (getline(ss, x, c)) v.push_back(x);
        return move(v);
    }
    void err(vector<string>::iterator it) {cerr<<endl;}
    template<typename T, typename... Args>
    void err(vector<string>::iterator it, T a, Args... args) {
        cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << "  "; err(++it, args...);
    }
#else
    #define DB(e) cerr << __LINE__ << ": " << #e << " = " << e << endl;
    void read(int& head) {scanf("%d",&head);}
#endif

#define ll long long int
#define pb push_back
#define fr(i,n)     for(int i=0;i<n;i++)
#define init(mem,v) memset(mem,v,sizeof(mem))
typedef pair<int,int> pii;

#define mx 30

int r,c;
char grid[mx][mx];
bool solved[mx];

int firstone(int cr){
    fr(j,c) if(grid[cr][j]!='?') return j;
    return -1;
}

int nextone(int cr, int cc){
    for(int j=cc+1;j<c;j++) if(grid[cr][j]!='?') return j;
    return -1;
}

int main(){
    int t;
    read(t);
    fr(ii,t){
        read(r,c);
        fr(i,r){
            scanf("%s",&grid[i]);
            solved[i]=false;
        }

        fr(i,r){
            int f=firstone(i);
            if(f==-1) continue;

            solved[i]=true;
            fr(j,f) grid[i][j]=grid[i][f];

            for(int j=f+1;j<c;j++){
                if(grid[i][j]=='?'){
                    grid[i][j]=grid[i][f];
                }
                else{
                    f=j;
                }
            }
        }

        int lastsolved=-1;
        fr(i,r){
            if(solved[i]) lastsolved=i;
            else if(!solved[i] and lastsolved>=0){
                solved[i]=true;
                fr(j,c) grid[i][j]=grid[lastsolved][j];
            }
        }

        lastsolved=-1;
        for(int i=r-1;i>=0;i--){
            if(solved[i]) lastsolved=i;
            else if(!solved[i] and lastsolved>=0){
                solved[i]=true;
                fr(j,c) grid[i][j]=grid[lastsolved][j];
            }
        }

        printf("Case #%d:\n",ii+1);
        fr(i,r) printf("%s\n",grid[i]);
    }
}
