#include <iostream>
#include <bits/stdc++.h>

#define ll long long int

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,i,n,j;
    string s;
    cin>>t;
   // cout<<t<<endl;
    for(j=1;j<=t;j++){
        cin>>s;
        n=s.size();
        int cnt=1;
       while(cnt==1){
            ll temp=n;
            cnt=0;
            for(i=0;i<n-1;i++){
                if(s.at(i)>s.at(i+1)){
                    cnt=1;
                    ll c=(ll)(s.at(i)-'0');
                    if(c==0){
                        s.at(i)='9';
                    }
                    else{
                        s.at(i)=(char)(48+c-1);
                    }
                    temp=i;
                    break;
                }
            }
            for(i=temp+1;i<n;i++){
                s.at(i)='9';
            }
        }
        ll counter=0;
        cout<<"Case #"<<j<<": ";
        for(i=0;i<n;i++){
            if(s.at(i)!='0'){
                counter=1;
            }
            if(counter==0){
                continue;
            }
            cout<<s.at(i);
        }
        printf("\n");
    }
    return 0;
}
