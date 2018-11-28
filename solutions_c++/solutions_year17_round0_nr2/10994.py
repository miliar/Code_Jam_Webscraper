#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for(int tc=1;tc<=t;tc++)
	{
		long long mylong;
		cin >> mylong;
		string as;
    	stringstream mystream;
    	mystream << mylong;

    	as = mystream.str();

    	int len = strlen(as.c_str());
    	int flag=1;
    	for(int i=len-1;i>0;i--)
    	{
    		if(as[i-1]>as[i])
    		{
    			if(as[i-1]=='1')
    			{	
    				flag=0;
    				break;
    			}
    			else
    			{
    				for(int j=i;j<len;j++)
    				{
    					as[j]='9';
    				}
    				int num = as[i-1]-'0';
    				num--;
    				as[i-1]=num+'0';	
    			}	
    		}	
    	}
    	if(flag==0)
    	{
    		long long kr=0;
    		for(int kd=0;kd<len-1;kd++)
    		{
    			kr=kr*10;
    			kr=kr+9;
    		}
    		cout << "Case #"<<tc<<": "<<kr<<endl;
    	}
    	else
    	{
    		long long kr = stoll(as,0,10);
    		cout << "Case #"<<tc<<": "<<kr<<endl;
    	}	
	}
}