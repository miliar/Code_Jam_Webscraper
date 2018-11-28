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
		std::vector<int> v;
		for (auto c:str)
		{
			v.push_back(atoi(&c)) ;
		}

		std::reverse (begin(v), end(v));
		for (int i=1; i<v.size();)
		{
			if (v[i] > v[i-1])
			{
				v[i]--;

				
				for (int j=0; j<i; j++)
				{
					v[j]=9;
				}
				i++;
			}
			else
			{
				i++;
			}

			
		}


		std::reverse (begin(v), end(v));
		cout << "Case #" << p << ": ";
		for (int i=0; i<v.size();i++)
		{
			if (i==0 && v[i]==0){
				continue;
			}

			cout << v[i];
		}
		cout << endl;
		p++;

		N--;

	}
}