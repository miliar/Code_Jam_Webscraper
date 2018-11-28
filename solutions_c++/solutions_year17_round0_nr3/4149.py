#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;

int t;
ll n, k;
vii node;
void pre() {
    node.assign(1000010, ii());
    for (int j = 1 ; j <= 1000000 ; j++) {
        if (j % 2 == 0) {
            node[j].first = j/2;
            node[j].second = j/2 - 1;
        }
        else {
            node[j].first = j/2;
            node[j].second = j/2;
        }
    }
}
int main() {
    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
    freopen("cjinput.txt", "r", stdin);
    freopen("cjoutput.txt", "w", stdout);
    pre();
    ll val;
    cin >> t;
    for (int i = 1 ; i <= t ; i++)
    {
        
        priority_queue<ll> q;
        cin >> n >> k;
        q.push(n);
        
        while (k>1) {
            val = q.top();
            q.pop();
            q.push(node[val].first);
            q.push(node[val].second);
            k--;
        }
        val=q.top();
        cout << "Case #" << i << ": " << node[val].first << " " << node[val].second << endl;
    }
    return 0;
}