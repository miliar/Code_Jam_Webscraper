#include <iostream>
#include <fstream>

using namespace std;

bool test(int number)
{
	int flag=1;
	while(number/10>0)
	{
		if(number%10<(number/10)%10)
		{
			flag=0;
			break;
		}
		number/=10;
	}
	return flag;
}

int main()
{
	ifstream ifs;
    ifs.open("input.txt");
	int n;
	ifs>>n;
	for(int i=0;i<n;i++)
	{
		int number;
		int printed;
		ifs>>number;
		for(int j=number;j>=0;j--)
		{
			if(test(j))
			{
				printed=j;
				break;
			}
		}
		cout << "Case #" << i+1 << ": " << printed << endl;
	}
	return 0;
}