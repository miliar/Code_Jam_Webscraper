#include <iostream>
//#include <math.h>
//#include <stdlib.h>
//#include <iomanip>
#include <queue>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        string t;
        cin >> t;
        for(int j=0;j<t.length();j++)
        {
            int c = t.length()-j-1;
            while(c>=1)
            {
                if((int)t[c]<(int)t[c-1])
                {
                    for(int k=c;k<t.length();k++)
                        t[k] = '9';
                    t[c-1]=(int)t[c-1]-1;
                }
                c--;
            }
        }
        while(t[0]=='0')
        {
            t = t.substr(1,t.length());
        }
       //Answer
        cout << "Case #" << i+1 << ": ";
        cout << t << endl;
    }
    return 0;
}
