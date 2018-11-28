#include "COutputGenerator.h"
#include <fstream>
#include <iostream>

bool Istidy(std::string number)
{
	for (int k = 1; k < number.length(); k++)
	{
		if (number[k] < number[k - 1])
			return false;
	}

	return true;
}

void solveQ2()
{
	std::ifstream input;
	input.open("Q2input.txt");
	COutputGenerator output;
	output.initFile("Q2out.txt");

	int n;

	input >> n;

	for (int test = 0; test < n; test++)
	{
		std::string number;
		input >> number;

		while (!Istidy(number))
		{
			//std::cout << "Number:" << number << std::endl;

			for (int k = 0; k < number.length()-1; k++)
			{
				if (number[k + 1] < number[k])
				{
					if (k == 0)
					{
						if (number[k] == '1')
						{
							std::string res = "";
							for (int kk = 0; kk < number.length() - 1; kk++)
								res = res + '9';

							number = res;
							break;
						}
						else
						{
							std::string res = number.substr(0,k);
							res = res + char(number[k] - 1);
							for (int kk = k + 1; kk < number.length(); kk++)
								res = res + '9';

							number = res;
							break;
						}
					}

					else
					{
						std::string res = number.substr(0, k);
						res = res + char(number[k] - 1);
						for (int kk = k + 1; kk < number.length(); kk++)
							res = res + '9';

						number = res;
						break;
						
					}

				}
			}
		}

		output.writeTest(test + 1, number);



	}



	input.close();
	output.closeFile();
}

int main()
{

	solveQ2();

	//std::cout << "FINISHED " << std::endl;
	//getchar();
}