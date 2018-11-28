#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

int main(){
    int t;cin>>t;
    int caseno=1;
    while(t--){
        string s;cin>>s;
        int k;cin>>k;int slen=s.length();
        vector<int> f(slen,0);
        int count=0;
        for(int i=0;i<=slen-k;i++){
            if(s[i]=='-' && f[i]%2==0){
                for(int j=i;j<i+k;j++){
                    f[j]++;
                }
                count++;
            }
            else if(s[i]=='+' && f[i]%2==1){
                for(int j=i;j<i+k;j++){
                    f[j]++;
                }
                count++;
            }
        }
        bool poss=true;
        for(int i=0;i<slen;i++){
            if((s[i]=='-' && f[i]%2==0) || (s[i]=='+' && f[i]%2==1)){
                poss=false;
            }
        }
        if(poss)cout<<"Case #"<<caseno<<": "<<count<<endl;
        else cout<<"Case #"<<caseno<<": "<<"IMPOSSIBLE"<<endl;
        caseno++;
    }
}
