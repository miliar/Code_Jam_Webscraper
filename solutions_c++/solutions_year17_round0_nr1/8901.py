#include<bits/stdc++.h>
using namespace std;
int main()
{

     freopen("ot.txt","w",stdout);
      freopen("in.txt","r",stdin);
    string s,ss;
    int i,j,k,l,t,cs=1,n,x,xx;
    bool f=0,ff=0;
    cin>>t;
    while(t--)
    {
        x=0;
        xx=100000000;
        f=0;
        ff=0;
        cin>>s>>k;
        cout<<"Case #"<<cs++<<": ";
        ss=s;
        n=s.size();
        for(i=0;i<n;i++)
        {
            if(s[i]=='-' && i+k<=n)
            {
                x++;
                //cout<<i<<endl;
                    j=0;
                    while(j<k)
                    {
                        if(s[j+i]=='-')
                            s[j+i]='+';
                        else
                            s[j+i]='-';
                        j++;

                    }
            }
        }
       // cout<<s<<endl;

        for(i=0;i<n;i++)
            if(s[i]=='-') f=1;
        if(f==0)
        {
            cout<<x<<endl;
        }
        else if(f==1)
        {
            xx=0;
            reverse(ss.begin(),ss.end());
            s=ss;
            //cout<<ss<<endl;
            for(i=0;i<n;i++)
            {
                if(s[i]=='-' && i+k<=n)
                {
                    xx++;
                //cout<<i<<endl;
                    j=0;
                    while(j<k)
                    {
                        if(s[j+i]=='-')
                            s[j+i]='+';
                        else
                            s[j+i]='-';
                        j++;
                    }
                }
            }
             for(i=0;i<n;i++)
            if(s[i]=='-') ff=1;

            if(ff==0)
            cout<<xx<<endl;
            else
                cout<<"IMPOSSIBLE"<<endl;

        }

    }
}
