#include <iostream>
#include<fstream>
#include <sstream>
#include <iomanip>
#include <string>
#include <algorithm>

using namespace std;


int main()
{
    int t =0;
    long double n;

    ifstream infile("in/B-large.in");
    ofstream ofile("out/tidy_nums.out");



    infile >> t;

    for (int i =1 ; i<= t ; i++)
    {


        infile >> n;
        stringstream stream;
        stream << fixed << setprecision(0) << n;
        string a = stream.str();


        int size = a.length();

        for ( int k = size -1; k > 0; k--)
        {
            if ( a.at(k) < a.at(k-1) )
            {
                a[k-1] = a.at(k-1) -1;
                for ( int l = k ; l < size ;l++ ) {
                    a[l] ='9';
                }
            }
        }
        a.erase(0, min(a.find_first_not_of('0'), a.size()-1));
        ofile << "Case #"<<i<<": "<<a <<endl;

    }
    return 0;

}

