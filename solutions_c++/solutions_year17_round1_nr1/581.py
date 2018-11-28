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
		int R, C;
		fs >> R;
		fs >> C;		
		getline(fs, strLine);

		char** arrData = new char*[R];		
		for (int j = 0; j < R; j++)
		{
			getline(fs, strLine);
			arrData[j] = new char[C];
			for (int k = 0; k < C; k++)
			{
				arrData[j][k] = strLine[k];
			}
		}

		// 1. Fill the lines except those with all ?s.
		for (int j = 0; j < R; j++)
		{			
			bool bHasAlphabet = false;
			for (int k = 0; k < C; k++)
			{
				if (arrData[j][k] != '?')
				{
					bHasAlphabet = true;
				}				
			}

			if (bHasAlphabet)
			{
				bool bFirstShown = false;
				char cInsert = 0;
				for (int k = 0; k < C; k++)
				{
					if (arrData[j][k] != '?' )
					{
						if (!bFirstShown)
						{
							for (int m = 0; m < k; m++)
							{
								arrData[j][m] = arrData[j][k];
							}
							bFirstShown = true;
						}
						cInsert = arrData[j][k];
					}
					else if (bFirstShown)
					{
						arrData[j][k] = cInsert;
					}
				}
			}
		}

		// 2. Fill the lines with all ?s. (Just copy!)
		bool bFirstLineShown = false;
		for (int j = 0; j < R; j++)
		{
			if (arrData[j][0] != '?')
			{
				if (!bFirstLineShown)
				{
					for (int k = 0; k < C; k++)
					{
						for (int m = 0; m < j; m++)
						{
							arrData[m][k] = arrData[j][k];
						}
					}
					bFirstLineShown = true;
				}
			}
			else
			{
				if (bFirstLineShown)
				{
					for (int k = 0; k < C; k++)
					{
						arrData[j][k] = arrData[j - 1][k];
					}
				}
			}
		}

		fout << "Case #" << ( i + 1 ) << ":" << endl;
		for (int j = 0; j < R; j++)
		{
			for (int k = 0; k < C; k++)
			{
				fout << arrData[j][k];
			}
			fout << endl;
		}
	
	}

	fout.close();
	fs.close();

}





