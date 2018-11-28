#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;
#define rep(i,n) for(ll i=0;i<(n);i++)

using namespace std;


struct Node{
    string s;
    ll cost;
    bool operator< (const Node &r) const{
        return cost > r.cost;
    }
};

int main(){
    int t;
    cin >> t;

    char type[2] = {'-', '+'};
    rep(times, t){
        string s;
        int k;
        cin >> s >> k;

        int len = s.size();
        set<string> visited;
        priority_queue<Node> que;
        que.push({s, 0});
        visited.insert(s);

        string ans = "";
        rep(i, len) ans += "+";

        bool suc = false;
        ll cnt = 0;
        while(!que.empty()){
            Node node = que.top();  que.pop();
            if(node.s == ans){
                suc = true;
                cnt = node.cost;
                break;
            }

            rep(i, len-(k-1)){
                string ns = node.s;
                for(int j = i; j < i+k; j++){
                    if(ns[j] == type[0])    ns[j] = type[1];
                    else                    ns[j] = type[0];
                }
                if(visited.count(ns) == 0){
                    que.push({ns, node.cost+1});
                    visited.insert(ns);
                }
            }
        }

        if(suc) cout << "Case #" << times+1 << ": " << cnt << endl;
        else cout << "Case #" << times+1 << ": IMPOSSIBLE" << endl;        
    }




    return 0;
}
