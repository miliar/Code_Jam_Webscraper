#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <math.h>
using namespace std;

int main()
{
    ofstream outFile("D:\\Code Jam\\2017\\Qual\\main\\outLarge.txt");
    ifstream inFile("D:\\Code Jam\\2017\\Qual\\main\\A-large.in");
    if(inFile.is_open())
    {
        //cout << "open " << endl;
        string line;
        getline(inFile, line);
        //cout << line << endl;
        long testCases = strtol(line.c_str(), NULL, 0);
        for (int test = 1 ; test <= testCases; test++)
        {
            getline(inFile, line);

            string delimiter = " ";
            size_t pos = 0;
            string token[2];
            int i = 0;
            while ((pos = line.find(delimiter)) != std::string::npos)
            {
                token[i] = line.substr(0, pos);
                i++;
                line.erase(0,pos + delimiter.length());
            }
            token[1] = line;
            string row = token[0];

            int numFlip = 0;
            int k = strtol(token[1].c_str(), NULL, 0);
            i = 0;
            //cout << row << " " << k << endl;
            while (i < row.length())
            {
                if(row[i] == '-')
                {
                    if(i + k <= row.length())
                    {
                        numFlip++;
                        row[i] = '+';
                        for (int j = 1;j < k; j++)
                        {
                            row[i + j ] = (row[i + j] == '+') ? '-' : '+';
                        }
                    }
                    else
                        numFlip = -1;
                }
                i++;
            }
            if(numFlip == -1)
                outFile << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
            else
                outFile << "Case #" << test << ": " << numFlip << endl;
        }

        outFile.close();
        inFile.close();
    }
}
