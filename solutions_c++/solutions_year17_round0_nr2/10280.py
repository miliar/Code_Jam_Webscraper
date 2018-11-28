#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
    ifstream input("A-small-practice.in", ios::in);
    ofstream output("test.txt", ios::out | ios::trunc);
     if(input&&output)
     {
        int t; input >> t;
    for(int i=1;i<=t;i++)
    {
        bool trouve=false;
        int n; input >> n;

        while(n>9&&!trouve)
        {
            vector<int> tab;
            int n1=n;
            while(n1>0)
            {
                tab.push_back(n1%10);
                n1/=10;
            }

            int j=0;
            bool found=false;
            while(j<tab.size()-1&&!found)
            {
                if(tab[j]>=tab[j+1])
                    j++;
                else
                    found=true;
            }
            if(!found)
                trouve=true;
            else
                n--;
        }
        output << "Case #" << i << ": " << (n) << '\n';

     }

     }

    return 0;
}
