#include <iostream>
#include <string>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int test,t,i,j,k,cnt;
    string s;
    cin>>test;
    t=test;
    while(test--)
    {
        cnt=0;
        cin>>s>>k;
        for(i=0; i<s.length()-k+1; i++)
        {
            if(s[i]=='-')
            {
                cnt++;
                for(j=0; j<k; j++)
                {
                    if(s[i+j]=='-')
                        s[i+j]='+';
                    else
                        s[i+j]='-';
                }
            }
        }
        for(j=s.length()-k; j<s.length(); j++)
        {
            if(s[j]=='-')
                break;
        }
        if(j==s.length())
            cout<<"Case #"<<t-test<<": "<<cnt<<endl;
        else
            cout<<"Case #"<<t-test<<": IMPOSSIBLE"<<endl;
    }
	return 0;
}
