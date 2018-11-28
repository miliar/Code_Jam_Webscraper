#include <iostream>
#include <string.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        string s;
        cin>>s;
        int l=strlen(s.c_str());
        string ans="";
        if(l==1)	ans=s;
        else
        {
        	int i=0,j=1;
        	while(i<l && j<l && s[i]<=s[j])
        	{
        		if(s[i]<s[j])	i=j++;
        		else	j++;
        	}
        	if(j==l || i==l)
        		ans=s;
        	else
        	{
        		int k=0;
        		while(k<=i-1)	ans+=s[k++];
        		ans+=char(s[i]-1);
        		k=i;
        		while(++k<l)	ans+='9';
        	}
        }
        while(ans[0]=='0')	ans.erase(ans.begin());

        cout<<"Case #"<<z<<": "<<ans<<"\n";
    }
    return 0;
}
