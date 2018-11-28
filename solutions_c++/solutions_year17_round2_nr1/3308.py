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
    int D,N;
    scanf("%d %d",&D,&N);
    vi K(N),S(N);
    rep(i,N)
        scanf("%d %d",&K[i],&S[i]);
    double Spd=double(S[0])/(1-double(K[0])/double(D));
    rep(i,N)
        Spd=min(Spd,double(S[i])/(1-double(K[i])/double(D)));
    printf("%f\n",Spd);
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
