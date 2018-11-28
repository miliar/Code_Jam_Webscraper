#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
#include <sstream> 
#include <stdlib.h>

using namespace std;

void tokenize(const string &str, vector<string> &vTokens)
{
    int iPos = 0;
    int iTokBeg = 0;
    while (iPos < (int) str.length())
    {
        if (str[iPos] == ' ')
        {
            if (iTokBeg < iPos)
            {
                vTokens.push_back(str.substr(iTokBeg, iPos - iTokBeg));
                iTokBeg = iPos + 1;
            }
        }
        iPos++;
    }
    if (iTokBeg < (int) str.length())
        vTokens.push_back(str.substr(iTokBeg));
}

void readData(const string &strDataFile, int &iTC, vector<long long int> &vNumbers)
{
    ifstream f;
    f.open(strDataFile.c_str());
    if (!f.is_open())
    {
        cout << "Could not open frame data file " << strDataFile << endl;
		exit(-1);
    }
//     cout << "Reading file" << endl;
    
    bool bFirst = false;
    while (f.is_open() && !f.eof())
    {
        string s;
		string::size_type sz;
        getline(f, s);
        if (s.length() == 0)
            continue;
		if (!bFirst)
		{
			iTC = std::stoi(s);
			bFirst = true;
// 			cout <<"Test cases:" << iTC << endl;
			continue;
		}
		
		vector<string> vTokens;
		tokenize(s, vTokens);
		if (vTokens.size() > 1)
		  continue;

		long long int iNumber = std::stoll(vTokens[0],&sz);
		vNumbers.push_back(iNumber);
// 		cout << "Counted : "<<iNumber<< endl;
    }
}


long long int tidy(long long int llCounts)
{
	long long int llIndex = llCounts;
	long long int llLastTidy = llCounts;
	
	// Eliminate single digit number case
	if(llCounts <10)
	  return llCounts;
// 	cout<<"counting for "<< llCounts<<endl;
	
	while(llIndex > 0)
	{
		stringstream checkss;
		checkss << llIndex;
		string strCheck = checkss.str();
		bool isTidy = true;
		int iPos = 1;
		for(string::const_iterator it1 = strCheck.begin()+1, itend = strCheck.end(); it1 < itend; ++it1)
		{
			int iPrev = (int)(*(it1-1)) - '0';
			int iCur = (int)(*it1) - '0';
			if(iPrev>iCur)
			{
			  isTidy = false;
			  
			  if(it1 == itend - 1 && iCur == 0)
			  {
				//Subtract -1
				llIndex -= 1;
			  }
			  else
			  {
				string strNewVal(strCheck.length() - iPos, '0');
				strCheck.replace(iPos, strCheck.length() - iPos, strNewVal);
				long long int llReplace = std::stoll(strCheck);
				if(llIndex==llReplace)
				  llReplace -= 1;
				llIndex = llReplace;
				
			  }
			  break;
			}
			iPos++;
		}
		if(isTidy)
		{
		  llLastTidy = llIndex;
		  return llLastTidy;
		}
	}
	return llLastTidy;
}

void writeFile(const string &strDataFile, vector<long long int> vOutput)
{
	std::ofstream myfile;
	myfile.open (strDataFile.c_str());
	for(int i = 0; i < vOutput.size(); ++i)
	{
		std::stringstream outss;
		outss << "Case #"<< i+1 << ": ";
		outss << vOutput[i] << endl;
		myfile << outss.str();
	}
	myfile.close();
}

int main(int argc, char **argv) 
{

	int iTestCases = 0;
	vector<long long int> vNumbers;
	
	if(argc != 3)
	{
	  cout << "Usage: ./pancakes InputFile > OutputFile" << endl;
	  exit(-1);
	}
	string strInput = string(argv[1]);
	string strOutput = string(argv[2]);
	readData(strInput, iTestCases, vNumbers);
	
	if(iTestCases != vNumbers.size())
	{
	  cout << "Test case numbers not matching!!" << endl;
	  exit(-1);
	}
	
	vector<long long int> vOutput;
	for (int i = 0; i < iTestCases; i++)
	{
		long long int llTidyNum = tidy(vNumbers[i]);
		vOutput.push_back(llTidyNum);
	}
	
	writeFile(strOutput, vOutput);
    return 0;
}
