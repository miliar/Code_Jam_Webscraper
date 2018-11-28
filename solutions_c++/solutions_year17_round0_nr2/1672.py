#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define mod(a,b) ((a)%(b)+(b))%(b)
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define rep(i,n) for(int (i)=0;(i)<int((n));(i)++)


void solve(){
    char S[23];
    scanf("%s",S);
    vi N(strlen(S));
    rep(i,sz(N))
        N[i]=int(S[i])-48;
    rep(i,sz(N)-1){
        if(N[i]>N[i+1]){
            rep(j,sz(N)-i-1)
                N[j+i+1]=9;
            N[i]--;
            for(int k=i;k!=0 && N[k-1]>N[k];k--){
                N[k-1]--;
                N[k]=9;
            }
        }
    }
    tr(N,i)
        if(*i!=0)
            printf("%d",*i);
    printf("\n");
}
int main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T;
    scanf("%d",&T);
    //cin.ignore(numeric_limits<streamsize>::max(), '\n');
    rep(n,T) {
        fprintf(stderr,"%d\n",n+1);
        printf("Case #%d: ",n+1);
        solve();
    }
}
