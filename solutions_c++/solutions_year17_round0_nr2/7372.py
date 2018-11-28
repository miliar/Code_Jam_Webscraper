#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int t;
    int l,r;
    int val=0;
    string str;
    int case_no=0;
    cin>>t;
    while(t--){
        ++case_no;
        // str=to_string(val);
        // val++;
        // cout<<val-1<<":";
        cin>>str;
        l=0;
        r=INT_MAX;
        bool only1=true;
        cout<<"Case #"<<case_no<<": ";
        // cout<<str<<":";
        if(str.length()==1){
            cout<<str<<"\n";
            continue;
        }
        if(str[0]!='1')only1=false;
        for(int i=1;i<str.length();i++){
            if(str[i]<str[i-1]){
                int j=i;
                r=i;
                // str[i]='9';
                // str[i-1]--;
                while(j>=1){
                    if(str[j]<str[j-1]){
                        str[j]='9';
                        str[j-1]--;
                        j--;
                    }
                    else{
                        break;
                    }
                    
                }
                
                break;
            }
            if(str[i]!='1')
            only1=false;
        }
        if(str[0]<='0')l=1;
        // cout<<val<<":";
        bool bc=false;
        for(int i=l;i<str.length();i++){
            if(i==r){
                bc=true;
            }
            if(bc==true){
                cout<<"9";
            }
            else{
                cout<<str[i];
            }
        }
        cout<<"\n";
        
    }
    return 0;
}

