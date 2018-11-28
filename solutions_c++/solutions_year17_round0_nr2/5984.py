#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,i,one,zero,pos,ctr=1;
    long long ans=0;
      ofstream ofile ("C:\\Users\\P Barik\\Desktop\\output1.txt");
    string n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        ans=0;
        cout<<"Case #"<<ctr<<": ";
        ofile<<"Case #"<<ctr<<": ";
        ctr++;
        one=zero=0;
        if(n.length()==1)
        {
            cout<<n<<"\n";
            ofile<<n<<"\n";
        }
        else
        {
            pos=n.length();
            for(i=0;i<n.length();i++)
            {
                if(n[i]=='0')
                    zero++;
                if(n[i]=='1')
                    one++;
            }
            if(one==n.length())
            {
                cout<<n<<"\n";
                ofile<<n<<"\n";
            }
            else if(one+zero==n.length())
            {
                for(i=0;i<n.length()-1;i++)
                   {
                       cout<<'9';
                       ofile<<'9';
                   }
                    cout<<"\n";
                    ofile<<"\n";
            }
            else
            {
                for(i=0;i<n.length()-1;i++)
                {
                    if((int)(n[i+1])<(int)n[i])
                    {
                        pos=i;
                        break;
                    }
                }
                if(pos<n.length())
                n[i]=(char)((int)n[i]-1);
                for(i=pos+1;i<n.length();i++)
                {
                    n[i]='9';
                }
                for(i=n.length()-1;i>0;i--)
                {
                    if((int)n[i]<(int)n[i-1])
                    {
                        n[i]='9';
                        n[i-1]=(char)min((int)n[i-1]-1,(int)n[i]);
                    }
                }
                for(i=0;i<n.length();i++)
                {
                    ans=ans*10+n[i]-'0';
                }
                ofile<<(long long)ans<<"\n";
                cout<<(long long)ans<<"\n";
            }
        }
    }
    return 0;
}
