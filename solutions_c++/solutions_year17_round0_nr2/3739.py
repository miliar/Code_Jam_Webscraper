#include <bits/stdc++.h>


using namespace std;



int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);

	int T;
	cin>>T;

	for(int t = 1; t <= T; ++t)
	{
		string number;
		cin>>number;
		for (int i = 0; i < number.length()-1; ++i)
		{
			if(number[i]>number[i+1])
			{
				i--;
				while(i>=0 && number[i] == number[i+1])
					i--;

				number[++i]--;
				
				while(++i < number.length())
					number[i] = '9';
				
			}
		}
		cout<<"Case #"<<t<<": "<<stoll(number)<<"\n";
	}


	return 0;
}