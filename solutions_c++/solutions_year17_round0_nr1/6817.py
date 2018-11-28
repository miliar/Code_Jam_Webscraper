#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int  MOD=1000000007;
const int  INF= int(1e9);

int main()
{
    ios_base::sync_with_stdio(false);
    int testCases;
    cin>>testCases;
    for(int tc=1;tc<=testCases;tc++) {
        string s;
        int k;
        cin>>s>>k;
        int sz = s.size(),res=0;
        for(int i=0;i<sz;i++) {
            if(s[i] == '-' && i+k-1 < sz) {
                for(int cnt=0; cnt<k;cnt++) {
                    s[i+cnt]=(s[i+cnt] == '+' ? '-' : '+');
                }
                res++;
            }
        }
        bool ok =true;
        for(int i=0;i<sz;i++) {
            if(s[i] == '-') {
                ok=false;
                break;
            }
        }
        if(ok) {
            cout<<"Case #"<<tc<<": "<<res<<"\n";
        } else {
            cout<<"Case #"<<tc<<": "<<"IMPOSSIBLE"<<"\n";
        }

    }
    return 0;

}
