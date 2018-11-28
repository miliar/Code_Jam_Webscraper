#include <bits/stdc++.h>
using namespace std;
#define FOR(i, j, k) for(int i=j; i<=k; i++)
#define DFOR(i, j, k) for(int i=j; i>=k; i--)
#define bug(x) cerr<<#x<<" = "<<x<<'\n'
#define pb push_back
#define mp make_pair
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
ll n, t;
ll r[7];
int main(){
//    #ifdef I_have_no_girlfriend
//        if(fopen(taskname".inp", "r"))
//    #endif // I_have_no_girlfriend
            freopen(taskname".inp", "r", stdin);
            freopen(taskname".out", "w", stdout);
    read(t);
    FOR(itest, 1, t){
        read(n);
        FOR(i, 1, 6)
            read(r[i]);
        printf("Case #%d: ", itest);
        r[2]=r[3];
        r[3]=r[5];
        string s="0RYB";
        if(r[2]<r[3]){
            swap(r[2], r[3]);
            swap(s[2], s[3]);
        }
        if(r[1]<r[2]){
            swap(r[2], r[1]);
            swap(s[2], s[1]);
        }
        if(r[2]<r[3]){
            swap(r[2], r[3]);
            swap(s[2], s[3]);
        }
        if(r[2]+r[3]<r[1]){
            puts("IMPOSSIBLE");
            continue;
        }
        for(int i=1, j=1; i<=r[1]; i++){
            putchar(s[1]);
            if(j<=r[2]){
                putchar(s[2]);
                j++;
            }
            if(i>r[1]-r[3])
                putchar(s[3]);
        }
        putchar('\n');
    }
}