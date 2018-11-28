#include <bits/stdc++.h>
using namespace std;

#define sz(v)        ((int)v.size())
#define ll           long long
#define all(v)       (v.begin()) , (v.end())
#define rall(v)      (v.rbegin()) , (v.rend())
#define SetTo(v, a)  memset(v,a,sizeof(v))

int n;
bool vis[1005];
string ans;

bool check(string &s){
    for(int i=1;i<sz(s);i++){
        if(s[i] == s[i-1] || s[i] == '.' || s[i-1] == '.')
            return 0;
    }
    return 1;
}

int main ()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt", "w", stdout);
    int tc, R, O, Y, G, V, B;
    cin >> tc;
    for(int test = 1;test <= tc;test++){
        printf("Case #%d: ", test);
        SetTo(vis, 0);
        scanf("%d%d%d%d%d%d%d", &n, &R, &O, &Y, &G, &B, &V);
        vector <pair<int, char>> V;
        V.push_back({R, 'R'});
        V.push_back({B, 'B'});
        V.push_back({Y, 'Y'});

        if(2*R > n || 2*Y > n || 2*B > n){
            puts("IMPOSSIBLE");
            continue;
        }
        vector <int> indexes;
        for(int i=0;i<n;i+=2){
            indexes.push_back(i);
        }
        for(int i=1;i<n;i+=2){
            indexes.push_back(i);
        }

        sort(rall(V));
        ans.assign(n, '.');
        int idx = 0;

        for(int i=0;i<3;i++){
            char c = V[i].second;
            for(int j=0;j<V[i].first;j++){
                ans[indexes[idx]] = c;
                idx++;
            }
        }
        if(check(ans)){
            cout << ans << endl;
        }
        else{
            puts("IMPOSSIBLE");
        }

    }
    return 0;
}
