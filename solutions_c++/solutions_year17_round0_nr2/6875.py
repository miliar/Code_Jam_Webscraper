#include <iostream>

using namespace std;

int main()
{
    int cases;
    cin >> cases;
    for(int x = 1; x <= cases; ++x)
    {
        bool keep_going = true;
        string number;
        cin >> number;
        while(keep_going)
        {
            int changeSpot = -1;
            for(int j = 0; j < number.size(); ++j)
            {
                for(int i = number.size() - 1; i > 0; --i)
                {
                    if(number[i] < number[i - 1])
                    {
                        changeSpot = i - 1;
                    }
                }
            }
            if(changeSpot != -1)
            {
                number[changeSpot]--;
                for(int i = changeSpot + 1; i < number.size(); ++i)
                {
                    number[i] = '9';
                }
            }
            else
            {
                keep_going = false;
            }
        }  
        int begin_zero = -1;
        for(int i = 0; i < number.size(); ++i)
        {
            if((begin_zero != -1 || i == 0) && number[i] == '0')
            {
                begin_zero = i;
            }
        }
        if(begin_zero == -1)
        {
            cout << "Case #" << x << ": " << number << "\n";
        }
        else
        {
            cout << "Case #" << x << ": " << number.substr(begin_zero + 1, number.size() - begin_zero - 1) << "\n";
        }
    }
    return 0;
}