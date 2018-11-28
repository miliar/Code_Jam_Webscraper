#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int  MOD=1000000007;
const int  INF= int(1e9);

ll anyBasetoDecimal ( string r,ll b) {
    ll p=1,res=0;
    for(int i=r.size()-1;i>=0;i--) {
        ll d=(r[i]<='9'? r[i]-'0' : r[i]-'A'+10);
        res+=d*p;
        p*=b;
    }
    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    int testCases;
    cin>>testCases;
    for(int k=1;k<=testCases;k++) {
        string n;
        cin>>n;
        int sz = n.size();
        while (1) {
            bool mistake=false;
            for(int i=0;i<sz-1;i++) {
                if(n[i] > n[i+1]){
                    n[i] --;
                    for(int j=i+1;j<sz;j++) {
                        n[j]='9';
                    }
                    mistake=true;
                    break;
                }
            }
            if(!mistake){
                break;
            }
        }

        ll res=anyBasetoDecimal(n,10);
        cout<<"Case #"<<k<<": "<<res<<"\n";
    }
    return 0;

}
