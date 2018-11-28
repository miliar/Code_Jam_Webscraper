#include<iostream>
#include<fstream>
#include<string>

using namespace std;
bool areSorted(long int n)
{
	// Note that digits are traversed from last to first
	int next_digit = n % 10;
	n = n / 10;
	while (n)
	{
		int digit = n % 10;
		if (digit > next_digit)
			return false;
		next_digit = digit;
		n = n / 10;
	}

	return true;
}

void main()
{
	std::streambuf *coutbuf = std::cout.rdbuf();
	std::streambuf *cinbuf = std::cin.rdbuf();

	std::ofstream out("outputfile.out");
	std::ifstream in("B-small-attempt0.in");

	//Read from infile.txt using std::std::cin
	std::cin.rdbuf(in.rdbuf());

	//Write to outfile.txt through std::cout
	std::cout.rdbuf(out.rdbuf());

	int t, n;
	int a[1000], i, j, k;
	cin >> t;
	for (i = 0; i < t; i++)
	{
		cin >> a[i];
	}
	for (i = 0; i < t; i++)
	{
		for (j = a[i]; j >= 0;)
		{
			if (areSorted(j))
			{
				cout << "Case #" << i + 1<<": "<<j<< endl;

				break;
			}
			else
				j--;
			//areSorted(j) ? cout <<j: j--;
		}
	}
	std::cin.rdbuf(cinbuf);   //reset to standard input again
	std::cout.rdbuf(coutbuf); //reset to standard output again
}