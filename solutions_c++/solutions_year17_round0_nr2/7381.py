#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    string s, y;
    fstream fin;
    fin.open("B-large.in", fstream::in);

    fstream fout;
    fout.open("output.out", fstream::out);

    int N, i, j;
    if(fin.is_open() && fout.is_open())
    {
        int it = 0;
        getline(fin, s);
        while (getline(fin, s))
        {
            it++;
            fout << "Case #" << it << ": ";
            for(i=0; i < s.size()-1 && s[i] <= s[i+1]; i++);
            if(i<s.size()-1)
            {
                for(j=i+1; j<s.size(); j++)
                {
                    s[j]='9';
                }
                s[i]--;
                while(i>0 && s[i]<s[i-1])
                {
                    s[i]='9';
                    s[i-1]--;
                    i--;
                }
                if(i==0 && s[0]=='0')
                {
                    s.erase(s.size()-1);
                    s[0]='9';
                }
            }
            fout << s << endl;
        }
    }
}
