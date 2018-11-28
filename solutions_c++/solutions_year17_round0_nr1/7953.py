//Christopher Navarro
//April 8, 2017
//Google Code Jam

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

typedef long long ll;

int main()
{
    ofstream fout("out.out");
    int n, k, count;
    string str;
    cin >> n;
    for(int i = 1; i <= n; i++)
    {
        cin >> str;
        cin >> k;
        count = 0;
        
        char c;
        int j;
        for(j = 0; j < str.size() - k + 1; j++)
        {
            c = str.at(j);
            if(c == '+')
                continue;
            
            count++;
            
            for(int l = j; l < j + k; l++)
            {
                if(str.at(l) == '+') str.at(l) = '-';
                else                 str.at(l) = '+';
            }
        }
        //cout << str << endl;
        
        bool bad = false;
        for(int l = j; l < j + k - 1; l++)
        {
            if(str.at(l) == '-')
                bad = true;
        }
        if(bad) fout << "Case #" << i << ": IMPOSSIBLE" << endl;
        else    fout << "Case #" << i << ": " << count << endl;
    }
}
