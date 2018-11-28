#include <bits/stdc++.h>
#define ll long long
#define ull unsigned ll

using namespace std;
#define MAXN 150001
#define files(x) freopen((x+string(".dat")).c_str(), "r", stdin); //freopen((x+string(".sol")).c_str(), "w", stdout);



#define MAXN 1000001
#define input_file(x) freopen((x+string(".txt")).c_str(), "r", stdin);
#define output_file(x) freopen((x+string(".txt")).c_str(), "w", stdout);
vector<int> g[MAXN];
bool used[MAXN];
ll timer, tin[MAXN], fup[MAXN];
 ll k,n,m;


void solve(){
    string s;
    cin>>s;
    int n = s.size();
    int min_n = 9;
    for (int i=0;i<n;i++){
        min_n = min(min_n, s[i] - '0');
    }

    int last_good = 0;
    for (int i=1;i<n;i++){

        if (s[i] < s[i-1]){
            s[last_good] -=1;
            for (int j=last_good+1;j<n;j++)
                s[j] = '9';
            break;
        } else if (s[i] > s[i-1])
            last_good = i;

    }
    for (int i=0;i<n;i++)
        if (i==0 && s[i]=='0')
        continue;  else
        cout<<s[i];






}

main () {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    input_file("input");
    output_file("output");

    int t;
    cin>>t;
    for (int i=0;i<t;i++){

        cout<<"Case #"<<i+1<<": ";
        solve();
         cout<<endl;
    }



}
