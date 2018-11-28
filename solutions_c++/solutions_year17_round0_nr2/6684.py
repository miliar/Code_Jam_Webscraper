#include <iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int main() {
    int t;
    cin>>t;
    for(int xx=1;xx<=t;xx++){
        long long int tstcase;
        cin>>tstcase;
        if(tstcase==0){
            cout<<"Case #"<<xx<<": 0\n";
        }
        else{
            long long int ans=0;
            for(long long int x=1;x<=tstcase;x++){
                long long int ctr=0,len=0,temp=x;
                while(temp>0){
                    len++;
                    if(temp%10>=(temp/10)%10){
                        ctr++;
                    }
                    temp=temp/10;
                }
                if(ctr==len){
                    ans=x;
                }
            }
            cout<<"Case #"<<xx<<": "<<ans<<"\n";
        }
    }
    return 0;
}