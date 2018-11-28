#include <iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<string>

using namespace std;
 
unsigned long long tonum(string st)
{
       unsigned long long n=0,i=0;
        while(st[i]!='\0')
        {
                n=n*10+((int)st[i]-48);
                i++;
        }
        return n;
}
int main() {
	int t;
	cin>>t;
	for (int no=1;no<=t;no++)
	{
	    string num;
	    cin>>num;
	    int flag=0;
	    if (num.size()==1)
	    {
	        cout<<"Case #"<<no<<": "<<num<<endl;
	        continue;
	    }
	    for (int i=1;i<num.size();i++)
	    {
	    	if (num[i]<num[i-1])
	    	{
	    		flag=1;
	    		break;
	    	}
	    }
	    if (flag==0)
	    cout<<"Case #"<<no<<": "<<tonum(num)<<endl;
	    else
	    {
	    	for (int i=0;i<num.size()-1;i++)
	    	{
	    	    if (num[i]>=num[i+1])
	    	    {
	    	        num[i]=num[i]-1;
	    	        for (int j=i+1;j<num.size();j++)
		             num[j]='9';
		            break;
	    	    }
	    	}
	    	cout<<"Case #"<<no<<": "<<tonum(num)<<endl;
	    }
	}
	return 0;
}
