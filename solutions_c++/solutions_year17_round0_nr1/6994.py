#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int main(){
    freopen("A.in", "r", stdin); // redirects standard input
    freopen("outputA.out", "w", stdout); // redirects standard output
    int i,j,t,k,f,l=0;
    cin>>t;
    long ans;
    string s;
    while(t--){
        cin>>s;
        cin>>k;
        ans=0;
        l++;
        f=1;
        for(i=0;i<s.length();++i){
            if(s[i]=='-'){
                ans++;
                if(i+k-1>=s.size()){
                    cout<<"Case #"<<l<<": IMPOSSIBLE\n";
                    f=0;
                    break;
                }
                for(j=i;j<i+k;j++){
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
                //cout<<s<<endl;
            }
        }
        if(f)
            cout<<"Case #"<<l<<": "<<ans<<endl;
    }
    return 0;
}
