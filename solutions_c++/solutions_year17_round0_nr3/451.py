#include<bits/stdc++.h>
using namespace std;
map<long long,long long> ma;
void solve(int xxx)
{
    long long n,k;
    ma.clear();
    cin>>n;
    ma[n]=1;
    cin>>k;
    while(k){
        map<long long int,long long int> :: iterator it=ma.end(); it--;
        k-=(*it).second;
        if(k<=0){
            cout<<"CASE #"<<xxx<<": "<<(*it).first/2<<" "<<((*it).first-1)/2<<'\n';
            return ;
        }
        ma[(*it).first/2]+=(*it).second;
        ma[((*it).first-1)/2]+=(*it).second;
        ma.erase(it);
    }
}
int main()
{
    int t;
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++) solve(i);
}
