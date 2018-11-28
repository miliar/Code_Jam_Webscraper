#include <fstream>
#include <string>

class COutputGenerator
{

public:

	void initFile(const std::string a_rFileName);

	void writeTest(int a_nCaseID, int a_nResult);
	void writeTest(int a_nCaseID, double a_fResult);
	void writeTest(int a_nCaseID, long long a_lResult);
	void writeTest(int a_nCaseID, std::string a_Result);

	void closeFile();

	std::ofstream m_outputFile;



};