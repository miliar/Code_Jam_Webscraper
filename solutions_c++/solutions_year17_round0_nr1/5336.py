#include <iostream>
#include <fstream>
#include <string>

int main()
{
	std::ifstream inp("input_a.txt");
	int tt;
	inp >> tt;
	std::ofstream outp("output_a.txt");
	for (int t = 1; t <= tt; ++t)
	{
		std::string s;
		int k;
		inp >> s >> k;
		int len = s.length();
		int count = 0;
		for (int i = 0; i <= len - k; i++)
		{
			if (s[i] == '+')
				continue;
			count++;
			for (int j = 0; j < k; j++)
			{
				if (s[i + j] == '-')
					s[i + j] = '+';
				else
					s[i + j] = '-';
			}
		}
		bool is_correct = true;
		for (int i = 0; i < len; i++)
			if (s[i] == '-')
			{
				is_correct = false;
				break;
			}
		
		outp << "Case #" << t << ": ";
		if (is_correct)
			outp << count;
		else
			outp << "IMPOSSIBLE";
		if (t != tt)
			outp << std::endl;
			
	}
	outp.close();
	inp.close();
	return 0;
}