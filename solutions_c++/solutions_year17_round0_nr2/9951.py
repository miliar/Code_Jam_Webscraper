#include<iostream>
#include<fstream>
using namespace std;
bool check(int n)
{
	int max = 11;
	while (n > 0)
	{
		if (n % 10 > max)return false;
		else
		{
			max = n % 10;
			n = n / 10;
		}
	}
	return true;
}
int main()
{
	int N;
	cin >> N;
	ofstream outfile("test.txt");
	for (int i = 1; i <= N; i++)
	{
		int num;
		cin >> num;
		while (check(num) == 0){ num--; }
		outfile << "Case #" << i << ": " << num << endl;
		
	}
	outfile.close();
}