#include <iostream>
#include <string>

int main()
{
    int T;
    std::cin >> T;
    for (int t=1; t<=T; t++)
    {
        std::string s;
        std::cin >> s;
        int L = s.size();
        int l=L;
        for (int i=L-1; i>0; i--)
        {
            if (s[i-1]>s[i]) {s[i-1]--; l=i;}
        }
        int st=0;
        if (s[0]=='0') st++;
        std::string so;
        for (int i=st; i<l; i++) so.push_back(s[i]);
        for (int i=l; i<L; i++) so.push_back('9');

        std::cout << "Case #" << t << ": " << so << std::endl;
    }
    return 0;
}
