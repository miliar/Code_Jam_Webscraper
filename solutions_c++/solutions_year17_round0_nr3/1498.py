#include <bits/stdc++.h>

using namespace std;


int main()
{
//
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    long long n,k,Neven,Nodd;
    cin>>t;
    for(int tc=1;tc<=t;tc++){
        map<long long,long long> mp;
        cin>>n>>k;
        mp[n]=1;
        long long temp=n,temp2;
        while(temp){
            temp2=temp+1;
            if(temp%2==0){
                mp[(temp-1)/2]+=mp[temp];
                mp[(temp-1)/2+1]+=mp[temp];
            }else mp[(temp-1)/2]+=2*mp[temp];

            if(temp2%2==0){
                mp[(temp2-1)/2]+=mp[temp2];
                mp[(temp2-1)/2+1]+=mp[temp2];
            }else mp[(temp2-1)/2]+=2*mp[temp2];
            temp=(temp-1)/2;
        }
        long long a,b;
        temp=n;
        while(1){
            temp2=temp+1;
            if(k-mp[temp2]>0){
                k-=mp[temp2];
            }else if(k-mp[temp2]<=0){
                if(temp2%2==0){
                    a=(temp2-1)/2;
                    b=a+1;
                }else{
                    a=(temp2-1)/2;
                    b=a;
                }
                break;
            }
            if(k-mp[temp]>0){
                k-=mp[temp];
            }else if(k-mp[temp]<=0){
                if(temp%2==0){
                    a=(temp-1)/2;
                    b=a+1;
                }else{
                    a=(temp-1)/2;
                    b=a;
                }
                break;
            }
            temp=(temp-1)/2;
        }
        cout<<"Case #"<<tc<<": "<<b<<" "<<a<<endl;
    }



}
