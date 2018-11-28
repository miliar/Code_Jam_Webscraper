#include <string>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
using namespace std;

bool isTidy(vector<int> ans)
{
	bool b = true;

	for (int i = ans.size() - 1; i > 0; i--)
	{
		if (ans[i] < ans[i - 1])
		{
			b = false;
			break;
		}
	}
	return b;
}

long long toLong(vector<int> ans)
{
	long long num = 0;
	for (int i = 0; i < ans.size(); i++)
	{
		num *= 10;
		num += ans[i];
	}
	return num;
}

long long tidy(vector<int> ans)
{
	for (int i = ans.size()-1; i > 0; i--)
	{
		if (ans[i] < ans[i - 1])
		{
			ans[i-1]--;
			for (int j = i; j < ans.size(); j++)
			{
				ans[j] = 9;
			}
		}
	}
	return toLong(ans);
}



int main() {
	ifstream inStream;
	ofstream outStream;

	inStream.open("B-large.in");
	outStream.open("output.txt");

	int loop;
	inStream >> loop;

	for (int count = 1; count <= loop; count++)
	{
		long long num;
		inStream >> num;
		long long num2 = num;
		//convert long long to a vector
		long long temp = num;
		int size = 0;

		while (temp > 0)
		{
			temp /= 10;
			size++;
		}
		vector<int>ans(size);
		
		while (num > 0)
		{
			ans[size - 1] = num % 10;
			num /= 10;
			size--;
		}


		if (isTidy(ans))
		{
			outStream << "Case #" << count << ": " << toLong(ans) << endl;
			cout << "Case #" << count << ": " << toLong(ans) << endl;
		}
		else
		{
			outStream << "Case #" << count << ": " << tidy(ans) << endl;
			cout << "Case #" << count << ": " << tidy(ans) << endl;
		}
	}

	inStream.close();
	outStream.close();

	return(0);
}