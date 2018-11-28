#include <iostream>
#include <string>

int main()
{
    int T, K;
    std::string pancakes;

    std::cin >> T;
    for(int i = 0; i < T; i ++)
    {
        std::cin >> pancakes >> K;
        int flipper = 0, count = 0;
        while(flipper <= pancakes.length() - K)
        {
            if(pancakes[flipper] == '-')
            {
                count ++;
                for(int j = flipper; j-flipper < K; j ++)
                {
                    pancakes[j] = (pancakes[j]-44)*(-1)+44;
                }
                flipper ++;
            }else
            {
                flipper ++;
            }
        }

        while(flipper < pancakes.length())
        {
            if(pancakes[flipper] == '-')
            {
                std::cout << "Case #" << i+1 << ": IMPOSSIBLE" << std::endl;
                break;
            }
            flipper ++;
        }
        if(flipper == pancakes.length())
        std::cout << "Case #" << i+1 << ": " << count << std::endl;
    }

    return 0;
}
