#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int T,i;
    long long N,j,k;

    cin >> T;
    for(i=0;i<T;i++)
    {
        cin >> N;
        int count = 0;

        while(count!=1 && N>0)
        {   
            vector<int> vec;

            for(k=N;k>0;k=k/10)
            {
                vec.push_back(k%10);
            }
            if(vec.size()==1)
            {
                cout <<"Case #" << i+1 <<": " << N << endl;
                count = 1;
                break;

            }
            for(k=0;k<vec.size()-1;k++)
            {
                if(vec[k]<vec[k+1])
                    break;
                else
                    if(k==vec.size()-2)
                        {
                            cout <<"Case #" << i+1 <<": " << N << endl;
                            count = 1;
                        }

            }
            N--;
        }
    }
    return 0;
}

