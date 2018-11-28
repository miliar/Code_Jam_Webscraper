// Example program
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    unsigned long long k;
    bool is = true;
    int origin;
    int temp = 0;
    unsigned long long j;
    for(int i=0;i<T;i++)
    {
        cin >> k;
        for(j=k;j>0;j--)
        {
            origin = j;
            while(origin/10 != 0)
            {
                int temp = origin%10;
                origin /= 10;
                int temp1 = origin%10;
                if(temp >= temp1)
                    is = true;
                else
                {
                    is = false;
                    break;
                }
            }
            if(is)
                break;
        }
        temp++;
        if(is)
        {
            cout << "Case #" << temp << ": " << j << endl;
        }
    }
    return 0;
}

