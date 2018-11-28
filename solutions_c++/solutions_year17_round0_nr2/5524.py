#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("input.in","r",stdin);
    freopen("gc_out2.txt","w",stdout);
    int t;
    cin>>t;
    int k=1;
    while(t--){
        string s;
        cin>>s;
        cout<<"Case #" << k << ": ";
        if(s.length()==1){
            cout << s << endl;
        }else{
            int flag=0;
            for(int i=0; i<s.length()-1; i++){
                if(s[i]-'0'>s[i+1]-'0'){
                    flag=1;
                }
            }
            if(flag){
                int br=0;
                for(int i=0; i<s.length()-1; i++){
                    if(s[i]-'0'>s[i+1]-'0'){
                        br=i;
                        break;
                    }
                }
                while(s[br]==s[br-1] && br>0){
                    br--;
                }
                for(int i=0; i<s.length(); i++){
                    if(i<br){
                        if(i==0){
                            if(s[i]!='0')cout << s[i];
                        }else{
                            cout<<s[i];
                        }
                    }
                    if(i==br){
                        if(i==0){
                            if(s[i]!='1')cout << (s[i]-'0')-1;
                        }else{
                            cout << (s[i]-'0')-1;
                        }
                    }
                    if(i>br) cout<<9;
                }
                cout << endl;
            }else{
                cout << s << endl;
            }
        }
        k++;
    }
}
