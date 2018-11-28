#include <iostream>
#include <string>

using namespace std;

bool pc[1010];
string s;
int k, n;

int solve(int p)
{
    if(p > n - k) return 0;
    int ret = 0;
    if(!pc[p]){
        for(int i=p;i<p+k;i++){
            pc[i] = !pc[i];
        }
        ret = 1;
    }
    return ret + solve(p+1);
}

int main()
{
    freopen("A-large.in","r", stdin);
    freopen("A-large.out","w", stdout);
    int t;
    cin >> t;
    for(int tc=1;tc<=t;tc++){
        bool possible = true;
        cin >> s >> k;

        n = s.size();

        for(int i=0;i<n;i++){
            pc[i] = (s[i] == '+');
        }
        int ret = solve(0);
        for(int i = n-k;i<n;i++){
            if(!pc[i]) possible = false;
        }
        if(possible)
            cout << "Case #" << tc << ": " << ret << '\n';
        else
            cout << "Case #" << tc << ": IMPOSSIBLE\n";
    }
    return 0;
}
