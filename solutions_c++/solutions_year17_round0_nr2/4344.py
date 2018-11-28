#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output.out");

    //-- check if the files were opened successfully
    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int numCase;
    fin >> numCase;
    int i,d;
    string n;
    for (i = 0; i < numCase; i++)
    {
        fin >> n;

        if(n.size()==1){fout << "Case #" << (i + 1) << ": " << n << endl;}
        else{bool a = false;
            for(auto j=n.rbegin();j != n.rend()-1;++j){
            if(*j < *(j+1)){(*(j+1))--;for(auto k = n.rbegin();k != j+1;++k)*k='9';}
        for(auto j=n.begin();j != n.end();++j){if(*j=='0')n.erase(j);else{break;}}
            }
        fout << "Case #" << (i + 1) << ": " << n << endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}
