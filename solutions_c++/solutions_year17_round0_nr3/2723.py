#include <bits/stdc++.h>
using namespace std;
long long st,en;
void div(long long lo,long long hi,long long p)
{
    long long mid  = (hi+lo)/2;
    if(p == 1)
    {
        st = mid-lo;
        en = hi-mid;
        return;
    }
    if((p-1)%2 == 0)
    {
        if(hi-mid>lo-mid)
        {
            div(lo,mid-1,(p-1)/2);
        }
        else
        {
            div(mid+1,hi,(p-1)/2);
        }

    }
    else
    {
        if(hi-mid>lo-mid)
        {
            div(mid+1,hi,(p)/2);
        }
        else
        {
            div(lo,mid-1,(p)/2);
        }

    }
}
int main()
{
    long long T;
    cin>>T;
    for(long long t = 1;t<=T;t++)
    {
        long long s,p;
        cin>>s>>p;
        div(1,s,p);
        cout<<"Case #"<<t<<": ";
        cout<<en<<" "<<st<<endl;





    }

}
