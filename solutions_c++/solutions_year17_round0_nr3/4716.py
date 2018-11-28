#include<iostream>
#include<string>
#include<queue>
using namespace std;
typedef unsigned long long ull;
typedef pair<ull,ull> pi;
typedef pair<ull,pi> pii;
int main()
{

    int t;
    cin>>t;
    int g=1;
    while(g<=t)
    {
       priority_queue <pii> heap;
       ull n,k;
       cin>>n>>k;
       ull l=1;
       ull r=n;
       pi lr=make_pair(l,r);
       pii vlr=make_pair(n,lr);
       heap.push(vlr);
       //cout<<(heap.top()).first;
       ull v,mid;
       for(ull i=0;i<k;i++)
       {

            vlr=heap.top();
            v=vlr.first;
            l=vlr.second.first;
            r=vlr.second.second;
            heap.pop();
            //cout<<l<<" "<<r<<endl;
            mid=(l+r)/2;
            if(mid-l>0)
            {
                pii vlr1=make_pair(mid-l,make_pair(l,mid-1));
                heap.push(vlr1);
            }
            if(r-mid>0)
            {
                pii vlr1=make_pair(r-mid,make_pair(mid+1,r));
                heap.push(vlr1);
            }


       }
       // cout<<l<<" "<<mid<<endl;
       ull mx=max(mid-l,r-mid);
       ull mn=min(mid-l,r-mid);
       /*while(!heap.empty())
       {
           heap.pop();
           mn=min(mn,heap.top().first);

       }*/










       cout<<"Case #"<<g<<": "<<mx<<" "<<mn<<endl;

       g++;
    }

}
