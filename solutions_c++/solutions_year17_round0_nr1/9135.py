#include <iostream>
#include <cstdio>
#include <math.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <unordered_map>
#include <set>

using namespace std;

ifstream myfile;
ofstream outfile;

void func(int curTestCase,std::string strInput,int k)
{
    //std::string strInput = "-+--+++----+-+";

    int len = strInput.size();
    int curPos = 0;
    int result = 0;
    while(curPos<len)
    {
        if(strInput[curPos] == '-')
        {
            if(curPos+k>len)
            {
                outfile << "Case #"<<curTestCase+1<<": IMPOSSIBLE"<<endl;
         //       cout << "Impos"<< endl;
                curPos = len;
                return;
            }
            result += 1;
            int m = curPos;
            while(m<len && m-curPos<k )
            {
                if(strInput[m] == '+')
                    strInput[m] = '-';
                else
                    strInput[m] = '+';
                m += 1;
            }
        }
        curPos += 1;
    }

    //cout << result << endl;
    outfile << "Case #"<<curTestCase+1<<": "<<result<<endl;
    //cout << "Hello world!" << endl;
    return;
}


        int main()
        {

            long testCase,curTestCase;
            //cin >> testCase;
            std::string line;
            std::istringstream iss;

            //ifstream myfile;
            myfile.open("input.txt",ios::in);

            //ofstream outfile;
            outfile.open("out.txt");

            if (std::getline(myfile, line)) {
            iss.str(line);
            iss >> testCase;
            }

            //fscanf(fpt,"%ld\n",&testCase);
           // cout << testCase;
            for(curTestCase=0;curTestCase<testCase;curTestCase++)
            {

                std::istringstream iss2;
                std::string strCurVal;
                int k;
                if (std::getline(myfile, line))
                    {
                //        cout << line;
                    iss2.str(line);
                    iss2 >> strCurVal >> k;
                //    cout << "Cursize "<< cursize << endl;
                    }


            func(curTestCase,strCurVal,k);
            //cout << res << endl;
            //outfile << "Case #"<<curTestCase+1<<": "<<res<<endl;
            }
            //cout << "Hello world!" << endl;
            return 0;
        }
