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
#define taskname "A"
using namespace std;
typedef long long ll;
int t;
string s;
int k, ans;
const char sum=int('+')+int('-');
 int main(){
    freopen(taskname".in", "r", stdin);
    freopen(taskname".out", "w", stdout);
    cin>>t;
    FOR(itest, 1, t){
        cin>>s>>k;
        ans=0;
        for(int i=0; i+k<=s.size(); i++){
            if(s[i]=='-'){
                ans++;
                for(int j=0; j<k; j++)
                    s[i+j]=sum-s[i+j];
            }
        }
        printf("Case #%d: ", itest);
        for(int i=0; i<s.size(); i++){
            if(s[i]=='-'){
                puts("IMPOSSIBLE");
                goto line1;
            }
        }
        writeln(ans);
        line1:;
    }
}
