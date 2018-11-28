#include<iostream>
 
using namespace std;
 
int main()
{
    int t,k,ans,in;
    string s;
    cin>>t;
    for (int no=1;no<=t;no++)
    {   
		ans=0;
        cin>>s>>k;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {   ans++;
                for(int j=i;j<i+k;j++)
                {
                    if(j>=s.length())
                        ans = -1;
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
        if(ans==-1)
            cout<<"Case #"<<no<<": IMPOSSIBLE\n";
        else
            cout<<"Case #"<<no<<": "<<ans<<"\n";
    }
}
