#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
int main(){
        int flag;
        cin>>flag;
        for(int ptr=1;ptr<=flag;ptr++){
            long long no;
            cin>>no;
            long long kp;
            cin>>kp;
            vector<long long> s(log2(no)+1,0);
            vector<long long> scount(log2(no)+1,0);
            s[0]=no;
            scount[0]=1;
            for(long long i=1;i<=log2(no);i++){
                if(s[i-1]%2==0){
                    scount[i]+=scount[i-1];
                    s[i]=(s[i-1]/2)-1;
                }
                else if(s[i-1]%2!=0){
                    scount[i]=2*scount[i-1]+pow(2,i-1)-scount[i-1];
                    s[i]=(s[i-1]/2);
                }
            }
            long long l=(long long )log2(kp);
            if(l!=0){
                kp=kp-(long long )pow(2,l);
            }
            if(kp<pow(2,l)-scount[l]){
                long long r=s[l]+1;
                cout<<"Case #"<<ptr<<": "<<r/2<<" "<<(r-1)/2<<"\n";
            }
            else{
                long long r=s[l];
                cout<<"Case #"<<ptr<<": "<<r/2<<" "<<(r-1)/2<<"\n";
            }
        }
        return 0;
}
