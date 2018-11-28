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
        int K;
        scanf("%s %d\n", buf, &K);
        string s = buf;
        int len = s.length();
        int ans = 0;
        for (int j=0;j<=len-K;j++)
        {
           // cout << j << " : " << s << endl;
            if (s[j]=='-')
            {
                ans++;
                for (int z=0;z<K;z++)
                {
                    if (s[j+z]=='-') s[j+z] = '+'; else s[j+z] = '-';
                }
            }
        }
        bool bok = true;
        for (int z=0;z<K;z++)
        {
            if (s[len-z-1]=='-')
            {
                bok = false;
                break;
            }
        }
        cout << "Case #" << (i+1) << ": ";
        if (bok) cout << ans; else cout << "IMPOSSIBLE";
        cout << endl;
    }




 return 0;
}
