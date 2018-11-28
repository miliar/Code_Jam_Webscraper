#include <bits/stdc++.h>
using namespace std;

unsigned long long findnw(string str)
{
       unsigned long long num=0,k=0;
        while(str[k]!='\0')
        {
                num=num*10+((int)str[k]-'0');
                k++;
        }
        return num;
}
int main() {
	int t;
	cin>>t;
	for (int j=1;j<=t;j++)
	{
	    string str;
	    cin>>str;
	    if (str.size()==1)
	    {   cout<<"Case #"<<j<<": "<<str<<endl;
	        continue;}
	        int flag=0;
	    for (int i=1;i<str.size();i++)
	    {
	    	if (str[i]<str[i-1])
	    	{
	    		flag=1;
	    		break;
	    	}
	    }
	    if (flag==0)
	    cout<<"Case #"<<j<<": "<<findnw(str)<<endl;
	    else
	    {
	    	for (int i=0;i<str.size()-1;i++)
	    	{
	    	    if (str[i]>=str[i+1])
	    	    {
	    	        str[i]=str[i]-1;
	    	        for (int j=i+1;j<str.size();j++)
		             str[j]='9';
		            break;
	    	    }
	    	}
	    	cout<<"Case #"<<j<<": "<<findnw(str)<<endl;
	    }
	}
	return 0;
}