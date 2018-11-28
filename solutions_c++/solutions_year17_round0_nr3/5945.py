#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
#include <sstream> 
#include <stdlib.h>
#include <climits>

using namespace std;

struct stallInfo {
  long long int llIndex;
  long long int llLeft;
  long long int llRight;
  bool direction;
} ;
	
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

void readData(const string &strDataFile, int &iTC, vector<long long int> &vNumbers, vector<long long int> &vPeople)
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
		if (vTokens.size() > 2)
		  continue;

		long long int llNumber = std::stoll(vTokens[0],&sz);
		vNumbers.push_back(llNumber);
		
		long long int llPeople = std::stoll(vTokens[1],&sz);
		vPeople.push_back(llPeople);
// 		cout << "Counted : "<<llNumber<<" "<<llPeople<< endl;
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


void findIndex(stallInfo stInfo, bool init)
{
	
}

void countStallsOld(long long int llStalls, long long int llPeople)
{
	

	vector<stallInfo> vStallInfo;
	
	long long int llDivConst = 2;
  
	stallInfo siPrev;
	siPrev.llIndex = 0;
	siPrev.llLeft = 0;
	siPrev.llRight = 0;
	
	
	long long int llStallIndex = llStalls / llDivConst;
	
	lldiv_t llDiv;
	llDiv = div(llStalls,llDivConst);
	if(llDiv.rem != 0)
	{
	  llStallIndex++;
	}
	siPrev.llIndex = llStallIndex;
	siPrev.llLeft = llStallIndex-1;
	siPrev.llRight = llStalls - llStallIndex;
	vStallInfo.push_back(siPrev);
	
	for(long long int i = 0; i < llPeople-1; ++i)
	{
		vector<long long int> vMaxLower;
		vector<long long int> vMaxUpper;
		
		for(long long int j = 0; j < vStallInfo.size(); ++j)
		{
			long long int llmaxLower = min(vStallInfo[j].llLeft,vStallInfo[j].llRight);
			vMaxLower.push_back(llmaxLower);
			
			long long int llmaxUpper = max(vStallInfo[j].llLeft,vStallInfo[j].llRight);
			vMaxUpper.push_back(llmaxUpper);
		}
		if(vMaxLower.size()!=vMaxUpper.size())
		{
			cout << "Max min not same!!!"<<endl;
			exit(-1);
		}
		
		long long int llMinInd = -1, llMaxInd = -1;
		long long int llMinVal = -1, llMaxVal = -1;
		bool minRepeat = false, maxRepeat = false;
		for(long long int j = 0; j < vMaxLower.size(); ++j)
		{
			if(vMaxLower[j]>llMinVal)
			{
			  llMinVal = vMaxLower[j];
			  llMinInd = j;
			  minRepeat = false;
			}
			else if(vMaxLower[j]==llMinVal)
			  minRepeat=true;
			
			if(vMaxUpper[j]>llMaxVal)
			{
			  llMaxVal = vMaxUpper[j];
			  llMaxInd = j;
			  maxRepeat = false;
			}
			else if(vMaxUpper[j]==llMaxVal)
			  maxRepeat = true;
		}
		llStallIndex = llStalls / llDivConst;
		
// 		lldiv_t llDiv;
		llDiv = div(llStalls,llDivConst);
		if(llDiv.rem != 0)
		{
		  llStallIndex++;
		}
		
		
		
		siPrev.llIndex = llStallIndex;
// 		siPrev.llLeft = 
		cout << "Div: "<<llStallIndex<<endl;
	}
}


