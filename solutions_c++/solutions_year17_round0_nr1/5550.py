#include <bits/stdc++.h>
using namespace std;

int a[1001];

int main(){
    freopen("input.in","r",stdin);
    freopen("gc_out4.txt","w",stdout);
    int t;
    cin>>t;
    int cm=1;
    while(t--){
        string s;
        cin>>s;
        int k; cin>>k;
        int n=s.length();
        for(int i=0; i<n; i++){
            if(s[i]=='+') a[i]=1;
            else a[i]=0;
        }
        int ans = 0;
        for(int i=0; i<n; i++){
            if(a[i]==0 && i+k-1 < n){
                ans++;
                for(int j=i; j<=i+k-1; j++){
                    a[j]=abs(1-a[j]);
                }
            }
        }
        int flag = 1;
        for(int i=0; i<n; i++){
            if(!a[i]) flag = 0;
        }
        if(flag){
            cout << "Case #"<<cm<<": "<< ans << endl;
        }else{
            cout << "Case #" << cm<<": IMPOSSIBLE" << endl;
        }
        cm++;
    }
}
