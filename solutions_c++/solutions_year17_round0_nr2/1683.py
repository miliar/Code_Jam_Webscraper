#include <bits/stdc++.h>
#define ll long long
#define inf 1000000000
#define pb push_back
using namespace std;
string str;
int main()
{
    freopen("txtin.txt","r",stdin);
    freopen("txtout.txt","w",stdout);
    int n,m,i,j,k,l,t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        cout<<"Case #"<<test<<": ";
        cin>>str;
        bool flag=0;
        n=str.size();
                int ind=n+1;
        for(i=1;i<n;i++)
        {
            if(str[i]<str[i-1])
                {
                    ind=i-1;
                break;
            }
        }
        if(ind==n+1)
        {
            cout<<str<<"\n";
        }
        else
        {
            while(str[ind]-'0'-1<(str[ind-1]-'0')&&ind>0)
                ind--;
                if(ind==0){
                    if(str[ind]=='1')
                for(i=0;i<n-1;i++)
                cout<<"9";
                else
                {
                    cout<<str[0]-'0'-1;
                  for(i=0;i<n-1;i++)
                    cout<<"9";

                }

                }
                else
                {
                    for(i=0;i<ind;i++)
                    cout<<str[i];
                    cout<<str[ind]-'0'-1;
                    for(i=ind+1;i<n;i++)
                        cout<<"9";
                }
                cout<<endl;
        }

    }
    return 0;
}