stallInfo countStalls(long long int llStalls, long long int llPeople)
{
	vector<stallInfo> vStallInfo;
	
	long long int llDivConst = 2;
  
	stallInfo siPrev, siLast;
	siPrev.llIndex = 0;
	siPrev.llLeft = 0;
	siPrev.llRight = 0;
	
	
	long long int llStallIndex = llStalls / llDivConst;
	
	lldiv_t llDiv;
	llDiv = div(llStalls,llDivConst);
	if(llDiv.rem != 0)
	{
	  llStallIndex++;
	}
	siPrev.llIndex = llStallIndex;
	siPrev.llLeft = llStallIndex-1;
	siPrev.llRight = llStalls - llStallIndex;
	vStallInfo.push_back(siPrev);
	siLast = siPrev;
// 	cout <<"Index: ";
// 		for(long long int l = 0; l < vStallInfo.size(); ++l)
// 		{
// 		  cout<<" "<<vStallInfo[l].llIndex<<",";
// 		}
// 		cout << "."<<endl;
	for(long long int i = 0; i < llPeople-1; ++i)
	{
		
		long long int llMax = -1, llvIndex = 0;
		
		stallInfo siBlock, siVal;
		
		for(long long int j = 0; j < vStallInfo.size(); ++j)
		{
			long long int llmaxGap = max(vStallInfo[j].llLeft,vStallInfo[j].llRight);
			
			if(llmaxGap > llMax)
			{
				siBlock.llIndex = vStallInfo[j].llIndex;
				if(llmaxGap==vStallInfo[j].llLeft)
				  siBlock.direction = false;
				else
				  siBlock.direction = true;
				llMax = llmaxGap;
				llvIndex = j;
// 				cout << "llmaxgap: "<<llmaxGap<<", llMax: "<<llMax<<", vals: "<<vStallInfo[j].llLeft<<", "<<vStallInfo[j].llRight<<" dir: "<<siBlock.direction<<endl;;
			}
		}
		
		if(llMax > 0)
		{
		  llStallIndex = llMax / llDivConst;
	
		  lldiv_t llDiv;
		  llDiv = div(llMax,llDivConst);
		  if(llDiv.rem != 0)
		  {
			llStallIndex++;
		  }
		  
		  if(siBlock.direction) //Insert Right
		  {
			siVal.llIndex = siBlock.llIndex + llStallIndex;
			siVal.llLeft = siVal.llIndex - siBlock.llIndex - 1;
			if(llvIndex != vStallInfo.size()-1)
			{
			  siVal.llRight = vStallInfo[llvIndex+1].llIndex - siVal.llIndex - 1;
			  vStallInfo[llvIndex+1].llLeft = siVal.llRight;
			  vStallInfo[llvIndex].llRight = siVal.llLeft;
// 			  cout<<"llvindex: "<<llvIndex<<endl;
			  vStallInfo.insert(vStallInfo.begin()+llvIndex+1,siVal);
			}
			else
			{
			  siVal.llRight = llStalls - siVal.llIndex;
			  vStallInfo[llvIndex].llRight = siVal.llLeft;
			  vStallInfo.push_back(siVal);
			}
		  }
		  else // Insert Left 
		  {
			siVal.llIndex = siBlock.llIndex - llMax - 1 + llStallIndex;
			siVal.llRight = siBlock.llIndex - siVal.llIndex - 1;
			if(llvIndex != 0)
			{
			  siVal.llLeft = siVal.llIndex - vStallInfo[llvIndex-1].llIndex - 1;
			  vStallInfo[llvIndex-1].llRight = siVal.llLeft;
			}
			else
			  siVal.llLeft = siVal.llIndex - 1;
			vStallInfo[llvIndex].llLeft = siVal.llRight;
			vStallInfo.insert(vStallInfo.begin()+llvIndex,siVal);
		  }
		  siLast = siVal;
		}
// 		cout <<"Index: ";
// 		for(long long int l = 0; l < vStallInfo.size(); ++l)
// 		{
// 		  cout<<" "<<vStallInfo[l].llIndex<<",";
// 		}
// 		cout << "."<<endl;
	}
// 	cout<<vStallInfo.size()<<endl;
// 	cout << "Last: "<<siLast.llLeft << ", "<< siLast.llRight<< endl;
	return siLast;
}

void writeFile(const string &strDataFile, vector<stallInfo> vOutput)
{
	std::ofstream myfile;
	myfile.open (strDataFile.c_str());
	for(int i = 0; i < vOutput.size(); ++i)
	{
		std::stringstream outss;
		outss << "Case #"<< i+1 << ": ";
		outss << max(vOutput[i].llLeft,vOutput[i].llRight) << " ";
		outss << min(vOutput[i].llLeft,vOutput[i].llRight) << endl;
		myfile << outss.str();
	}
	myfile.close();
}

int main(int argc, char **argv) 
{

	int iTestCases = 0;
	vector<long long int> vStalls;
	vector<long long int> vPeople;
	
	if(argc != 3)
	{
	  cout << "Usage: ./pancakes InputFile > OutputFile" << endl;
	  exit(-1);
	}
	string strInput = string(argv[1]);
	string strOutput = string(argv[2]);
	readData(strInput, iTestCases, vStalls, vPeople);
	
	if(iTestCases != vStalls.size())
	{
	  cout << "Test case numbers not matching!!" << endl;
	  exit(-1);
	}
	
	vector<stallInfo> vOutput;
	for (int i = 0; i < iTestCases; i++)
	{
		stallInfo siReturn = countStalls(vStalls[i],vPeople[i]);
		vOutput.push_back(siReturn);
	}
	
	writeFile(strOutput, vOutput);
    return 0;
}
