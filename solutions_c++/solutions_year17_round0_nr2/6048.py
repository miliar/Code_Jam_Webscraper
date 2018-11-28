#include<bits/stdc++.h>
#define r0 return 0
#define ll long long
using namespace std;
ll t,n;
ll cou(ll z){
    ll c=1;
    while(z/10!=0){
        c++;
        z=z/10;
    }
    return c;
}
ll pw(ll x){
    ll res=1,c=0;
    while(c<x){
        res=res*10;
        c++;
    }
    return res;
}
int main(){
    fstream file;
  	file.open("tidy.txt",ios::out);
    cin>>t;
    ll i;
    for(i=1;i<=t;i++){
        cin>>n;
        if(n/10==0)file<<"Case #"<<i<<":"<<" "<<n<<endl;
        else{
                ll c=cou(n);
               // cout<<c<<endl;
                ll a[c+1],j,p=c,x=n;
                for(j=1;j<=c;j++){
                    ll l=pw(p-1);
                  //  cout<<l<<endl;
                    a[j]=x/l;
                   // cout<<a[j]<<endl;
                    x=x%l;
                    p--;
                }
                ll g=0;
                for(j=1;j<c;j++){
                    if(a[j]>a[j+1]){
                        if(a[j]-1>=a[j-1]&&j>1){
                        a[j]=a[j]-1;
                        for(p=j+1;p<=c;p++){
                            a[p]=9;
                        }
                        }
                        else{
                                g=1;
                            break;
                        }
                }}
                if(g==1){
                for(j=j;j>1;j--){
                    if(a[j]-1>=a[j-1]){
                        break;
                    }
                }
                a[j]=a[j]-1;
                for(j=j+1;j<=c;j++){
                    a[j]=9;
                }}
                ll sum=0;
                for(j=1;j<=c;j++){
                        sum=sum*10+a[j];
                }
                file<<"Case #"<<i<<":"<<" "<<sum<<endl;
        }
    }
    r0;
}
