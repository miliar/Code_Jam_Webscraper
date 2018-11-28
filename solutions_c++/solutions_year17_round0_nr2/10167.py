#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

#include <string>
#include <math.h>

using namespace std;

int main()
{

    ifstream fin("B-small-attempt1.in");
    ofstream fout("B-small.out");

    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;

    int case_number,test_number,value,check_count,answer;
    fin >> case_number;

    for(int i=0; i<case_number; i++)
    {

        test_number=0;
        fin >> test_number;
        value=test_number;

        int x=std::to_string(test_number).length();
        int number[x];

        for(int i=0; i<x; i++)
        {
            number[i]=value%10;
            value/=10;
        } 

        while(true)
        {
            check_count=0;

            for(int j=x-1; j>0; j--)
            {
                if(number[j]>number[j-1])
                {
                    number[j]=number[j]-1;
                    for(int k=0; k<j; k++)
                    {
                        number[j-1-k]=9;
                    }
                }else{
                    check_count++; 
                }
            }

            if(check_count==x-1)break;

        }

        answer=0;

        for(int j=0; j<x; j++)
        {
            answer = answer + (number[j])*(int)pow(10.0,j);
        }

        fout << "Case #" << (i + 1) << ": " << answer << endl;

    }

}