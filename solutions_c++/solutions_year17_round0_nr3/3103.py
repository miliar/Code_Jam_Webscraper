#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef long long ll;

pair<int,int> insertp(vi& sta){
    int n = sta.size() - 2;
    int optind = -1;
    int optmin = -1;
    int optmax = -1;
    for(int i=1; i<n+1; ++i){
        if(sta[i] != 0)
            continue;
        int ls = 0;
        for(int j=i-1; sta[j] == 0; --j)
            ++ls;
        int rs = 0;
        for(int j=i+1; sta[j] == 0; ++j)
            ++rs;
        if(min(ls,rs) > optmin){
            optind = i;
            optmin = min(ls,rs);
            optmax = max(ls,rs);
        }
        else if(min(ls,rs) == optmin && max(ls,rs) > optmax){
            optind = i;
            optmin = min(ls,rs);
            optmax = max(ls,rs);
        }
    }
    assert(optind != -1);
    sta[optind] = 1;
    return {optmax, optmin};
}

void solve(){
    ll n, k;
    cin >> n >> k;
    map<ll,ll> st;
    st[n] = 1;
    while(k > 0){
        auto b = prev(st.end());
        if(k > b->second){
            k -= b->second;
            ll la = (b->first)/2;
            ll sm = (b->first-1)/2;
            st[la] += b->second;
            st[sm] += b->second;
            st.erase(b);
        }
        else{
            ll la = (b->first)/2;
            ll sm = (b->first-1)/2;
            cout << la << " " << sm;
            return;
        }
    }
    assert(0);
    cout << "ERROR";
    return;
}

int main(){
    int tc;
    cin >> tc;
    for(int t=1; t<=tc; ++t){
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }
}
