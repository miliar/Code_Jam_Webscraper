#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,k,i,j,ll,l,cnt,cs=1,f,kk;
    string s,ss;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        cin>>s>>k;
        l=s.size();
        cnt=0;
        f=0;
        for(i=0;i<s.size();)
        {
            ll=l-i;
            if(s[i]=='-' && ll>=k)
            {
                kk=i;
                for(j=0;j<k;j++,kk++)
                {
                    if(s[kk]=='+') s[kk]='-';
                    else s[kk]='+';
                }
                i++;
                cnt++;
               // cout<<i<<endl;
            }
            else if(s[i]=='-' && ll<k)
            {
                f=1;
                break;
            }
            else i++;
            //cout<<s<<" "<<i<<endl;
        }
        printf("Case #%d: ",cs++);
        if(f) printf("IMPOSSIBLE\n");
        else cout<<cnt<<endl;
    }
}
