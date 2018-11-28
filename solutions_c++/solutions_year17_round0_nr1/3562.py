#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int t = 0; t < T; t++)
    {
        string pancake;
        cin >> pancake;
        int K;
        cin >> K;
        int times = 0;
        for(size_t i = 0; i < pancake.length()-K+1; i++)
        {
            if(pancake[i]=='+')
                continue;
            else
            {
                for(size_t j = i; j < i+K; j++)
                {
                    if(pancake[j] =='-')
                        pancake[j]='+';
                    else
                        pancake[j]='-';
                }
                times++;
            }
        }
        bool succeed = true;        
        for(size_t i = 0; i < pancake.length(); i++)
        {
            if(pancake[i]=='-')
            {
                succeed = false;
                break;
            }
        }
        if(succeed)
            cout << "Case #"<<t+1<<": "<< times <<endl;
        else
            cout << "Case #"<<t+1<<": "<< "IMPOSSIBLE" <<endl;
    }
    return 0;
}
