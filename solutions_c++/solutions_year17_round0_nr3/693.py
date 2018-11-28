#include <bits/stdc++.h>
using namespace std;
#define FOR(i, j, k) for(int i=j; i<=k; i++)
#define DFOR(i, j, k) for(int i=j; i>=k; i--)
#define bug(x) cerr<<#x<<" = "<<x<<'\n'
#define mp make_pair
#define pb push_back
typedef long long ll;
template <typename T> inline void read(T &x){
    char c;
    bool nega=0;
    while((!isdigit(c=getchar()))&&(c!='-'));
    if(c=='-'){
        nega=1;
        c=getchar();
    }
    x=c-48;
    while(isdigit(c=getchar()))
        x=x*10+c-48;
    if(nega)
        x=-x;
}
template <typename T> inline void writep(T x){
    if(x>9) writep(x/10);
    putchar(x%10+48);
}
template <typename T> inline void write(T x){
    if(x<0){
        putchar('-');
        x=-x;
    }
    writep(x);
}
template <typename T> inline void writeln(T x){
    write(x);
    putchar('\n');
}
#define taskname "C"
using namespace std;
typedef long long ll;
map <ll, ll, greater <ll> > M;
int t;
ll n, k;
int main(){
    freopen(taskname".in", "r", stdin);
    freopen(taskname".out", "w", stdout);
    read(t);
    FOR(itest, 1, t){
        read(n);
        read(k);
        M.clear();
        M[n]=1;
        while(true){
            ll res=M.begin()->first;
            if(M.begin()->second>=k){
                printf("Case #%d: ", itest);
                write(max((res+1)/2-1, res-(res+1)/2));
                putchar(' ');
                writeln(min((res+1)/2-1, res-(res+1)/2));
                goto line1;
            }
            else{
                k-=M.begin()->second;
                if(M.find((res+1)/2-1)==M.end())
                    M[(res+1)/2-1]=0;
                M[(res+1)/2-1]+=M.begin()->second;
                if(M.find(res-(res+1)/2)==M.end())
                    M[res-(res+1)/2]=0;
                M[res-(res+1)/2]+=M.begin()->second;
                M.erase(M.begin());
            }
        }
        line1:;
    }
}
