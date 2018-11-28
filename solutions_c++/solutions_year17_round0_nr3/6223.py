#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        long int n,k;
        cin>>n>>k;
        multiset<long int> s;
        s.insert(n);
        cout<<"Case #"<<j<<": ";
        for(int i=0;i<k-1;i++)
        {
            int x=*(s.rbegin());
            //cout<<x;
            s.erase(--s.end());
            if(x%2==0)
            {
                s.insert(x/2);
                if((x/2)-1<0)
                    s.insert(0);
                else
                    s.insert((x/2)-1);
            }
            else
            {
                s.insert(x/2);
                s.insert(x/2);
            }
        }
        int x=*(s.rbegin());
        //cout<<x;

        if(x%2==0)
        {
            cout<<x/2<<" ";
            if(((x/2)-1)<0)
                cout<<0;
            else
                cout<<(x/2)-1;
            cout<<"\n";
        }
        else
        {
            cout<<x/2<<" "<<x/2<<"\n";
        }
    }
    return 0;

}
