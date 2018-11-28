#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector< string > tokenize(string strInput, string strDelim)
{
	vector< string > vecRet;
	while (strInput.find(strDelim) != string::npos)
	{
		int idx = strInput.find(strDelim);
		vecRet.push_back(strInput.substr(0, idx));
		strInput = strInput.substr(idx + 1);
	}

	vecRet.push_back(strInput);
	return vecRet;
}

void main()
{
	string strLine;
	fstream fs("input.txt", ios_base::in);
	fstream fout("output.txt", ios_base::out);
	int iNumTC = 0;
	getline(fs, strLine);
	iNumTC = atoi(strLine.c_str());

	for (int t = 0; t < iNumTC; t++)
	{
		int N, P;
		fs >> N;
		fs >> P;
		getline(fs, strLine);

		int* arrReq = new int[N];
		int** arrPackages = new int*[N];
		bool** arrUsed = new bool*[N];
		getline(fs, strLine);
		vector< string > vecTokReq = tokenize(strLine, " ");

		vector< string > vecInput;
		vecInput.push_back(strLine);
		for (int i = 0; i < N; i++)
		{
			arrReq[i] = atoi(vecTokReq[i].c_str());

			getline(fs, strLine);
			vecInput.push_back(strLine);
			arrPackages[i] = new int[P];
			arrUsed[i] = new bool[P];
			vector< string > vecIngredients = tokenize(strLine, " ");
			for (int j = 0; j < P; j++)
			{

				arrPackages[i][j] = atoi(vecIngredients[j].c_str());
				arrUsed[i][j] = false;
			}

			// Sort in inc. order.
			for (int j = 0; j < P; j++)
			{
				for (int k = j + 1; k < P; k++)
				{
					if (arrPackages[i][k] < arrPackages[i][j])
					{
						int iTmp = arrPackages[i][j];
						arrPackages[i][j] = arrPackages[i][k];
						arrPackages[i][k] = iTmp;
					}
				}
			}
		}

		// Find appropriate ingredient.
		int iCnt = 0;
		for (int i = 0; i < P; i++)
		{
			int iPackageMin = ((float)arrPackages[0][i] / arrReq[0]) * 0.9;
			int iPackageMax = ((float)arrPackages[0][i] / arrReq[0]) * 11.0 / 9.0 + 1;
			vector< int > vecTestSize;
			for (int j = iPackageMin; j <= iPackageMax; j++)
			{
				if (0.9 * j * arrReq[0] <= arrPackages[0][i] && 1.1 * j * arrReq[0] >= arrPackages[0][i])
				{
					vecTestSize.push_back(j);
				}
			}

			if (vecTestSize.size() == 0) continue;
			for (size_t ts = 0; ts < vecTestSize.size(); ts++)
			{
				int iPackageSize = vecTestSize[ts];
				vector< int > vecAcceptables;
				bool bFail = false;
				for (int j = 1; j < N; j++)
				{
					int iAvPackage = -1;
					for (int k = 0; k < P; k++)
					{
						if (1.1 * iPackageSize * arrReq[j] < arrPackages[j][k])	break;
						if (!arrUsed[j][k] && 0.9 * iPackageSize * arrReq[j] <= arrPackages[j][k] && 1.1 * iPackageSize * arrReq[j] >= arrPackages[j][k])
						{
							iAvPackage = k;
							break;
						}
					}
					if (iAvPackage == -1)
					{
						bFail = true;
						break;
					}
					vecAcceptables.push_back(iAvPackage);
				}

				if (!bFail)
				{
					iCnt++;				
				//	cout << "PACKAGE: " << arrPackages[0][i] << " ";
					for (int j = 0; j < vecAcceptables.size(); j++)
					{
						arrUsed[j + 1][vecAcceptables[j]] = true;	
					//	cout << arrPackages[j + 1][vecAcceptables[j]] << " ";
					}					
					//cout << " with " << iPackageSize << " packages" << endl;
					//cout << endl;
					break;
				}
			}

		}
		fout << "Case #" << (t + 1) << ": " << iCnt << endl;
	}

	fout.close();
	fs.close();

}



