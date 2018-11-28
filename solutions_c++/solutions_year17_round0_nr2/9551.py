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

typedef vector<long> LongVector;


std::string func(std::string input)
{

    int len = input.size();
    int i=0;
    while(i<len-1 && input[i]<=input[i+1])
    {
        i += 1;
    }
    //cout <<"i " << i << endl;
    if(i == len-1)
        //cout<< input; // return
        return input;
    else
    {
        int k = i+1;
        while(k<len)
        {
            input[k] = '9';
            k += 1;
        }
      //  cout << "inp 1: "<< input<<endl;
        if(input[i]!='1')
        {
            int j=i;
            char ch2 = input[i];
            char ch = input[i]-1;
            input[j] = ch;
            j -= 1;
            while(j>=0 && input[j] == ch2)
                {
                    input[j] = ch;
                    j -= 1;
                }
             if(j < 0)
             {
                 int p=1;
                 while(p < len && p <=i )
                 {
                     input[p] = '9';
                     p += 1;
                 }
             }
            //cout << input; // return
            return input;
        }
        else
        {
            int m=i;
            input[m] = '9';
            m -= 1;
            while(m>=0)
                {
                    input[m] = '9';
                    m -= 1;
                }
         //   cout <<"bp2"<<endl;
            input.erase(input.begin());
            //cout << input; // return
            return input;
        }

    }

}



int main()
{

    long testCase,curTestCase;
    //cin >> testCase;
    std::string line;
    std::istringstream iss;

    ifstream myfile;
    myfile.open("input.txt",ios::in);

    ofstream outfile;
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
        if (std::getline(myfile, line))
            {
        //        cout << line;
            iss2.str(line);
            iss2 >> strCurVal;
        //    cout << "Cursize "<< cursize << endl;
            }


    std::string res = func(strCurVal);
    //cout << res << endl;
    outfile << "Case #"<<curTestCase+1<<": "<<res<<endl;
    }
    //cout << "Hello world!" << endl;
    return 0;
}
