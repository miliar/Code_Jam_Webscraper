#include <iostream>
#include <fstream>
#include <vector>

int main()
{
	std::ifstream inp("input_b.txt");
	std::ofstream outp("output_b.txt");

	int tt;
	inp >> tt;
	for (int t = 1; t <= tt; t++)
	{
		outp << "Case #" << t << ": ";
		long long n;
		inp >> n;
		long long copy_n = n;
		std::vector< int > v;
		while (n != 0)
		{
			v.push_back( n % 10 );
			n /= 10;
		}
		v.push_back( 0 );
		int i = v.size() - 2;
		while (i != -1)
		{
			if (v[i] < v[i+1])
			{
				int j = i;
				for (int k = j; k >= 0; k--)
					v[k] = 9;
				j++;
				--v[j];
				while (v[j] < v[j+1])
				{
					v[j] = 9;
					v[j+1]--;
					j++;
				}
				break;
			}

			i--;
		}
		i = v.size() - 1;
		while (v[i] == 0)
			i--;
		for (int j = i; j >= 0; j--)
			outp << v[j];
		if (t != tt)
			outp << std::endl;
	}

	outp.close();
	inp.close();
	return 0;
}
