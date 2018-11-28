// Pancakes2017.cpp: define el punto de entrada de la aplicación de consola.
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
	std::string pancakes;
	int flipperK;

	bool IsSolution(const std::string &str) const
	{
		return str.find('-', 0) == std::string::npos;
	}

public:
	TestCase(const char (& lines)[8000])
	{
		std::string inputStr(lines);

		size_t whiteSpaceIdx = inputStr.find(' ', 0);

		this->pancakes = inputStr.substr(0, whiteSpaceIdx);
		std::string kStr = inputStr.substr(whiteSpaceIdx, (inputStr.length() - whiteSpaceIdx));
		this->flipperK = atoi(kStr.c_str());
	}

	 char *Solve() const
	{
		 if (this->IsSolution(this->pancakes))
		 {
			 return "0";
		 }
		
		 char result[8000];

		 std::strcpy(result, "IMPOSSIBLE");

		 if (this->pancakes.size() >= (size_t)this->flipperK)
		 {

			 std::queue<std::string> queue;
			 

			 queue.push(this->pancakes);

			 std::map<std::string, long> pancakesFlips;

			 pancakesFlips.insert(std::pair<std::string, long>(this->pancakes, 0));

			 long betterSolution = INT_MAX-1000;

			 long flipCount = 0;

			 while(queue.size()>0)
			 {
				 std::string current = queue.front();
				 queue.pop();

				 flipCount = pancakesFlips[current];

				 if (flipCount >= betterSolution)
				 {
					 continue;
				 }
				 

				 if (this->IsSolution(current))
				 {
					 betterSolution = flipCount;
					 continue;
				 }

				 int possibleFlipsCount = current.size() - this->flipperK;

				 for (int i = possibleFlipsCount; i >= 0; i--)
				 {
					 std::string pancakesFlipped( current);
					
					 for (int rIdx = i, charCounter = 0; charCounter < this->flipperK;charCounter++, rIdx++)
					 {
						 pancakesFlipped.replace(rIdx,1,1,(pancakesFlipped[rIdx] == '+'?'-':'+' ));
							 
					 }

					 long newCount = flipCount + 1;

					 std::map<std::string, long>::iterator mIter = pancakesFlips.find(pancakesFlipped);
					
					 if (mIter == pancakesFlips.end())
					 {
						 pancakesFlips.insert(std::pair<std::string, long>(pancakesFlipped, newCount));
						 queue.push(pancakesFlipped);
					 }
					 else
					 {
						 if (mIter->second > newCount )
						 {
							 pancakesFlips[current] = newCount;
							 queue.push(pancakesFlipped);
						 }
					 }
					 
				 }
			 }


			 if (betterSolution < (INT_MAX - 1000))
			 {
				 sprintf(result,"%d", betterSolution);
			 }
		 }

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
	TestCaseRepository( char* filename)
	{
		
		myfile.open(filename,std::ios::in);

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

		myfile.getline(buffer,8000);

		TestCase *testCase = new TestCase( buffer);


		return testCase;
	}

	void PrintResult(const TestCase &testCase)
	{
		char buffer[8000];
		int theLength = std::sprintf(buffer, "Case #%d: %s", this->currentCase, testCase.Solve());
		if (this->currentCase > 1)
		{
			this->outfile.write("\n",1);
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

