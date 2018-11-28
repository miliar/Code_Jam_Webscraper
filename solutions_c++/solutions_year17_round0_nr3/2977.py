#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long ll;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("cc3.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        ll n,k;
        cin>>n>>k;
        ll r=k;
        ll ls=1;//level size
        pair<ll,ll>c1=make_pair(n,1);
        pair<ll,ll>c2=make_pair(0,0);
        while(r>ls){
            pair<ll,ll>nC1=make_pair(0,0);
            pair<ll,ll>nC2=make_pair(0,0);
            if(c1.first%2==0){
                nC1=make_pair(c1.first/2,c1.second);
                nC2=make_pair(c1.first/2-1,c1.second);

            }else{
                nC1=make_pair(c1.first/2,c1.second*2);
            }
            if(c2.second!=0){
                ll splits[2];
                splits[0]=c2.first/2;
                splits[1]=(c2.first-1)/2;
                for(int j=0;j<2;j++){
                    ll temp=splits[j];
                    if(nC1.first==temp){
                        nC1.second+=c2.second;
                    }else if(nC2.second!=0){
                        if(nC2.first!=temp)cout<<"something went wrong";
                        nC2.second+=c2.second;
                    }else{
                        nC2.first=temp;
                        nC2.second=c2.second;
                    }
                }
            }
            c1.first=nC1.first;
            c1.second=nC1.second;
            c2.first=nC2.first;
            c2.second=nC2.second;
            r-=ls;
            ls<<=1;
        }
        ll larger,smaller;
        ll lC,sC;
        if(c1.first>c2.first){
            larger=c1.first;
            lC=c1.second;
            smaller=c2.first;
            sC=c2.second;
        }else{
            larger=c2.first;
            lC=c2.second;
            smaller=c1.first;
            sC=c1.second;
        }
        ll last=(r<=lC)?(larger):(smaller);
        cout<<"Case #"<<i+1<<": "<<last/2<<" "<<(last-1)/2<<endl;
    }
    return 0;
}
