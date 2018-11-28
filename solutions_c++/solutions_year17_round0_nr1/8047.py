

#include <iostream>
#include <string>


int main()
{
	std::ios_base::sync_with_stdio(false);
/*
	freopen("inputL.in","r",stdin);
	freopen("outputL.txt","w",stdout);
	*/
	int t;
	std::cin >> t;

	for(int z=1; z<=t; z++)
	{
		std::string s;
		int k;

		std::cin >> s >> k;

		int c=0,i;
		for(i=0;i<=s.size()-k; i++)
		{
			if(s[i] =='-')
			{
				c++;
				for(int j=i; j<i+k; j++)
				{
					if(s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
			}
		}

		std::cout << "Case #" << z <<": ";
		bool flag = true;
		for(;i<s.size(); i++)
		{
			if(s[i] == '-')
			{
				flag = false;
				break;
			}
		}
		if(!flag)
			std::cout<<"IMPOSSIBLE\n";
		else
			std::cout<<c<<"\n";
	}
}
