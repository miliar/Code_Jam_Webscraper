#include<iostream>
#include<map>
using namespace std;
int main(){
    int t;
    cin>>t;
    int cas=0;
    while(t--){
        map<long long,long long> mp;
        long long n,k;
        cin>>n>>k;
        mp[n]=1;
        long long use=0;
        while(!mp.empty()){
            map<long long,long long>::reverse_iterator rit=mp.rbegin();
            long long time=rit->second;
            long long val=(rit->first);
            long long l=val/2;
            long long r=val/2;
            if(val%2==0){
                l--;
            }

            //cout<<l<<" "<<r<<endl;

            if(use+time>=k){
                cout<<"Case #"<<++cas<<": "<<r<<" "<<l<<endl;
                break;
            }

            mp.erase(val);

            use+=time;
            if(mp.find(l)!=mp.end()){
                mp[l]+=time;
            }
            else{
                mp[l]=time;
            }

            if(mp.find(r)!=mp.end()){
                mp[r]+=time;
            }
            else{
                mp[r]=time;
            }
        }

    }
}
