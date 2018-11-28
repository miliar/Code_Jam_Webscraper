#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define pf pop_front
#define IOS ios::sync_with_stdio(false)
ll t , k , n ;
vector <ll> path;
pair <ll,ll> retlsandrs(ll num){
    pair <ll,ll> ans;
    if(num&1){
        ans.ff = ans.ss = num/2;
    }
    else{
        ans.ff = max(num/2 - 1,0ll);
        ans.ss = num/2;
    }
    return ans;
}
bool checkLeft(ll par , ll child){
    if(child==2*par)return true;
    else return false;
}
int main(){

	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	cin >> t;
    for(int test = 1 ; test <= t ; test++){
        cin >> n >> k;
        queue <ll> q;
        path.clear();
        ll sz = n;
        q.push(n);
        while(!q.empty()){
            ll el = q.front();
            q.pop();
            if(el==0)continue;
            path.pb(el);
            if(el&1){
                if(el==1)continue;
                q.push(el/2);
                q.push(el/2);
            }
            else{
                if(el==2||el==0)continue;
                q.push(el/2);
                q.push(max(el/2-1,0ll));
            }
        }
        sort(path.rbegin(),path.rend());
        if(k==1){
            pair <ll,ll> ans = retlsandrs(n);
            cout << "Case #" << test << ": " << max(ans.ff,ans.ss) << " " << min(ans.ff,ans.ss) << endl;
            continue; 
        }
        if(k>=path.size()){
            cout << "Case #" << test << ": " << 0 << " " << 0 << endl;
            continue;
        }
        else{
            pair <ll,ll> ans = retlsandrs(path[k-1]);
            cout << "Case #" << test << ": " << max(ans.ff,ans.ss) << " " << min(ans.ff,ans.ss) << endl;
        }

    }
    return 0;
}