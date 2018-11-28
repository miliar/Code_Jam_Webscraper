#include<bits/stdc++.h>
#define ll long long
#define mp make_pair
#define pb push_back
#define vll vector<long long>
#define cd complex<double>
#define pll pair<long long, long long>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int i,j,n,k,t,cases,res;
    string s;
    cin>>t;
    cases=1;
    while(t--){
        cin>>s>>k;
        n=s.length();
        bool b[n+1];
        memset(b,0,sizeof b);
        res=0;
        for(i=0;i<=n-k;i++){
            if(!b[i] && s[i]=='-'){
                res++;
                for(j=1;j<k;j++){
                    b[i+j] = !b[i+j];
                }
            }
            if(b[i] && s[i]=='+'){
                res++;
                for(j=1;j<k;j++){
                    b[i+j] = !b[i+j];
                }
            }
        }
        for(i=n-k+1;i<n;i++){
            if((b[i] && s[i]=='+')||(!b[i] && s[i]=='-')){
                res=-1;
            }
        }
        cout<<"Case #"<<cases<<": ";
        if(res==-1)cout<<"IMPOSSIBLE\n";
        else cout<<res<<"\n";
        cases++;
    }
}
