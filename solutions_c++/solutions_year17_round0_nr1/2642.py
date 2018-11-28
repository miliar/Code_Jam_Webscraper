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
     string ss; int k;
        cin>>ss>>k;
        int n = ss.size();
        int inverses = 0;
        int state = 0;
        queue<int> flips;


        for (int i=0;i<n-k+1;i++){
            while (!flips.empty() && flips.front()<=i ){
                flips.pop(); state^=1;
            }
            int val = (ss[i]=='+') ^ state;
            if (val == 0){
                inverses++;
                state^=1;
                flips.push(i + k);

            }


        }
        for (int i=n-k+1;i<n;i++){
          while (!flips.empty() && flips.front()<=i ){
                flips.pop(); state^=1;
            }
            int val = (ss[i]=='+') ^ state;
            if (val == 0)
                return (void)(cout<<"IMPOSSIBLE\n");
        }



        cout<<inverses<<endl;


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
    }



}
