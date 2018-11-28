#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("tidy_number_large.out","w",stdout);
    long long tc,i,j,k,l,t;
    cin>>t;
    string s;
    for(tc=1;tc<=t;tc++){
        cin>>s;
        l=s.length();
        i=0;
        while(i<(l-1) && s[i]<=s[i+1]){
            i++;
        }
        if(i==l-1){
            cout<<"Case #"<<tc<<": "<<s;
            cout<<"\n";
            continue;
        }
        j=i;k=i;
        for(j=i+1;j<l;j++){
            s[j]='9';
        }
        if(s[k]=='0'){
        }
        else{
            s[k]=((char)(s[k]-1));
        }
        while(k>=1 && s[k-1]>s[k]){
            if(s[k-1]=='0'){
            }
            else{
                s[k]='9';
                s[k-1]=((char)(s[k-1]-1));
            }
            k--;
        }
        j=0;
        if(s[j]=='0'){
            j++;
        }
        cout<<"Case #"<<tc<<": ";
        while(j<l){
            cout<<s[j];
            j++;
        }
        cout<<"\n";
    }
return 0;
}
