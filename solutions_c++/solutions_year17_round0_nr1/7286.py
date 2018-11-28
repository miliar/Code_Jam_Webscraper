/** source code by coolreshab **/

#include<bits/stdc++.h>
using namespace std;

string s;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,K,dragon=1,ans,len,i,j;
    cin>>T;
    while(T-->0)
    {
        cin>>s>>K;
        len=s.length();
        ans=0;
        for(i=0;i<len;++i)
        {
            if(s[i]=='-')
            {
                ans++;
                if(i+K-1>=len)
                {
                    ans=-1;
                    break;
                }
                j=0;
                while(j<K)
                {
                    s[i+j]=='+'?s[i+j]='-':s[i+j]='+';
                    j++;
                }
            }
        }
        cout<<"Case #"<<dragon<<": ";
        ans==-1?cout<<"IMPOSSIBLE":cout<<ans;
        cout<<endl;
        dragon++;
        s.clear();
    }
    return 0;
}
