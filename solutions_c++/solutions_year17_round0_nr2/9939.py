#include <iostream>
#include <string>
using namespace std;

int main()
{
    int tests;
    long long number;
    string nStr;
    
    cin >> tests;
    
    for (int t=1; t<=tests; t++)
    {
        cin >> number;
        long long n = number;
        
        while (1)
        {
            bool isTidy = true;
    
            nStr = to_string(n);
            
            for (int i=1; i<nStr.size(); i++)
            {
                if ((nStr.at(i) - '0') < (nStr.at(i-1) - '0'))
                {
                    if ((nStr.at(i-1) - '0') == 0)
                    {
                        nStr.at(i-1) = (char)(48);
                    }
                    else
                    {
                        nStr.at(i-1) = (char)((nStr.at(i-1) - '0') - 1 + 48);
                    }
                    for (int j=i; j<nStr.size(); j++)
                    {
                        nStr.at(j) = (char)(57);
                    }
                    n = stoll(nStr);
                    //cout << n << endl;
                    isTidy = false;
                    break;
                }
            }
            
            if (isTidy)
            {
                break;
            }
            //cout << nStr << " size: " << nStr.size() << " -" << nStr.at(0) << endl;
            //cout << "N: " << n << endl;
        }
        cout << "Case #" << t << ": " << n << endl;;
    }
    return 0;
}
