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

void readData(const string &strDataFile, int &iTC, vector< vector <int> > &vState,
        vector<int> &vPanSize)
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
		
		string sCakes = vTokens[0];
// 		cout << "Cakes: "<< sCakes << endl;
		
		int iPanSize = std::stoi(vTokens[1],&sz);
		vPanSize.push_back(iPanSize);
// 		cout << "Pan size: "<<iPanSize << endl;
		
		vector<int> vCurrentState;
		for (string::const_iterator i1 = sCakes.begin(), iend = sCakes.end(); i1 < iend; ++i1)
		{
		  if(*i1 == '+')
			vCurrentState.push_back(1);
		  else if(*i1 == '-')
			vCurrentState.push_back(0);
		}
		vState.push_back(vCurrentState);
    }
}


int flip(vector<int> vCurState, int iPS)
{
	int iMaxIndex = vCurState.size() - iPS;
	int iTries = 0;
	int iOldBestIndex = -2;
	while(1)
	{
	  
	  if(std::find(vCurState.begin(), vCurState.end(), 0) != vCurState.end())
	  {
		int iMaxNeg = -1;
		int iBestIndex = -1;
		int iNegPos = 10000;
		for (int i = 0; i <= iMaxIndex; ++i)
		{
			int iNumNegs = 0;
			int iTNP = 10000;
			for(int j = 0; j < iPS; ++j)
			{
				if(vCurState[j+i] == 0)
				{
				  iNumNegs++;
				  if(j < iTNP)
					iTNP = j;
				}
			}
			if(iNumNegs>=iMaxNeg &&  iTNP<iNegPos)
			{
			  iMaxNeg = iNumNegs;
			  iBestIndex = i;
			  iNegPos = iTNP;
			}
		}
		if(iOldBestIndex == iBestIndex)
		{
// 		  cout <<"Cannot be solved" << endl;
		  return -1;
		}
		
		iOldBestIndex = iBestIndex;
		
// 		cout << "Best Index: "<< iBestIndex << endl;
// 		for(int k = 0; k < vCurState.size(); ++k)
// 		{
// 		  cout <<" "<< vCurState[k] <<" ";
// 		}
// 		cout << ": Before" << endl;
		for (int i = iBestIndex; i < iBestIndex + iPS; ++i)
		{
			if(vCurState[i] == 0)
			  vCurState[i] = 1;
			else
			  vCurState[i] = 0;
		}
// 		for(int k = 0; k < vCurState.size(); ++k)
// 		{
// 		  cout <<" "<< vCurState[k] <<" ";
// 		}
// 		cout << ": After" << endl;
		
		iTries++;
// 		cout << "Tries: " << iTries << endl;
	  }
	  else
		break;
	}
// 	cout << "Took: " <<iTries << " tries" <<endl;
	return iTries;
}


void writeFile(const string &strDataFile, vector<int> vOutput)
{
	std::ofstream myfile;
	myfile.open (strDataFile.c_str());
	for(int i = 0; i < vOutput.size(); ++i)
	{
		std::stringstream outss;
		outss << "Case #"<< i+1 << ": ";
		if(vOutput[i] < 0)
		  outss << "IMPOSSIBLE" << endl;
		else
		  outss << vOutput[i] << endl;
		myfile << outss.str();
	}
	myfile.close();
}

int main(int argc, char **argv) 
{

	int iTestCases = 0;
	vector< vector <int> > vState;
	vector<int> vPanSize;
	
	if(argc != 3)
	{
	  cout << "Usage: ./pancakes InputFile > OutputFile" << endl;
	  exit(-1);
	}
	string strInput = string(argv[1]);
	string strOutput = string(argv[2]);
	readData(strInput, iTestCases, vState, vPanSize);
	
	vector<int> vOutput;
	for(int j = 0; j < vState.size(); ++j)
	{
	  vector<int> vCurrentState = vState[j];
// 	  for(int k = 0; k < vCurrentState.size(); ++k)
// 	  {
// 		cout <<" "<< vCurrentState[k] <<" ";
// 	  }
// 	  cout <<" : "<< vPanSize[j]<< endl;
	  
	  int iTries = flip(vCurrentState, vPanSize[j]);
	  vOutput.push_back(iTries);
	}
	
	writeFile(strOutput,vOutput);
	
	
    return 0;
}
