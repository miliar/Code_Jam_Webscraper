#include <bits/stdc++.h>
using namespace std;
#define MP make_pair
#define LL long long 
map<pair<LL,LL>,LL> mp;
set<LL>st;
LL T,n,k;
pair<LL,LL> solve(LL n){
    if(n&1) return MP(n/2,n/2);
    else return MP(n/2,n/2-1);
}
long long res;
int main(){
    cin>>T;
    freopen("c.txt","w",stdout);
    int _case = 0;
    while(T--){
        res = 0;
        cin>>n>>k;
        mp.clear();
        st.insert(-n);
        mp[solve(n)]=1;
        res++;
        pair<LL,LL> ans = solve(n),tm;
        
        while(res<k){
            
            LL temp = -*st.begin();
            //cout<<res<<" "<<temp<<endl;
            st.erase(-temp);
            tm = solve(temp);
            res+=mp[tm];
            mp[solve(tm.first)] += mp[tm];
            if(res>=k){
                ans = solve(tm.first);break;
            }
            st.insert(-tm.first);
            res+=mp[tm];
            if(res>=k){
                ans = solve(tm.second);break;
            }
            st.insert(-tm.second);
            mp[solve(tm.second)]+=mp[tm];
        }
        cout<<"Case #"<<++_case<<": "<<ans.first<<" "<<ans.second<<endl;
        
    }
    return 0;
}
