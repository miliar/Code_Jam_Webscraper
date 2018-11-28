#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

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
		char arrData[25];
		fs >> arrData;
		int iLen = strlen(arrData);
		
		for (int j = iLen - 1; j > 0; j--)
		{
			if (arrData[j] < arrData[j - 1])
			{
				int k = j - 1;
				while (arrData[k] == '0')
				{
					arrData[k] = '9';
					k--;
				}
				arrData[k]--;
				for (int m = j; m < iLen; m++)
				{
					arrData[m] = '9';
				}
			}
		}

		stringstream ss;
		bool bBegin = false;
		for (int j = 0; j < iLen; j++)
		{
			if (arrData[j] != '0')	bBegin = true;
			if (bBegin)	ss << arrData[j];
		}

		fout << "Case #" << (i + 1) << ": " << ss.str() << endl;		
	}

	fout.close();
	fs.close();

}





