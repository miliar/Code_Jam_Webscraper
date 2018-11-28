#include <string>
#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A.out");
    
    int Case;
    fin >> Case;
    for(int c = 0; c < Case; ++c)
    {
        int width;
        string str;
        fin >> str >> width;
        
        int count = 0;

        for(int i = 0; i <= str.length() - width; ++i)
            if(str.at(i) == '-')
            {
                for(int j = 0; j < width; ++j)
                    str.at(i + j) = (str.at(i + j) == '+' ? '-' : '+');
                ++count;
            }
        
        bool solved = true;
        for(int i = str.length() - width; i < str.length(); ++i)
            if(str.at(i) == '-')
            {
                solved = false;
                break;
            }

        fout << "Case #" << c + 1 << ": ";
        if(solved)
            fout << count << endl;
        else
            fout << "IMPOSSIBLE" << endl;
    }
    
    return 0;
}
