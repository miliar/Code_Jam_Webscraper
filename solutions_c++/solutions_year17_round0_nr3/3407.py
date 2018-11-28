#include <iostream>
#include <map>
using namespace std;

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--){
    tci++;
    cout<<"Case #"<<tci<<": ";
    long long n,k;
    cin>>n>>k;
    map<long long,long long,greater<long long> > mp;
    mp[n]++;
    long long c1,c2;
    long long i;
    map<long long,long long>::iterator it;
    for(i=0;i<k;i++)
    {
        it=mp.begin();
        (it->second)--;
        long long len=it->first;
        c1=(len-1)/2;
        c2=len-1-c1;
        if(it->second==0)mp.erase(it);
        if(c1!=0)mp[c1]++;
        if(c2!=0)mp[c2]++;
    }
    cout<<max(c1,c2)<<" "<<min(c1,c2)<<endl;
    }
    return 0;
}
