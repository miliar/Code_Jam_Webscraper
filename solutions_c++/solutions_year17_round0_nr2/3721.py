#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;



int main() {

	ifstream in;
	in.open("B-large.in");

	ofstream out;
	out.open("output.txt");

	int T;
	in >> T;

	for (int i = 0; i < T; i++)
	{
		out << "Case #" << (i + 1) << ": ";

		string s;
		in >> s;

		int size = s.length();

		int* a = new int[size];
		for (int j = 0; j < size; j++)
		{
			a[j] = s[j] - '0';
		}

		int j;
		for (j = 0; j < size - 1; j++)
		{
			if (a[j] > a[j + 1])
				break;
		}
		
		if(j != size - 1)
			a[j]--;
		
		for (int k = j + 1; k < size; k++)
			a[k] = 9;

		for (int k = j; k >= 1; k--)
		{
			if (a[k] < a[k - 1])
			{
				a[k] = 9;
				a[k - 1]--;
			}
			else 
				break;
		}

		string number = "";
		
		if (a[0] == 0)
		{
			for (int k = 1; k < size; k++)
				number = number + '9';
		}
		else
		{
			for (int k = 0; k < size; k++)
			{
				number = number + to_string(a[k]);
			}
		}
	

		out << number << endl;
		//cout << i+1 << " " << number << endl;

	}

	in.close();
	out.close();
	system("PAUSE");

	return 0;

}