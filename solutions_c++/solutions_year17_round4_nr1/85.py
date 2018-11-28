#include <bits/stdc++.h>
using namespace std;
//make_tuple emplace_back next_permutation push_back make_pair second first setprecision

#if MYDEBUG
#include "lib/cp_debug.h"
#else
#define DBG(...) ;
#endif

using LL = long long;
constexpr LL LINF=334ll<<53;
constexpr int INF=15<<26;
constexpr LL  MOD=1E9+7;

struct Problem{
    int n,p,ans;
    vector<int> g,cnt;
    Problem(int n, int p):n(n),p(p),g(n),cnt(p){};

    void solve(){
        for(int i=0; i<n; ++i){
            cin >> g[i];
            cnt[g[i]%p]++;
        }
        if(p==2){
            ans=cnt[0];
            ans+=(cnt[1]+1)/2;
            cout <<ans <<"\n";
        }else if(p==3){
            ans=cnt[0];
            int add=min(cnt[2],cnt[1]);
            ans+=add;
            cnt[2]-=add;
            cnt[1]-=add;
            ans+=(cnt[1]+2)/3+(cnt[2]+2)/3;
            cout <<ans <<"\n";
        }else if(p==4){
            ans=cnt[0];
            int add=min(cnt[1],cnt[3]);
            ans+=add;
            cnt[3]-=add;
            cnt[1]-=add;

            int odd=max(cnt[1],cnt[3]);
            int maxi=0;
            for(int i=0; i<=min(odd/2,cnt[2]); ++i){
                int tmp=i,tmpo=odd,tmp2=cnt[2];
                tmpo-=i*2;
                tmp2-=i;
                tmp+=tmp2/2;
                tmp2%=2;
                tmp+=tmpo/4;
                tmpo%=4;
                tmp+=(tmpo or tmp2);
                DBG(tmp)
                maxi=max(maxi,tmp);
            }
            cout <<ans+maxi <<"\n";
        }


    }
};

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int testcases;
    cin >> testcases;
    for(int i=1; i<=testcases; ++i){
        cout << "Case #" << i << ": ";
        int n,pp;
        cin >>n >>pp;
        Problem p(n,pp);
        p.solve();
    }

    return 0;
}

