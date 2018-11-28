#include <iostream>
//#include <math.h>
//#include <stdlib.h>
//#include <iomanip>
//#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int A[n];
    for(int i=0;i<n;i++)
    {
        string t;
        cin >> t;
        int k;
        cin >> k;
        int c=0;
        int ans=0;
        while(t[c]!='\0')
        {
            if(t[c]!='+')
            {
                for(int j=c;j<k+c;j++)
                {
                    if(t[j]=='\0')
                    {
                        ans = -2;
                        break;
                    }
                    if(t[j]=='+')
                        t[j]='-';
                    else
                        t[j]='+';
                }
                ans++;
            }
            c++;
        }
        cout << "Case #" << i+1 << ": ";
        if(ans!=-1)
            cout << ans;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }
    return 0;
}
