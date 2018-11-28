#include<bits/stdc++.h>
using namespace std;
bool ok(int n){
    stringstream ss;
    ss<<n;
    string s;
    ss>>s;
    for(int i=1;i<(int)s.size();i++){
        if(s[i-1]>s[i])return 0;
    }
    return 1;
}
int main(){
    freopen("in.in","r",stdin);
    freopen("in.out","w",stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        int n;
        cin>>n;
        do{
            if(ok(n)){
                cout<<"Case #"<<z<<": "<<n<<"\n";
                break;
            }
        }while(--n);
    }
    return 0;
}
