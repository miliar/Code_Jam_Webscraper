#include<bits/stdc++.h>
using namespace std;

#define lli long long
#define pb push_back
#define mp make_pair
#define gc getchar_unlocked
#define lld "%I64d"
#define DEBUG(x) cout<<">value ("<<#x<<") : "<<x<<endl;
#define mod 1000000007

const int lmt=1000005;
const double oo = (double)1e15;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++){
        double dest;
        int n;
        cin>>dest>>n;
        double ans = oo;
        while(n--){
            double pos,sp;
            cin>>pos>>sp;
            double tmm = (dest-pos)/sp;
            double st=0,en=oo;
            for(int i=0;i<300;i++){
                double md = (st+en)/2.0;
                double cur = dest/md;
                if(cur<tmm)
                    en=md;
                else
                    st=md;
            }
            ans = min(ans,st);
        }
        printf("Case #%d: %.6lf\n",test,ans);
    }
    return 0;
}