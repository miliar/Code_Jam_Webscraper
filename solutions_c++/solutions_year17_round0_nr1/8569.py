#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll  long long int
#define X first
#define Y second
using namespace std;
int main()
{
    int t,k,i,j,c,n,m;
    string s,s1;
    ofstream out;
    out.open("output.txt");
    int pp=1;
    cin>>t;
    while(t--)
    {
        cin>>s1>>k;
        cout<<"Case #"<<pp<<": ";
        out<<"Case #"<<pp<<": ";pp++;
        int ans=1e7;
        s=s1;c=0;
        for(i=0;i<=s.length()-k;i++)
            if(s[i]=='-')
        {
            for(j=0;j<k;j++)
                if(s[i+j]=='-') s[i+j]='+';
                else s[i+j]='-';
             c++;
        }
        for(;i<s.length();i++)
            if(s[i]=='-')
            break;
        if(i==s.length()) ans=min(ans,c);
        //
        s=s1;c=0;
        for(i=s.length()-1;i>=k-1;i--)
            if(s[i]=='-')
        {
            for(j=0;j<k;j++)
                if(s[i-j]=='-') s[i-j]='+';
                else s[i-j]='-';
             c++;
        }
        for(;i>=0;i--)
            if(s[i]=='-')
            break;
        if(i==-1) ans=min(ans,c);
        //
        if(ans==1e7) cout<<"IMPOSSIBLE\n";
        else cout<<ans<<endl;

        if(ans==1e7) out<<"IMPOSSIBLE\n";
        else out<<ans<<endl;
    }
    return 0;
}
