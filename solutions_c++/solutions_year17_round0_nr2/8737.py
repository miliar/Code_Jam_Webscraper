#include <iostream>
#define ull unsigned long long
using namespace std;
ull sti(string str)
{
        ull n=0,i=0;
        while(str[i]!='\0')
        {
                n=n*10+((int)str[i]-48);
                i++;
        }
        return n;
}
int main() {
	int t;
	cin>>t;
	for (int test=1;test<=t;test++)
	{
	    string num;
	    cin>>num;
	    int flag=0;
	    if (num.size()==1)
	    {
	        cout<<"Case #"<<test<<": "<<num<<endl;
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
	    cout<<"Case #"<<test<<": "<<sti(num)<<endl;
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
	    	cout<<"Case #"<<test<<": "<<sti(num)<<endl;
	    }
	}
	return 0;
}