#include <iostream>
#include <string>
#include<stack>
using namespace std;

int main()
{
    int T;
    cin >> T;
    int round=1;
    while(T-- > 0)
    {
        string number;
        cin >> number;
        string p = number;
        //cout << number << p;
        bool flag = true;
        int i;
        for(i=1; i<number.length(); i++)
        {
            if(number[i] < number[i-1])
            {
                flag = false;
                break;
            }
        }
        if(flag)
         {
             cout << "Case #" << round << ": " << number << "\n";
         }
        else
        {
            i--;
            number[i] = number[i]-1;
            while(i > 0)
            {
                if(number[i] < number[i-1])
                    number[i-1] = number[i-1] - 1;
                else
                    break;
                i--;
            }
            for(int k=i+1; k<number.length(); k++)
                number[k] = '9';

            cout << "Case #" << round << ": ";
            for(int i=0; i<number.length(); i++)
            {       if(number[i]!='0')
                        cout<<number[i];
            }
            cout<<"\n";
        }

        round++;

    }
}
