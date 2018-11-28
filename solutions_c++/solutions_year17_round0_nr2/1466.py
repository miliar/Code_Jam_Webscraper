#include <bits/stdc++.h>
#define F first
#define S second
using namespace std;

typedef long long ll;


string solve();
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //freopen("output.txt", "w", stdout);
    srand(time(0));
    int t;
    int i = 0;
    cin >> t;
    while(t--){
        ++i;
        string y = solve();
        cout << "Case #" << i << ": ";
        reverse(y.begin(), y.end());
        while(!y.empty() && y.back() == '0')y.pop_back();
        if(y.empty())y.push_back('0');
        reverse(y.begin(), y.end());
        cout << y << endl;
        //if(y >= 0)cout << y << endl;
        //else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
#define many(x, y) v[y + x] + u[maxn + y - x]
#define mp(x, y) make_pair(x, y)


bool check(ll t){
    vector<int> c;
    while(t){
        c.push_back(t % 10);
        t /= 10;
    }
    bool ok = true;
    for(int i = 1; i < c.size(); ++i)
        ok &= c[i] < c[i - 1];
    return ok;
}

string solve(){
    string n;
    cin >> n;
    for(int i = 1; i < n.size(); ++i){
        if(n[i] < n[i - 1]){
            for(int j = i; j < n.size(); ++j)
                n[j] = '9';
            n[--i] -= 1;

            while(i > 0){
                if(n[i] < n[i - 1]){
                    n[i] = '9';
                    n[--i] -= 1;
                }
                else break;
            }
            return n;
        }
    }
    return n;
}



int solveA(){

string h;
int r[1000];
int s = 0;
int k;
int ans;
    cin >> h >> k;
    s = 0;
    ans = 0;
    for(int i = 0; i < h.size(); ++i){
        if(i + k > h.size() && h[i] == '-'){
            //cerr << i << endl;
            return -1;
        }
        if(h[i] == '-'){
            ++ans;
            for(int j = i; j < i + k; ++j)
                if(h[j] == '-')h[j] = '+';
                else h[j] = '-';
        }
    }
    return ans;
}
