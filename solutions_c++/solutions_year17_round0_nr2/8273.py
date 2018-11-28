#include<iostream>
#include<string>
#include<sstream>
using namespace std;

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.txt", "w", stdout);
	
	int test;
	cin>>test;
	
	for(int j=1;j<=test;j++)
	{
		long long N;
		cin>>N;
		
		stringstream stream;
	    stream << N;
	    string str = stream.str();
	    
	    long long Ans;
	    if(str.size() == 1)
	    	Ans = N;
	    else
	    {
	    	while(N)
	    	{
	    		int len = str.size();
	    		int flag = 0;
	    		int i = 0;
	    		for(int i=0;i<len-1;i++)
	    		{
	    			if(str[i] > str[i+1])
	    			{
	    				flag = 1;
	    				break;
					}
				}
				
				if(flag == 0)
				{
					Ans = N;
					break;
				}
				else
				{
					N = N - 1LL;
					stream.str(std::string());
					stream << N;
	    			str = stream.str();
	    			if(str.size() == 1)
	    			{
	    				Ans = N;
	    				break;
					}
				}
			}
		}
		
		cout<<"Case #"<<j<<": "<<Ans<<endl;
	}
	
	return 0;
}
