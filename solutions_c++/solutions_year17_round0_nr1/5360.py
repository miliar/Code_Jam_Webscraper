#include<bits/stdc++.h>

using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("op3.out","w",stdout);
    int t,ii=1,n;
    cin>>t;
    while(ii<=t)
    {
        string s;
        int k;
        cin>>s;
        cin>>k;
        cout<<"Case #"<<ii<<": ";
        int count_flips=0,j;
        int sz=s.size();
        for(int i=0;i<s.size()-k+1;)
        {
             j=i;
            //cout<<i;
            int gotminus=-1;
            while(j<s.size() && s[j]=='+')
            {
                gotminus=1;
                j++;
            }
            if(j+k-1 < sz)
            {
                for(int x=j;x<j+k;x++)
                    {
                        if(s[x]=='-')
                            s[x]='+';
                        else
                            s[x]='-';
                    }
                    count_flips++;
            }
            i=j+1;
        }
        //cout<<count_flips<<"=";
        //for(int i=0;i<s.size();i++)
           // cout<<s[i];
            int flag=1;
            for(int i=0;i<s.size();i++)
            if(s[i]=='-')
            {
                    //cout<<s[i]<<" ";
                    flag=0;
                    break;
            }

        if(flag==1)
            cout<<count_flips;
        else
            cout<<"IMPOSSIBLE";
        cout<<endl;
        ii++;
    }
}
