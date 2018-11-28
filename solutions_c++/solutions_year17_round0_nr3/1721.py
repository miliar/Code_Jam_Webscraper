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
    long long N,K;
    scanf("%lld %lld",&N,&K);
    K--;
    long long M=K,P=1,A;
    while(M!=0){
        M=M/2;
        P=P*2;
    }
    P=(P-1==K)?P-1:P/2-1;
    A=(N-P)/(P+1);
    if(mod(N-P,P+1)>K-P)
        A++;
    printf("%lld %lld\n",A/2,(A+1)/2-1);
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
