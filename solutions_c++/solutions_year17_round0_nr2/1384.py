//This template was originally written by zscoder and copied by duckmoon.
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key
#define INF 2e18

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector< pair<ll, ll> > vii;
typedef vector<int> vi;
typedef long double ld;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

ll t, ans, last_pos;
string s;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(int x = 1; x <= t; x++){
        cin >> s;
        last_pos = 0;
        for(int i = 1; i < s.size(); i++){
            if(s[i-1] < s[i]){
                last_pos = i;
            }
            else{
                if(s[i-1] > s[i]){
                    s[last_pos]--;
                    for(int j = last_pos + 1; j < s.size(); j++){
                        s[j] = '9';
                    }
                }
            }
        }
        cout << "Case #" << x << ": ";
        for(int i = 0; i < s.size(); i++){
            if(s[i] != '0'){
                cout << s[i];
            }
        }
        cout << endl;

    }
    return 0;
}
