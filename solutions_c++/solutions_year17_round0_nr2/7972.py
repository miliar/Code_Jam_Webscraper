#include <iostream>
#include <string>
#include <fstream>

using namespace std;

typedef long long ll;

int main()
{
    ofstream fout("out.out");
    int n;
    string str;
    cin >> n;
    for(int i = 1; i <= n; i++)
    {
        cin >> str;
        
        if(str.size() == 1)
        {
            fout << "Case #" << i << ": " << str << endl;
            continue;
        }
        
        char c1, c2;
        for(int j = str.size() - 1; j > 0; j--)
        {
            c1 = str.at(j);
            c2 = str.at(j - 1);
            
            if(c2 > c1)
            {
                for(int k = j; k < str.size(); k++)
                    str.at(k) = '9';
                str.at(j - 1)--;
            }
        }
        if(str.at(0) == '0')
            str = str.substr(1, str.size());
        
        fout << "Case #" << i << ": " << str << endl;
    }
}
