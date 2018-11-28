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

char S[1005];
int n,k;

void flip(int st, int end){
    for(int i=st;i<end;i++) S[i]=S[i]=='+'?'-':'+';
}

bool allplus(){
    fr(i,n) if(S[i]=='-') return false;
    return true;
}

int main(){
    int t;
    read(t);

    fr(ii,t){
        scanf("%s %d",S,&k);
        n=strlen(S);
        int cnt=0;

        for(int i=0;i<=n-k;i++){
            if(S[i]=='-'){
                cnt++;
                flip(i,i+k);
            }
        }
        if(allplus()){
            printf("Case #%d: %d\n",ii+1,cnt);
        }
        else{
            printf("Case #%d: IMPOSSIBLE\n",ii+1);
        }
    }
}
