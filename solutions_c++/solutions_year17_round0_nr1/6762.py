#include<bits/stdc++.h>
using namespace std;

int main()
{

    freopen("inp.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    int curr=1;
    while(t--)
    {


        string s;
        int k;
        cin>>s>>k;


    int l=0;
    int r=s.size()-1;
    int ans=0;
    while(l<r)
    {
        //cout<<"hello\n";
        if(((l+k-1)>r)||(r-k+1<l))
            break;
        if(s[l]=='+')
                l++;
       else  if(s[l]=='-')
        {

            ans++;
            //l--;
            for(int i=l;i<l+k;i++)
            {

                if(s[i]=='-')
                    s[i]='+';
                else
                    s[i]='-';
            }
            l++;
        }
         if(((l+k-1)>r)||(r-k+1<l))
            break;
         if(s[r]=='-')
        {

            ans++;
            //l--;
            for(int i=r;i>r-k;i--)
            {

                if(s[i]=='-')
                    s[i]='+';
                else
                    s[i]='-';
            }
            r--;
        }
        else if(s[r]=='+')
            r--;
    }
    int imp=0;

    for(int i=l;i<=r;i++)
    {

        if(s[i]=='-')
        {
            imp++;

        }
    }
    if(imp!=0)
        cout<<"Case #"<<curr<<": IMPOSSIBLE\n";
    else
        cout<<"Case #"<<curr<<": "<<ans<<"\n";
    curr++;
}
}
