// tidynumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
    fstream fInput, fOutput;
    fInput.open("in.txt", ios::in);
    fOutput.open("out.txt", ios::out);

    if (fInput.good() && fOutput.good())
    {
        int iNumLine = 0;
        string sLine;
        if (getline(fInput,sLine))
        {
            sscanf_s(sLine.c_str(),"%d",&iNumLine);
        }

        if (iNumLine > 100 || iNumLine < 1)
        {
            return 1;
        }
        
        for (int i=1; i<=iNumLine; i++)
        {
            fOutput<<"Case #";
            fOutput<<i;
            fOutput<<": ";

            bool bSuccess = false;
			
            
            if (getline(fInput,sLine))
            {
                int iLength = sLine.length();

				if (iLength < 1)
				{
					// Should not happen
				}
				else if (iLength == 1)
				{
					fOutput<<sLine;
				}
				else
				{
					bool bLarger = false;
					int iIndexLarger = 0;
					bool bTidy = true;
					int iIndex = 0;
					for (iIndex=0; iIndex<iLength - 1; iIndex++)
					{
						if (sLine[iIndex+1] < sLine[iIndex])
						{
							bTidy = false;
							break;
						}

						if (sLine[iIndex+1] > sLine[iIndex])
						{
							bLarger = true;
							iIndexLarger = iIndex;
						}
					}

					if (bTidy)
					{
						fOutput<<sLine;
					}
					else
					{
						int iStartReduce = 0;
						if (bLarger)
						{
							iStartReduce = iIndexLarger+1;
							for (int iOut=0; iOut<iStartReduce; iOut++)
							{
								fOutput << sLine[iOut];
							}
						}

						if (iStartReduce == 0)
						{
							if (sLine[iStartReduce] == '0')
							{
								printf("impossible\n");
							}
							else if (sLine[iStartReduce] == '1')
							{
								// Skip if 1
							}
							else
							{
								char cOut = sLine[iStartReduce];
								cOut -=1;
								fOutput << cOut;
							}
						}
						else
						{
							if (sLine[iStartReduce] == '0')
							{
								printf("impossible\n");
							}
							else if (sLine[iStartReduce] == '1')
							{
								printf("impossible\n");
							}
							else
							{
								char cOut = sLine[iStartReduce];
								cOut -=1;
								fOutput << cOut;
							}
						}

						for (int iOut=iStartReduce+1; iOut<iLength; iOut++)
						{
							fOutput<<'9';
						}
					}
				}
            }
            
            fOutput<<"\n";
        }
    }
    
    fOutput.close();
    fInput.close();
	
	return 0;
}

