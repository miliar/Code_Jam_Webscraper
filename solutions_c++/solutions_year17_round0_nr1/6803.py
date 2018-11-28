#include <bits/stdc++.h>

#define ll long long
#define de(x) cout<<#x<<": "<<x<<endl

using namespace std;

int b[1000001];

int main() {
     
    ios::sync_with_stdio(false);
    int n,l;
    cin>>n;
    string t;
    map<char,char> k;
    k['+']='-';
    k['-']='+';
    for(int i=1;i<=n;i++){
        cin>>t>>l;
        int k1=t.length();
        int count=0;
        for(int j=0;j<=k1-l;j++){
            if(t[j]=='-'){
                for(int g=j;g<j+l;g++){
                    t[g]=k[t[g]];
                }
                count++;
            }
        }
        for(int j=k1-1;j>k1-l;j--){
            if(t[j]=='-'){
                count=-1;
                break;
            }
        }
        if(count==-1){
            cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
        }
        else{
            cout<<"Case #"<<i<<": "<<count<<endl;
        }
    }

} 