#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main()
{
    int i, k;
    string s;
    fstream fin;
    fin.open("A-large.in", fstream::in);

    fstream fout;
    fout.open("output.out", fstream::out);

    if(fin.is_open() && fout.is_open())
    {
        getline(fin, s);
        int it = 0;
        while (getline(fin, s))
        {
            it++;
            fout << "Case #" << it << ": ";
            for(i=0; s[i]!=' '; i++);
            stringstream convert(s.substr(i+1));
            convert >> k;
            s.erase(i);


            int y=0;
            i=0;
            while(i < s.size())
            {
                if(s[i]=='-')
                {
                    if(i+k <= s.size())
                    {
                        for(int j=i; j<i+k; j++)
                        {
                            if(s[j]=='+') s[j]='-';
                            else s[j]='+';
                        }
                        y++;
                    }
                    else
                    {
                        fout << "IMPOSSIBLE" << endl;
                        break;
                    }
                }
                i++;
            }
            if(i==s.size())
            {
                fout << y << endl;
            }
            s.clear();
        }
    }
    else cout << "unable to open file" << endl;
}
