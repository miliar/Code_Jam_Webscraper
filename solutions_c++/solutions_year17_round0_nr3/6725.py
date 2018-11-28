#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>


using namespace std;
ifstream myfile;
ofstream myfile2;
using namespace std;





int main()
{
    int NumberOfCases=0;
    int NumberOfStalls=0;
    int NumberOfPeople=0;
    int maximum=0;
    int minimum=0;
    int counter=0;
    int firstMin=0;
    int interval=0;
    int Largest=0;
    int BestLowerBound=0;
    int LowerBound=0;
    string stalls="";

    myfile.open ("C-small-1-attempt3.in");
    myfile2.open ("example.out");

    myfile>>NumberOfCases;
    for (int i=0; i<NumberOfCases; i++)
    {
        myfile>>NumberOfStalls;
        myfile>>NumberOfPeople;
        counter=0;
        stalls="";
        Largest=0;
        BestLowerBound=0;
        LowerBound=0;
        counter=0;
        for (int t=0; t<NumberOfStalls; t++)
        {
            if (t==0)
            {
                stalls+="o";
            }
            stalls+=".";
            if (t==NumberOfStalls-1)
            {
                stalls+="o";
            }
        }
        for (int t=0; t<NumberOfPeople; t++ )
        {
            BestLowerBound=0;
            Largest=0;
            counter=0;
            if (t==0)
            {
                 maximum=ceil((NumberOfStalls-1)/2.0);
                 minimum=floor((NumberOfStalls-1)/2.0);
                // cout<<minimum<<endl;
                 stalls[minimum+1]='o';
            }
            else
            {
                for (int q=0; q<NumberOfStalls+2; q++)
                {
                    if (stalls[q]=='o' && counter==0)
                    {
                        counter=1;
                        LowerBound=q;
                    }
                    else if (stalls[q]=='o')
                    {
                        //counter=0;
                        interval=q-LowerBound;
                        if (interval>Largest)
                        {
                            Largest=interval;
                            BestLowerBound=LowerBound;
                        }
                        LowerBound=q;
                    }
                }
                maximum=ceil((Largest-2)/2.0);
                 minimum=floor((Largest-2)/2.0);
                if (minimum<0)
                {
                    minimum=0;
                }
                if (maximum<0)
                {
                    maximum=0;
                }
                stalls[BestLowerBound+minimum+1]='o';

            }


        }
        /*for (int q=0; q<NumberOfStalls+2; q++)
        {
            cout<<stalls[q];
        }*/
    myfile2<<endl<<"Case #"<<i+1<<": "<<maximum<<" "<<minimum<<endl;
    }


    return 0;
}
