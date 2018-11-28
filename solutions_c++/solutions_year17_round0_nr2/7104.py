#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %d\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    string s;
    for(int t=1;t<=T;t++)
    {
        DI(t)
//----  wczytaj();
        cin >> s;
        int start = 0;
        for(int i = 0 ; i < s.size() - 1; ++i)
        {
            if(s[i] < s[i+1])
            {
                start = i+1;
                continue;
            }
            else if(s[i] == s[i+1])
            {
                continue;
            }
            if(s[i + 1] == '0')
            {
                if(start == 0 && s[0] == '1')
                {
                    s = s.substr(0, s.size() - 1);
                    for(auto& a : s)
                        a='9';
                    break;
                }
                else
                {
//9 od start
                    s[start]--;
                    for(int j = start+1; j<s.size() ;++j)
                        s[j] = '9';
                    break;
                }
            }
            else
            {
//9 od start
                s[start]--;
                for(int j = start+1; j<s.size() ;++j)
                    s[j] = '9';
                break;
            }

        }


        printf("Case #%d: ",t);
//----  wykonaj();

        cout << s << endl;
        //printf("%s\n", s);
    }
    return 0;
}
