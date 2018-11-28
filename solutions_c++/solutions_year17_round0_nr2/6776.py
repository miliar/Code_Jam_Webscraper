#include <bits/stdc++.h>

#define ll long long
#define de(x) cout<<#x<<": "<<x<<endl
#define INF 99999

using namespace std;

int main() {
    
    ios::sync_with_stdio(false);

    int n;
    cin>>n;
    string t;
    for(int i=1;i<=n;i++){
        cin>>t;
        int k=t.length();
        int h=k;
        while(k--){
            for(int j=0;j<h-1;j++){
                if(t[j]>t[j+1]){
                    t[j]=t[j]-1;
                    for(int f=j+1;f<h;f++){
                        t[f]='9';
                    }
                    break;
                }
            }
        }
        cout<<"Case #"<<i<<": ";
        if(t[0]!='0'){
            cout<<t[0];
        }
        for(int j=1;j<h;j++){
            cout<<t[j];
        }
        cout<<endl;
    }

}