#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <ctype.h>

using namespace std;

#define ll long long
#define fo(n) for(int i=0;i<n;i++)
#define pb push_back
#define be v.begin()
#define en v.end()
#define mt make_tuple
#define fot(n,k) for(int k=0;k<n;k++)

int main()
{
    int t;
    cin >> t;
    fo(t)
    {
        string a;
        int val,coun=0;
        cin >> a >> val;
        for(int j=0;j<a.size()-val+1;j++)
        {
            if(a[j]=='+')
            continue;
            else
            {
                coun++;
                for(int k=0;k<val;k++)
                {
                    if(a[j+k]=='+')
                    a[j+k]='-';
                    else
                    a[j+k]='+';
                }
            }
        }
        int pr=0;
        for(int k=0;k<val;k++)
        {
                if(a[a.size()-1-k]=='-')
                    pr=1;
                //else
                  //  a[j+k]='+';
        }
        if(pr==1)
        cout << "Case #"<< i+1 <<": IMPOSSIBLE" << '\n';
        else
        cout << "Case #"<< i+1 << ": "<<coun << '\n';
            
        
    }
    return 0;
}