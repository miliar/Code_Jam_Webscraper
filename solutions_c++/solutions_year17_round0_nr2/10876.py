#include <bits/stdc++.h>

using namespace std;
#define ll long long int
vector<int> v,v1;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    ll n,t;
    cin >> t;
    for(int a=1;a<=t;a++){
        cin >> n;
    for(int i=n;i>=1;i--){
        int q=i;int w=10;int fl=0;
        while(q>0){
            int r=q%10;
            if(r<=w){
                w=r;
            }
            else{
                fl=1;
            }
            q=q/10;
        }
        if(!fl){
            cout<<"Case #"<<a<<": "<<i<<endl;
            break;
        }
    }
    }
}
