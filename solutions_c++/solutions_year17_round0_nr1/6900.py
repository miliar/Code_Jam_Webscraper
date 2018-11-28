#include <iostream>

using namespace std;

int main()
{
    int cases;
    cin >> cases;
    for(int i = 1; i <= cases; ++i)
    {
        string pancakes;
        int spatula, startPos = 0, count = 0;
        cin >> pancakes >> spatula;
        
        while(startPos < pancakes.size())
        {
            while(pancakes[startPos] != '-' && startPos < pancakes.size())
            {
                startPos++;
            }
            if(startPos == pancakes.size())
            {
                cout << "Case #" << i << ": " << count << "\n";
                break;
            }
            else if(startPos > pancakes.size() - spatula)
            {
                cout << "Case #" << i << ": IMPOSSIBLE\n";
                break;
            }
            count++;
            int new_start = 0;
            for(int i = 0; i < spatula; ++i)
            {
                if(pancakes[startPos + i] == '-')
                {
                    pancakes[startPos + i] = '+';
                }
                else
                {
                    pancakes[startPos + i] = '-';
                    if(!new_start)
                    {
                        new_start = startPos + i;
                    }
                }
            }
            if(new_start)
            {
                startPos = new_start;
            }
        }
    }
    return 0;
}