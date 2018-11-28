#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#include <map>

using namespace std;

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for (int i=0;i<T;i++)
    {
        char buf[65536];
        scanf("%s\n", buf);
        string s = buf;
        int len = s.length();
        for (int q=0;q<len;q++)
        {
            for (int j=0;j<len-1;j++)
            {
                if (s[j]>s[j+1])
                {
                    s[j]--;
                    for (int k=j+1;k<len;k++)
                        s[k] = '9';
                }
            }
        }
        int zero = 0;
        for (int j=0;j<len;j++)
            if (s[j]=='0') zero++; else break;
        if (zero==len)
            s = "0";
        else
            s = s.substr(zero, len-zero);

        cout << "Case #" << (i+1) << ": " << s << endl;
    }




 return 0;
}
