#include <iostream>
//#include <limits>
#include <string>
#include <sstream>
#include <stdlib.h>
using namespace std;
int main()
{
	//unsigned long max_unsigned_int_size = std::numeric_limits<unsigned long>::max();
	//cout<<max_unsigned_int_size;
	int t,t1=0;
	cin>>t;
	while(t1<t)
	{
		unsigned long N;
		cin>>N;
		for(int j=N;j>0;j--)
		{
		int ans=j;
		int flag=0;
		stringstream ss;
		ss << ans;
		string str = ss.str();
		//cout<<str;
		for(int i=0;i<str.length()-1;i++)
		{
			if(int(str[i])<=int(str[i+1]))
				continue;
			else
			{
				flag=1;
				break;
			}
		}

		if(flag==0)
		{
			cout<<"Case #"<<t1+1<<":"<<ans<<endl;
			break;
		}
		}
		t1++;
	}
	return 0;
}

