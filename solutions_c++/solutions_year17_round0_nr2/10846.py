#include <bits/stdc++.h>
using namespace std;
string make(string s){
    int len=s.length();
    string ans="";
    int i;
    for(i=0;i<len-1;i++){
        ans+='9';
    }
    return ans;
}
bool check(string s,int len){
    for(int i=0;i<len-1;i++){
        if(s[i]=='1' && s[i+1]=='0') return true;
    }
    return false;
}
int main()
{
    int t,i,j;
    long long x;
    cin>>t;
    for(i=1;i<=t;i++){
        cout<<"Case #"<<i<<": ";
        cin>>x;
            string s=to_string(x);
            if(check(s,s.length()))
                cout<<make(s);
        else if(x<10) cout<<x;
        else{
            string s=to_string(x);
            int len = s.length();
            for(j=0;j<len-1;j++){
                if(s[j]>s[j+1]){
                    int idx=j;
                    bool ch=0;
                    while(1){
                       if(idx>0 && s[idx]-'0'-1<s[idx-1]-'0') {s[idx--]='9';ch=1;}
                       else break;
                    }
                    if(!ch)
                    s[j]=(s[j]-'0'-1)+'0';
                    else 
                    s[idx]=(s[idx]-'0'-1)+'0';
                    
                    j++;
                    while(j<len) s[j++]='9';
                    break;
                }
            }
            cout<<s;
        }
        cout<<endl;
    }
    return 0;
}
