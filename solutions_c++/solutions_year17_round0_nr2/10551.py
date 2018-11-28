#include <iostream>
#include<fstream>
using namespace std;


int main()
{
    ifstream infile;
    infile.open("B-small-attempt3.in");
    ofstream ofile;
    ofile.open("output3.op");
    int T,N;
    int tidy=0;
    infile>>T;
    for(int i=0;i<T;i++)
    {
        infile>>N;
        for(int i=1;i<=N;i++)
        {
            if(i%10!=0)
            {
                if((i%10)>=(i%100)/10 )
                {
                    if((i%100)/10 >= i/100)
                    {

                        tidy=i;
                    }

                }
            }
        }
    ofile<<"Case #"<<i+1<<": ";
    ofile<<tidy<<"\n";
    }
    infile.close();
    ofile.close();
}
