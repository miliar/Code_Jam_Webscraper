#include<bits/stdc++.h>
using namespace std;

#define l long long
#define ld long double
#define pb push_back
#define mod 10000007
#define ii pair<int,int>
#define jj pair<ii,ii>

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;cin>>t;

    for(int ix=1;ix<=t;ix++){

        printf("Case #%d: ",ix);
        string s;cin>>s;
        bool f=true;
        for(int i=0;i<s.length()-1;i++){
            if(s[i+1]>=s[i]);
            else f=false;
        }
        if(f==false){
            for(int i=0;i<s.length()-1;i++){
                if(s[i+1]<=s[i]){
                    s[i]--;
                    for(int j=i+1;j<s.length();j++)s[j]='9';
                    break;
                }
            }
        }

        int i=0;
        for(;i<s.length();i++){
            if(s[i]!='0')   break;
        }

        for(;i<s.length();i++){
            cout<<s[i];
        }
        cout<<endl;
    }
}
