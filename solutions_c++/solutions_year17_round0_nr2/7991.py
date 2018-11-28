#include <bits/stdc++.h>

using namespace std;
typedef long long ll;


int main()
{
    freopen("B-large.in","r",stdin);
   freopen("B-largeout.out","w",stdout);

    int t;
    cin>>t;

    int cs=0;
    string in;
    while(cs<t)    {
        cin>>in;

        cout<<"Case #"<<++cs<<": ";
        int pos=-1;
        for(int i=1;i<in.length();i++)    {
            if(in[i]<in[i-1])    {pos=i;break;}
        }
        if(pos==-1)    {cout<<in<<endl;continue;}

        for(int i=pos;i>=0;i--)    {
            if(i==0||in[i]>in[i-1])    {
                in[i]--;
                for(int j=i+1;j<in.length();j++)    in[j]='9';
                break;
            }
        }
        int strt=-1;
        for(int i=0;i<in.length();i++)    {
            if(in[i]!='0')    {
                strt=i;
                break;
            }
        }

        for(int i=strt;i<in.length();i++)    cout<<in[i];
        cout<<endl;
    }

    return 0;
}
