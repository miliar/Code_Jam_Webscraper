#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("be.txt","r",stdin);
    freopen("ki.txt","w",stdout);
    long long t;
    cin>>t;
    for(long long tc=0;tc<t;tc++) {
        long long n, k;
        cin>>n>>k;
        map<long long,long long> tab;
        tab[-n]=1;
        while(k>0) {
            if(tab.begin()->second<k) {
                long long l=tab.begin()->first;
                long long db=tab.begin()->second;
                k-=db;
                if(tab.count(l/2)==0) {
                    tab[l/2]=0;
                }
                tab[l/2]+=db;
                l++;
                if(tab.count(l/2)==0) {
                    tab[l/2]=0;
                }
                tab[l/2]+=db;
                tab.erase(tab.begin());
            }
            else {
                long long l=tab.begin()->first;
                l*=-1;
                cout<<"Case #"<<tc+1<<": "<<(l/2)<<" "<<((l-1)/2)<<endl;
                k=0;
            }
        }

    }
    return 0;
}
