#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        string N;
        cin >> N;
        if(N.length()==1)
            cout << "Case #"<<i+1<<": "<<N<<endl;
        else
        {
            for(size_t j = 0; j < N.length()-1; j++)
            {
                if(N[j+1]>=N[j])
                    continue;
                else
                {
                    size_t k = j;
                    bool flag = false;
                    if(k == 0)
                    {
                        if(N[k] != '1')
                        {
                            N[k] -= 1;
                            for(size_t m = k+1; m < N.length(); m++)
                                N[m] = '9';
                        }
                        else
                        {
                            string temp(N.length()-1,'9');
                            N = temp;
                        }
                        break;
                    }
                    while(k!=0)
                    {
                        if(N[k-1]<N[k])
                        {
                            N[k] -= 1;
                            for(size_t m = k+1; m < N.length(); m++)
                                N[m] = '9';
                            flag = true;
                            break;
                        }
                        else
                        {
                            k--;
                        }
                    }
                    if(!flag)
                    {
                        if(N[k] != '1')
                        {
                            N[k] -= 1;
                            for(size_t m = k+1; m < N.length(); m++)
                                N[m] = '9';
                        }
                        else
                        {
                            string temp(N.length()-1,'9');
                            N = temp;
                        }
                    }       
                    break;
                }
            }
            cout << "Case #"<<i+1<<": "<<N<<endl;
        }
    }

    return 0;
}
