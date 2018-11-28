#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        string s;
        cin >> s;
        int k;
        cin >> k;

        bool found = true;
        int flips = 0;

        for(int j = 0; j<s.length(); ++j)
        {
            if(s[j] == '+')
                continue;
            else
            {
                if(j+k > s.length())
                {
                    found= false;
                    break;
                }
                //flip(s, j , k);
                flips +=1;
                for(int idx = j; idx < j+k ; ++idx)
                {
                    if(s[idx] == '+')
                        s[idx] = '-';
                    else
                        s[idx] = '+';
                }
            }
        }

        if(found)
            cout<<"Case #"<<i<<": "<<flips<<endl;
        else
            cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;

    }
    return 0;
}
