#include <iostream>
#include <map>
using namespace std;

void out(long long v)
{
    cout<<v/2<<' ';
    if(v%2==1) cout<<v/2;
    else cout<<v/2-1;
    cout<<endl;
}

void mymain(int t)
{
    long long n,k;
    map<long long, long long> mp;
    map<long long, long long>::iterator itr;
    cin>>n>>k;
    cout<<"Case #"<<t<<": ";
    mp.insert(make_pair(n,1));
    while(true)
    {
        itr=mp.end();
        itr--;
        if(itr->second>=k)
        {
            out(itr->first);
            return;
        }
        k-=itr->second;
        mp[itr->first/2]+=itr->second;
        if(itr->first%2==1) mp[itr->first/2]+=itr->second;
        else mp[itr->first/2-1]+=itr->second;
        mp.erase(itr->first);
    }
}

int main()
{
    int t,T;
    cin>>T;
    for(t=0;t<T;t++) mymain(t+1);
    return 0;
}
