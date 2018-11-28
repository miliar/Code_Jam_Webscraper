#include <iostream>
#include <fstream>
#include <cmath>
#include <sstream>

using namespace std;

string toStr(long long a)
{
    stringstream ss;
    ss << a;
    string str = ss.str();
    return str;
}

bool isTidy(long long n)
{
    string ss = toStr(n);
    int dits=ss.size();
    int nrs[dits];


    for (int k=0;k<dits;k++)
    {
        nrs[k]=ss[k]-48;
    }

    bool tidy=true;
    for (int k=0;k<dits-1;k++)
        if (nrs[k]>nrs[k+1])
            tidy=false;
    return tidy;
}

int main()
{
    ifstream inFile;
    ofstream outFile;
    inFile.open("B-small-attempt0.in");
    outFile.open("out.dat");

    int T;
    inFile>>T;

    for (int mainLoop=0;mainLoop<T;mainLoop++)
    {
        int N;
        int soln;
        inFile>>N;
        bool tidyFound=false;
        while (!tidyFound)
        {
            if (isTidy(N))
            {
                tidyFound=true;
                soln=N;
            }
            else
                N--;
        }

        outFile<<"Case #"<<mainLoop+1<<": "<<soln<<endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}
