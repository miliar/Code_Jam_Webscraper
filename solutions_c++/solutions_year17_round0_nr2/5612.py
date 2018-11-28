#include <iostream>
#include <string>
#include <cmath>

using namespace std;

typedef long long int lli;

lli cStoll(string val)
{
    lli res = 0;
    int size = val.size();
    for(int i = 0; i < size; i++)
    {
        res += ((val[i] - 48) * pow(10, size - (i + 1)));  
    }
    return res;
}
int main()
{
    int t = 0;
    cin >> t;
    for(int k = 1; k < (t + 1); k++)
    {
        string val;
        cin >> val;
        string res = val;
        int size = val.size();
        if(size > 1)
        {
            for(int i = 0; i < (size - 1); i++)
            {
                if(val[i] > val[i + 1])
                {
                    if(val[i] == '1')
                    {
                        res = "";
                        for(int j = 0; j < (size - 1); j++)
                        {
                            res += '9';     
                        }
                    }
                    else
                    {
                        while(i > 0)
                        {
                            if(val[i] == val[i - 1])
                                i--;
                            else
                                break;
                        }
                        res[i] = res[i] - 1;
                        for(int j = (i + 1); j < size; j++)
                        {
                            res[j] = '9'; 
                        }
                    }
                    break;
                }
            }
        }
        cout << "Case #" << k << ": " << res << endl; 
        //cout << "Case #" << k << ": " << cStoll(res) << endl; 
    }
    return 0;
}
