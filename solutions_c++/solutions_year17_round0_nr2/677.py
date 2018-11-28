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
#define taskname "B"
using namespace std;
typedef long long ll;
map <ll, ll, greater <ll> > M;
int t;
ll n;
string s;
ll ans=0;
int main(){
    freopen(taskname".in", "r", stdin);
    freopen(taskname".out", "w", stdout);
    read(t);
    FOR(itest, 1, t){
        read(n);
        stringstream ss;
        ss<<n;
        ss>>s;
        ans=0;
        if(n==1000000000000000000LL)
            ans=999999999999999999LL;
        else
            for(int i=0; i<s.size(); i++){
                DFOR(k, 9, 0){
                    ll temp=ans;
                    for(int j=i; j<s.size(); j++)
                        temp=temp*10+k;
                    if(temp<=n){
                        ans=ans*10+k;
                        break;
                    }
                }
            }
        printf("Case #%d: ", itest);
        writeln(ans);
    }
}
