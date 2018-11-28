#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        char s[20];
        cin>>s;
        int i,j,l=strlen(s);
        for(i=l-1;i>0;i--)
        {
            if(s[i]<s[i-1])
            {
                for(j=i;j<l;j++)
                    s[j]='9';
                s[i-1]--;
            }
        }
        cout<<"Case #"<<k<<": ";
        for(i=0;i<l;i++)
        {
            if(s[i]!='0')
            break;
        }
        while(i<l)
        {
            cout<<s[i];
            i++;
        }
        cout<<endl;
    }
	return 0;
}
