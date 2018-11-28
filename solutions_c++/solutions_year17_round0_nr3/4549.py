#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.out","w",stdout);
    long long int T,i,j,n,k,v,mx;
    string str;
    cin>>T;
    multiset<long long int> ms;
    v=T;
    while(T--)
    {
        cin>>n>>k;
        ms.insert(n);
        for(i=0;i<k-1;i++)
        {
            mx=*ms.rbegin();
            auto itr=ms.find(mx);
            if(itr!=ms.end())
                ms.erase(itr);
            if(mx%2==0)
            {
                ms.insert(mx/2);
                ms.insert((mx/2) - 1);
            }
            else
            {
                ms.insert(mx/2);
                ms.insert(mx/2);
            }
        }
        mx=*ms.rbegin();
        //cout<<ms.size()<<" ";
        cout<<"Case #"<<v-T<<": ";
        if(mx%2==0)
        {
            if(mx>=2)
                cout<<mx/2<<" "<<(mx/2) - 1;
            else
                cout<<"0 0";
        }
        else
            cout<<mx/2<<" "<<mx/2;
        ms.clear();
        cout<<endl;
    }
}
