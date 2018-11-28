// TidyNumbers.cpp: define el punto de entrada de la aplicación de consola.
//

#include <stdio.h>
#include <tchar.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <queue>
#include <map>

class TestCase
{
private:
	std::string lastTatianaNumber;
	

	bool IsSolution(const std::string &str) const
	{
		char firstChar = '0';

		for(char currentChar:str)
		{
			if (firstChar > currentChar)
			{
				return false;
			 }
			firstChar = currentChar;
		}

		return true;
	}

public:
	TestCase(const char(&lines)[8000])
	{
		std::string inputStr(lines);

		this->lastTatianaNumber = inputStr;
	}

	char GetGreaterDigit(const std::string str1, int topVal) const
	{
		char firstDigit = str1[0];
		for (int j = 1; j <= topVal; j++)
		{
			if (str1[j] > firstDigit )
			{
				firstDigit = str1[j];
			}
		
		}

		return firstDigit;

	}

	char *Solve() const
	{
		char  result[8000];

		std::string evalStr = std::string(this->lastTatianaNumber);

		int topVal = evalStr.size() - 2;

		while (!this->IsSolution(evalStr))
		{


			for (int i = topVal; i >=0; i--)
			{
				char firstDigit = this->GetGreaterDigit( evalStr,i);
				char lastDigit = evalStr[i+1];

				if (firstDigit > lastDigit)
				{
				//	evalStr.replace(i+1, 1, 1, '9');
					bool offset = false;
					bool firstEval = true;

					for (size_t j = i+1; j > 0; j--)
					{
						bool someChange = false;
						firstDigit = evalStr[j-1];
						lastDigit = evalStr[j];

						if (firstEval || firstDigit > lastDigit)
						{
							firstEval = false;
							offset = true;
							lastDigit = '9';
						
						}
						else
							if (lastDigit == '0')
							{
								lastDigit = '9';
								offset = true;
							
							}
							
							if (offset)
							{
								if (firstDigit == '0')
								{
									firstDigit = '9';
									
								}
								else
								{
									firstDigit--;
									if (j>0)
									offset = false;
								}
								someChange = true;

							}
							evalStr.replace(j-1, 1, 1, firstDigit);
							evalStr.replace(j, 1, 1, lastDigit);

							if (lastDigit == '9' && someChange)
							{
								for (int x = evalStr.size()-1; x > j; x--) {
									evalStr.replace(x, 1, 1, '9');
								}
							}

						
	
					}

				}

			}
		}

		if (evalStr.size() > 1 && evalStr[0] == '0')
		{
			evalStr.replace(0, 1, 0, '0');
		}

		std::strcpy(result, evalStr.c_str());

		return result;
	}
};

class TestCaseRepository
{
private:
	std::ifstream myfile;
	std::ofstream outfile;
	int casesCount;
	int currentCase;

public:
	TestCaseRepository(char* filename)
	{

		myfile.open(filename, std::ios::in);

		std::string outputFilename(filename);
		outputFilename.replace(outputFilename.size() - 2, 2, "out");
		outfile.open(outputFilename, std::ios::out);

		char countstr[128];

		myfile.getline(countstr, 128);
		this->casesCount = std::atoi(countstr);
		this->currentCase = 0;

	}

	TestCase* Next()
	{
		if (this->casesCount == this->currentCase)
		{
			return NULL;
		}

		this->currentCase++;

		char buffer[8000];

		myfile.getline(buffer, 8000);

		TestCase *testCase = new TestCase(buffer);


		return testCase;
	}

	void PrintResult(const TestCase &testCase)
	{
		char buffer[8000];
		int theLength = std::sprintf(buffer, "Case #%d: %s", this->currentCase, testCase.Solve());
		if (this->currentCase > 1)
		{
			this->outfile.write("\n", 1);
		}
		this->outfile.write(buffer, theLength);
	}

	~TestCaseRepository()
	{
		myfile.close();

		outfile.close();
	}
};


int main(int argc, char **argv)
{
	TestCaseRepository repo(argv[1]);
	TestCase *testCase;
	while ((testCase = repo.Next()) != NULL)
	{
		testCase->Solve();
		repo.PrintResult(*testCase);

		delete testCase;
	}

	return 0;
}

