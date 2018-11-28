#include <iostream>
#include <string>
#include <sstream>

using namespace std;
int main()
{
	long long N;
	string str_num;
	int T;
	int i, j, k;
	int len, prev;
	bool FLAG;
	std::string::size_type sz = 0;

	cin>>T;
	for(i=1; i<=T; i++)
	{
		cin>>N;

		//cout<<"Current input = "<<N<<"\n";
		while(true)
		{
			std::ostringstream oss;
			oss<<N;
			str_num = oss.str();

			//cout<<"current str = "<<str_num<<"\n";
			len = str_num.size();
			prev = 0;
			FLAG = false;
			for(j=0; j<len; j++)
			{
				if( (str_num[j] - '0') < prev)
				{
					//cout<<(str_num[j] - '0')<<" is less than "<<prev<<"\n";
					for(k=j; k<len; k++)
						str_num[k] = '0';
					FLAG = true;
					break;
				}
				prev = (str_num[j] - '0');
			}

			if (FLAG == false)
				break;
			std::stringstream iss(str_num);
			iss >> N;
			N = N - 1;
		}
		cout<<"Case #"<<i<<": "<<N<<"\n";
	}

	return 0;
}
