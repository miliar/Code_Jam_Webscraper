#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int xx=1;xx<=t;xx++){
        long int n;
        cin>>n;
        long int k;
        cin>>k;
        //k--;
        vector<long int> s(log2(n)+1,0);
        vector<long int> scount(log2(n)+1,0);
        //vector<long int> scount1(log2(n)+1,0);
        s[0]=n;
        scount[0]=1;
        for(long long int i=1;i<=log2(n);i++){
            if(s[i-1]%2==0){
                scount[i]+=scount[i-1];
                s[i]=(s[i-1]/2)-1;
                //scount1[i]+=scount[i-1]+2*scount1[i-1];
            }
            else if(s[i-1]%2!=0){
                scount[i]=2*scount[i-1]+pow(2,i-1)-scount[i-1];
                //scount1[i]=scount1[i-1];
                s[i]=(s[i-1]/2);
            }
        }
        long long int l=(long long int)log2(k);
        if(l!=0){
            k=k-(long long )pow(2,l);
        }
        if(k<pow(2,l)-scount[l]){
            long long r=s[l]+1;
            cout<<"Case #"<<xx<<": "<<r/2<<" "<<(r-1)/2<<"\n";
        }
        else{
            long long r=s[l];
            cout<<"Case #"<<xx<<": "<<r/2<<" "<<(r-1)/2<<"\n";
        }
    }
    return 0;
}
