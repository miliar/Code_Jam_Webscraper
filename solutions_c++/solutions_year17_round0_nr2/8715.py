#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;
ifstream myfile;
ofstream myfile2;
bool isTidy(string num);
string makeTidy(unsigned long long num );

int main()
{
    int numberOfCases=0;
    unsigned long long  maxNum=0;
    unsigned long long  lastTidy=0;

     myfile.open ("B-large.in");
     myfile2.open ("example.out");

     myfile>>numberOfCases;

     for (int i=0; i<numberOfCases; i++)
     {

         myfile>>maxNum;

        istringstream(makeTidy(maxNum)) >> lastTidy;
                 myfile2<<"Case #"<<i+1<<": "<<lastTidy<<endl;



     }

    return 0;
}

bool isTidy(string number)
{



    if (number.length()==1)
    {
        return true;
    }
    for (int i=1; i<number.length(); i++)
    {
        if ((int)number[i]<(int)number[i-1])
        {
            return false;
        }
    }
    return true;

}
string makeTidy(unsigned long long num)
{
    stringstream ss;
    ss<<num;

    string number= ss.str();
    //cout<<number<<endl;
        for (int i=number.length()-1; i>=0 && !isTidy(number); i--)
        {
            number[i]='9';
            if (i!=0)
            {
                number[i-1]-=1;
            }

        }

    return number;
}
