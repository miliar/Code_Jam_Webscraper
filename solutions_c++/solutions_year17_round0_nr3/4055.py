#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef long long int ll;
typedef pair<int,int> pi;
typedef unsigned long long int ull;

ll lsone(ll p){return(p & -p);}

int TC;
string s;
ll n,k;

int main(){
    std::ios::sync_with_stdio(false);
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> TC;
    for (int outi=1;outi<=TC;outi++){
        cin >> n >> k;
        cout << "Case #" << outi << ": ";
        k--;
        ll mul = 2;
        unordered_map<ll, ll> myque;
        unordered_map<ll, ll> myque2;
        myque[n] = 1;
        while (k>=mul-1){
            mul *= 2;
            for (auto i : myque){
                ll a = i.first - 1;
                ll b = a/2;
                ll c = a-b;
                //cout << b << " " << c << " " << i.second << "\n";
                myque2[b] += i.second;
                myque2[c] += i.second;
            }
            myque = myque2;
            myque2.clear();
        }
        mul = mul / 2;
        ll noc = k-mul+1;
        vector<pair<ll,ll> > ans;
        for (auto i : myque){
            if (i.first>0) ans.push_back(i);
            //cout << i.first << " " << i.second << "\n";
        }
        sort(ans.begin(),ans.end());
        ll ans2;
        for (int i=ans.size()-1;i>=0 && noc>=0;i--){
            noc -= ans[i].second;
            if (noc < 0) ans2 = ans[i].first-1;
        }
        if (noc>= 0) ans2 = ans[0].first-1;
        cout << ans2-ans2/2 << " " << ans2/2 << "\n";

    }

}
