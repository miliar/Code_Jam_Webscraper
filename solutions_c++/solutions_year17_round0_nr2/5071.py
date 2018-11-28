#include<iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;

    string N;
    for (int t = 1; t <= T; ++t)
    {
        cin >> N;
        if(N.length() == 1)
        {
            cout <<"Case #"<<t<<": "<<N<< endl;
        }
        else
        {
            for(int i=0; i< N.length()-1; ++i)
            {
                if(N[i]<= N[i+1])
                    continue;
                else
                {
                    N[i] = N[i] -1;
                    for(int j=i+1; j< N.length();++j)
                        N[j] = '9';

                    for(int j=i; j>0;--j)
                    {
                        if(N[j] < N[j-1])
                        {
                            N[j] = '9';
                            N[j-1] -=1;
                        }
                    }
                    while(N[0] == '0')
                        N = N.substr(1);
                    break;
                }
            }

            cout <<"Case #"<<t<<": "<<N<< endl;

        }
    }
    return 0;
}
