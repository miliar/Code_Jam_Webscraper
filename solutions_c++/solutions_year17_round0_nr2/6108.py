#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int n,t,l,i,j,cs=1;
    char s[10000];
     freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        cin>>s;
        cout<<"Case #"<<cs++<<": ";
        l=strlen(s);
        for(i=1;i<l;i++)
        {
            if(s[i]<s[i-1])
            {
                for(j=i;j<l;j++)
                    s[j]='9';
                s[i-1]--;
                break;
            }
        }

        for(j=i-1;j>=0;j--)
        {
            if( j && s[j]<s[j-1])
            {
                s[j-1]--;
                s[j]='9';
            }
        }
        cout<<atoll(s)<<endl;
    }


}
