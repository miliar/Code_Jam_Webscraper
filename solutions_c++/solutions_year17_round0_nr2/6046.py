#include <string>
#include <fstream>
#include <iostream>
using namespace std;

bool check(string str)
{
    for(int i = 0; i < str.length() - 1; ++i)
        if(str.at(i) > str.at(i + 1))
            return false;
    return true;
}

void remove_zero(string &str)
{
  while(str.at(0) == '0' && str.length() > 1)
    str = str.substr(1, str.length() - 1);
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B.out");
    
    int Case;
    fin >> Case;
    for(int c = 0; c < Case; ++c)
    {
        string str;
        fin >> str;
        
        int last = str.length() - 1;
        while(!check(str))
        {
            str.at(last) = '9';
            str.at(last - 1) -= 1;
            
            for(int i = last - 1; i > 0; --i)
                if(str.at(i) < '0')
                {
                    str.at(i - 1) -= 1;
                    str.at(i) = '9';
                }
                
            --last;
        }
        
        remove_zero(str);
        
        fout << "Case #" << c + 1 << ": " << str << endl;
    }
    
    return 0;
}
