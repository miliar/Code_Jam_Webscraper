#include <iostream>
#include <fstream>
#include <string>
using namespace std;
string s;
int k;
int t;
int cnt;
int main()
{
    ifstream fin ("Downloads/A-large.in");
    ofstream fout ("pancake.out");
    fin >> t;
    for (int i=1; i<=t; i++)
    {
        cnt=0;
        fin >> s >> k;
        for (int j=0; j<=s.length()-k; j++)
        {
            if (s[j]=='-')
            {
                cnt++;
                for (int l=j; l<j+k; l++)
                {
                    if (s[l]=='-')
                        s[l]='+';
                    else
                        s[l]='-';
                }
            }
        }
        bool flag=false;
        for (int j=s.length()-k+1; j<s.length(); j++)
        {
            if (s[j]=='-')
            {
                flag=true;
                break;
            }
        }
        fout << "Case #" << i << ": ";
        if (!flag)
        {
            fout << cnt << endl;
        }
        else fout << "IMPOSSIBLE" << endl;
    }
    fin.close();
    fout.close();
}
