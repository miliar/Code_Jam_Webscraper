#include <iostream>
#include <fstream>
#include <string>


bool isTidy(std::string num)
{
	for (int i=0; i<num.length()-1; i++)
	{
		if (num[i] > num[i+1]) 
		{
			return false;
		}
	}
	return true;
}

int main()
{
	long long T;
	long long N;
	std::cin >> T;
	for (int i=0; i<T; i++)
	{	
		int last_num;
		std::cin >> N;
		while (!isTidy(std::to_string(N)))
		{
			N--;
		}
		std::cout << "Case #" << i+1 << ": " << N << std::endl;
	}
}
