#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std;

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<ll> vll;

#define inst freopen("in.txt", "r", stdin)
#define oust freopen("out.txt", "w", stdout)

int main() {
    inst;oust;
    int t, cs = 1;
    cin>>t;
    while(t--) {
        int n,rr, oo, yy, gg, bb, vv;
        cin>> n>> rr>>oo>>yy>>gg>>bb>>vv;
        vector< pair<ll, char> > vec;
        vec.pb(mp(rr,'R'));
        vec.pb(mp(yy,'Y'));
        vec.pb(mp(bb,'B'));
        sort(vec.begin(),vec.end());
        if(vec[2].first > vec[1].first + vec[0].first) {
            printf("Case #%d: IMPOSSIBLE\n", cs++);
            continue;
        }
        printf("Case #%d: ", cs++);
        ll ext = vec[1].first + vec[0].first - vec[2].first;
        //cout<<ext<<endl;
        for(int i = 0;i<ext;i++) cout<<vec[2].second<<vec[0].second<<vec[1].second;
        for(int i=1;i<=vec[1].first-ext;i++) cout<<vec[2].second<<vec[1].second;
        for(int i=1;i<=vec[0].first-ext;i++) cout<<vec[2].second<<vec[0].second;
        cout<<'\n';
    }
    return 0;
}
