#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int t;
string n;
bool works(char x, string y)
{
    for (int i=0; i<y.length(); i++)
    {
        if (x<y[i])
            return true;
        if (x>y[i])
            return false;
    }
    return true;
}
int main()
{
    ifstream fin ("Downloads/B-large.in");
    ofstream fout ("tidy.out");
    fin >> t;
    for (int i=1; i<=t; i++)
    {
        fin >> n;
        string s=n;
        bool flag=false;
        for (int j=0; j<n.length(); j++)
        {
            if (flag)
            {
                s[j]='9';
                continue;
            }
            if (works(n[j], n.substr(j, n.length())))
                s[j]=n[j];
            else
            {
                flag=true;
                s[j]=n[j]-1;
            }
        }
        if (s[0]=='0')
            s=s.substr(1, s.length()-1);
        fout << "Case #" << i << ": " << s << endl;
    }
    fin.close();
    fout.close();
}
