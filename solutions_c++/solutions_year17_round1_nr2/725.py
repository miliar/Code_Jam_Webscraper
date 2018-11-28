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

int ceil(int a, int b){
    if(a%b==0) return a/b;
    return 1+a/b;
}

int Q[55][55];
queue<pii> W[55];
int R[55];

bool works(int amt0, int ind, int& x0, int& y0){
    x0=ceil(10*amt0,11*R[ind]);
    y0=(10*amt0)/(9*R[ind]);

    return x0>0 and x0<=y0;
}

int main(){
    int t;
    read(t);
    fr(ii,t){
        int n,p;
        read(n,p);

        fr(i,n) read(R[i]);
        fr(i,n){
            fr(j,p) read(Q[i][j]);
            sort(Q[i],Q[i]+p);
        }

        fr(i,n){
            while(W[i].size()>0) W[i].pop();

            fr(j,p){
                int x,y;
                if(works(Q[i][j],i,x,y)){
                    W[i].push(pii(x,y));
                }
            }
        }

        int cnt=0;

        int claim=1;
        while(claim<=1000005){
            bool allempty=true;
            bool allhaveit=true;

            // clean
            fr(i,n){
                while(W[i].size()>0 and W[i].front().second<claim) W[i].pop();
            }

            fr(i,n){
                if(W[i].size()>0){
                    allempty=false;
                    if(W[i].front().first>claim or W[i].front().second<claim) allhaveit=false;
                }
                else{
                    allhaveit=false;
                }
            }

            if(allempty) break;

            if(!allhaveit){
                claim++;
            }
            else{
                cnt++;
                fr(i,n) W[i].pop();
            }
        }

        printf("Case #%d: %d\n",ii+1,cnt);
    }
}
