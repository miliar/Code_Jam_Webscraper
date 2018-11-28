#include<bits/stdc++.h>
using namespace std;
int main(){
    #ifndef ONLINE_JUDGE
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);
    #endif
    int t;
    cin>>t;
    int k=1;
    while(k<=t){
        long long n;
        cin>>n;
        long long i=n;
        int flag=0;
        //cout<<i<<endl;
        for(;i>0;i--){
            long long a=i;
            vector<int> x;
            //cout<<"a= "<<a<<endl;
            while(a!=0){
                x.push_back(a%10);
                a=a/10;
                //cout<<a<<endl;
                //int temp;
                //cin>>temp;
            }
            flag=0;
            for(typeof(x.rbegin()) it=x.rbegin()+1;it!=x.rend();it++){
                if(*it<*(it-1)){
                    flag=1; break;
                }
            }
            //cout<<i<<endl;
            if(flag==0){
                cout<<"Case #"<<k<<": "<<i<<endl;break;
            }
        }
        if(flag==1)cout<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<endl;

        k++;
    }
    return 0;
}
