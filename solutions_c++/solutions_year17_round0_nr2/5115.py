#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>

using namespace std;

int main()
{

    int nn;
    cin >> nn;
    for(int kk=1; kk<=nn; kk++)
    {

        string s;
        cin >> s;
        const unsigned n = s.size();

        int x = -1;
        for(int i=1; i<n; i++)
        {
            if(s[i] < s[i-1])
            {
                x = i-1;
                break;
            }
        }

        if(x >= 0)
        {
            if(x-1 >= 0)
            {
                int val = s[x];
                do{ x--; }
                while(x >= 0 && s[x] == val);
                x++;
            }
            
            s[x]--;
            x++;
            for(; x<n; x++) s[x] = '9';
        }

        cout << "Case #" << kk << ": ";
        int i;
        for(i=0; i<n && s[i] == '0'; i++);
        for(; i<n; i++)
        {
            cout << s[i];
        }
        cout << endl;
        
    }

}
