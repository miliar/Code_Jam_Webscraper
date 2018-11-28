#include <bits/stdc++.h>
using namespace std;
void Solve();
int main(){
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    int t; cin>>t;
    for(int i=1;i<=t;i++){
         cout<<"Case #"<<i<<": ";
         Solve();
    }
    return 0;
}

void Solve(){
    string str;
    cin>>str;
    int l_break = -1;
    if(str.length()==1){cout<<str<<"\n";return;}

    for(int i=1;i<str.length();i++){
        if(str[i]<str[i-1]){
            l_break = i-1;
            break;
        }
    }
    if(l_break==-1){cout<<str<<"\n";return;}
    while(l_break>=1){
       if(str[l_break]==str[l_break-1]) l_break--;
       else break;
    }
    if(l_break==0){
        str[0]--;
        if(str[0]=='0'){
            for(int i=1;i<str.length();i++) cout<<"9";
        }
        else{
            cout<<str[0];
            for(int i=1;i<str.length();i++) cout<<"9";
        }
        cout<<"\n"; return;
    }

    else{
        for(int i=0;i<str.length();i++){
            if(i<l_break) cout<<str[i];
            else if(i==l_break){
                str[i]--;
                cout<<str[i];
            }
            else cout<<"9";
        }
        cout<<"\n"; return;
    }

}