#include <fstream>
#include <iostream>
#include <string>

using namespace std;

void main()
{
	string strLine;
	fstream fs("input.txt", ios_base::in);
	fstream fout("output.txt", ios_base::out);
	int iNumTC = 0;
	getline(fs, strLine);
	iNumTC = atoi(strLine.c_str());

	for (int i = 0; i < iNumTC; i++)
	{
		string strData = "";
		int K = 0;
		fs >> strData >> K;
		int iFlipCnt = 0;
		bool bPossible = true;
		for (int j = 0; j < strData.size(); j++)
		{
			if (strData[j] == '-')
			{	// Flip if possible;
				if (j + K > strData.size())
				{
					bPossible = false;
					break;
				}
				for (int k = j; k < j + K; k++)
				{
					if (strData[k] == '-')		strData[k] = '+';
					else if (strData[k] == '+')	strData[k] = '-';
				}
				iFlipCnt++;				
			}
		}
		if (!bPossible)
		{
			fout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
		}
		else
		{
			fout << "Case #" << (i + 1) << ": " << iFlipCnt << endl;
		}
	}

	fout.close();
	fs.close();
	
}





