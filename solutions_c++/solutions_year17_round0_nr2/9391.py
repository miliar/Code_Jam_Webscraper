#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <math.h>
using namespace std;

int main()
{
    ofstream outFile("D:\\Code Jam\\2017\\Qual\\B Tidy Numbers\\main\\out1.txt");
    ifstream inFile("D:\\Code Jam\\2017\\Qual\\B Tidy Numbers\\main\\B-small-attempt1.in");
    int x,y,progress_theta_degree,test;
    double point_theta_rad = 0, m = 0, progress_theta_rad = 0;
    bool bIsWhite = false;
    if(inFile.is_open())
    {
        //cout << "open " << endl;
        string line;
        getline(inFile, line);
        //cout << line << endl;
        long testCases = strtol(line.c_str(), NULL, 0);
        for (test = 1 ; test <= testCases; test++)
        {
            getline(inFile, line);
            int N[18];
            bool bTidy = true;
            char num = 0;
            for (int i = 0; i < line.length(); i++)
            {
                num = line[i];
                N[i] = strtol(&num, NULL, 0);

            }

            //cout << line.length() << endl;
            for (int i = 0; i < line.length() - 1; i++)
            {
                //cout << N[i] << endl;
                if(N[i] > N[i + 1])
                    bTidy = false;
            }

            for(int i = 0; i< line.length() - 1 && !bTidy; i++)
            {
                if(N[i] >= N[i+1])
                {
                    N[i]--;
                    for (int j = i + 1; j < line.length(); j++)
                        N[j] = 9;
                    break;
                }
            }

            outFile << "Case #" << test << ": ";
            bool bFirstTime = true;
            for (int i = 0; i < line.length(); i++)
            {
                if (bFirstTime && N[i] == 0)
                    continue;

                outFile << N[i];
            }
           outFile << endl;
        }

        outFile.close();
        inFile.close();
    }
}
