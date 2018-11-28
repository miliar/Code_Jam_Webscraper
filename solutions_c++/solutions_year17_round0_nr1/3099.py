#include <iostream>
#include <vector>
#include <string>
#include <algorithm>


using namespace std;

int main()
{
	int N;
	cin >> N;
	long p=1;
	while (N!=0)
	{
		
		string str;
		cin >> str;
		std::vector<bool> v;
		for (auto c:str)
		{
			if (c=='+')
			v.push_back(1) ;
			else
				v.push_back(0);
		}

		int k;
		cin >>k;
		int count = 0;

		for (int i=0; i<v.size()-k+1;i++)
		{
			if (!v[i])
			{
				for (int i1=0; i1<k;i1++)
				{
					v[i+i1] = !v[i+i1];
				}
				count++;
			}
		}
		bool x = true;
		for (auto c:v)
		{
			x = x && c;
		}
		cout << "Case #" << p << ": " ;
		if (x)
		cout <<  count << std::endl;
		else
		cout << "IMPOSSIBLE" << std::endl;		
		p++;


		N--;

	}
}