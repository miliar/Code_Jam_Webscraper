#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define SF scanf
#define PF printf
#define PB push_back
#define MP make_pair
#define mx 4000001
#define INP          freopen("A-large.in.txt", "r", stdin);
#define OUT          freopen("out.txt", "w", stdout);
#define BOOST        std::ios_base::sync_with_stdio(false);
int a[mx];

map<string,int>mp;
int main()
{
    INP;
    OUT;
    ll n,t,i,j,m,f,p,p1,flag,c=0,c1,q,k;
    t=1;
    string st;
    cin>>q;
    while(q--)
    {
        cin>>st>>p;
        f=0;
        c=0;
        for(i=0;i<st.size();i++)
        {
            if(st[i]=='-')
            {
                c++;

                if(i+p-1>=st.size())
                {
                    f=1;
                }
                j=0;
                k=i;
                while(j<p&&k<st.size())
                {
                    if(st[k]=='-')
                    {
                        st[k]='+';
                    }
                    else
                    {
                        st[k]='-';
                    }
                    j++;
                    k++;
                }
            }
        }
        if(f==1)
        {
            cout<<"Case #"<<t++<<": IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<"Case #"<<t++<<": "<<c<<endl;
        }
    }

return 0;
}
