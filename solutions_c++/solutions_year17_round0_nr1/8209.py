#include <iostream>
#include <string>

void flip(char &c)
{
    if (c=='+') c='-';
    else c='+';
}

int main()
{
    int T;
    std::cin >> T;
    for (int t=1; t<=T; t++)
    {
        std::string S; int K;
        std::cin >> S >> K;
        int L = S.size();

        int s=0, count=0;
        while(true)
        {
            while(s<L && S[s]=='+') s++;
            if(s>=L) break;
            if(L-s<K) {count=-1; break;}
            int k=0;
            while(k<K && S[s+k]!='+') k++;
            if (k<K)
            {
                for (int i=k; i<K; i++) flip(S[s+i]);
            }
            s+=k;
            count++;
        }

        if (count>=0)
            std::cout << "Case #" << t << ": " << count << std::endl;
        else
            std::cout << "Case #" << t << ": " << "IMPOSSIBLE" << std::endl;
    }
    return 0;
}
