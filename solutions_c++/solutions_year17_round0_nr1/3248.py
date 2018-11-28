#include <stdio.h>
#include <bits/stdc++.h>

#include <string.h>
#include <math.h>
#include <stdlib.h>

using namespace std;
int main() {
    int t;cin>>t;
    int testcase=1;
    
    while(t--){
        int k;
        string s;
        cin>>s>>k;
        int count=0;
        //cout<<s.length();
        for(int i=0;i<s.length();i++){
            if(s[i]=='+'){
                //cout<<"skipping index"<<i<<endl;
            }
            else if(s[i]=='-'){
            //    cout<<"found - at index "<<i<<endl;
                if(i+k>s.length()){break;}
                for(int j=i;j<i+k;j++){
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
            //        cout<<"flipped index"<<j<<" "<<s<<endl;
                    
                                    }
                count++;

            }
            
        }
        for(int i=0;i<s.length();i++){
                if(s[i]=='-')count=-1;
            }
            cout<<"Case #"<<testcase++<<": ";
            if(count>=0)cout<<count<<endl;
            else cout<<"Impossible"<<endl;
            //cout<<s[i]<<endl;
    }
    return 0;
}
