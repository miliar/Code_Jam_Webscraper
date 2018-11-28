#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("oversized_pancakes_large0.out","w",stdout);
    long long tc,i,j,k,l,t,c;
    cin>>t;
    string s;
    for(tc=1;tc<=t;tc++){
        cin>>s>>k;
        l=s.length();
        i=0;c=0;
        while(i<l){
            if(s[i]=='-'){
                if((i+k-1)>=l){
                   c=-1;
                   break;
                }
                for(j=i;j<=(i+k-1);j++){
                    if(s[j]=='+'){
                        s[j]='-';
                    }
                    else{
                        s[j]='+';
                    }
                }
                c++;
            }
            i++;
        }
        if(c==-1){
            cout<<"Case #"<<tc<<": IMPOSSIBLE\n";
        }
        else{
            cout<<"Case #"<<tc<<": "<<c<<"\n";
        }
    }
return 0;
}
