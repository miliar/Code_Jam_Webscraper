#include<iostream>
#include<map>
#define N 4000006
using namespace std;
int arr[N];
int main()
{
    long long T,t,k,n,i,j,l;
  //  int count=0;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        map<int,int> mp;
        cin>>n>>k;
        mp[n]=1;
        int max,min,par;
        map<int,int>::reverse_iterator rit;
        for(int idx=0;idx<k;idx++)
        {
            rit = mp.rbegin();
            par = rit->first;
            if(par==0) { continue;}
            max=par/2;
            min=par-1-max;
            mp[max]++;
            mp[min]++;
            mp[par]--;
            if(mp[par]==0) mp.erase(par);
        }
        cout<<"Case #"<<t<<": "<<max<<" "<<min<<endl;
    }
  //  cout<<count<<endl;
    return 0;
}
