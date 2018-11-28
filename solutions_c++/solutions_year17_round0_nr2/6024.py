#include <iostream>
#include <string>

int main()
{
    int T;
    std::string digits;

    std::cin >> T;
    for(int i = 0; i < T; i ++)
    {
        std::cin >> digits;
        int idx = 1, down = -1;//, eql = -1;
        while(idx < digits.length())
        {
            if(digits[idx] < digits[idx-1])
            {
                down = idx-1;
                break;
            }
            /*else if(digits[idx] > digits[idx-1])
            {
                eql = -1;
            }else if(digits[idx] == digits[idx-1])
            {
                eql = idx-1;
            }*/

            idx ++;
        }

        if(down >= 0)
        {
            idx = digits.length();
            while(idx > down)
            {
                digits[idx] = '9';
                idx --;
            }

            while(digits[idx] == digits[idx-1])
            {
                digits[idx] = '9';
                idx --;
            }
        }
        digits[idx] --;

        int count = 0;
        for(int j = 0; j < digits.length(); j ++)
        {
            if(digits[j] == '0')
            {
                count ++;
            }else
            {
                break;
            }
        }

        digits.erase(0, count);

        std::cout << "Case #" << i+1 << ": " << digits << std::endl;
    }

    return 0;
}
