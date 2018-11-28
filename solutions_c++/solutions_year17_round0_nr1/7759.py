#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int t,i,ans,k,size,c;
    string inp;
    cin >> t;
    c = 1;
    while (t--)
    {
        ans = 0;
        cin >> inp >> k;
        size = inp.size();
        vector<bool> check(size,false);
        for(i=0;i<size-k+1;i++)
        {
            if(inp[i] == '-' && check[i] == false)
            {
                for(int z = i; z < i+k; z++)
                    if(inp[z] == '+')       inp[z] = '-';
                    else                    inp[z] = '+';
                check[i] = true;
                ans ++;
            }
        }
        if(inp.find('-') != string::npos)
            cout << "Case #" << c << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << c <<": "<< ans << endl;
        c++;
    }
    return 0;
}
