#include <iostream>
using namespace std;

#include <string>

int isTidy(string N);
int greatestTidyNum(string N);

main()
{

	int T,i;
	cin>>T;

	string N;

	for(i=0;i<T;++i)
	{
		cin>>N;
		cout<<"Case #"<<i+1<<": "<<greatestTidyNum(N)<<endl;
	}

}

int greatestTidyNum(string N)
{

	int tidyNumber;

	if(isTidy(N))
		tidyNumber=stoi(N);

	//if it is not tidy number
	else
	{
		int str_len=N.length();

		if(str_len==2)
		{
			tidyNumber=(stoi(N)/10 - 1)*10+9;
		}

		else if(str_len==3)
		{

			if(N[1]==N[0])
			{
				tidyNumber=greatestTidyNum(to_string(stoi(N.substr(0,2))-1))*10+9;
			}

			else if(isTidy(N.substr(0,2)))
			{
				//cout<<"isTidy 0,2 : "<<stoi(N.substr(0,2))<<endl;
				tidyNumber=(stoi(N.substr(0,2))-1)*10+9;
			}

			else
			{
				string s=N.substr(0,2);
				//cout<<"s "<<s<<" "<<greatestTidyNum(s)<<endl;
				tidyNumber=greatestTidyNum(s)*10+9;
			}
		}

		else if(N=="1000")
			tidyNumber=999;

	}

	return tidyNumber;
}

int isTidy(string N)
{
	int str_len=N.length();

	int isTidy=1;

	for(int i=0;i<str_len-1;++i)
		if(N[i]>N[i+1])
		{
			isTidy=0;
			break;
		}

	return isTidy;
}