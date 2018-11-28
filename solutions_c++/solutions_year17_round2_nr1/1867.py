#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<cmath>
#include<string>
#include<algorithm>
#include<cstdlib>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pr;
const double pi=acos(-1);
#define rep(i,a,n) for(int i=a;i<=n;i++)
#define per(i,n,a) for(int i=n;i>=a;i--)
#define Rep(i,u) for(int i=head[u];i;i=Next[i])
#define clr(a) memset(a,0,sizeof a)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)(x).size())

int main(){
    int t;
    cin>>t;
    int i = 1;
    int d,n;
    while(t--){
        //logic
        cin>>d>>n;
        vector<int> pos(n),s(n);
        int j;
        double slowest = 0.0f;
        rep(j,0,n-1){
            cin>>pos[j]>>s[j];
            double time = (double)(d-pos[j])/s[j];
            slowest = max(slowest,time);
            //cout<<slowest<<" slow"<<endl;
        }
        double ans = (double)d/slowest;
        
        cout<<"Case #"<<i++<<": "<<setprecision(6)<<fixed<<ans<<endl;
    }
}
