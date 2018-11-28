#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main()
{

    int nn;
    cin >> nn;
    for(int kk=1; kk<=nn; kk++)
    {
        int N, K;
        cin >> N >> K;
        K--;

        map<int, int, greater<int>> H;
        H[N] = 1;

        map<int, int>::iterator it = H.begin();
        while(K > 0)
        {
            int len = it->first;
            int n = it->second;
            if(n <= K)
            {
                H.erase(it);

                auto it1 = H.find((len-1)/2);
                if( it1 != H.end())
                {
                    it1->second += n;
                }
                else
                {
                    H[(len-1)/2] = n;
                }

                it1 = H.find(len-1-(len-1)/2);
                if( it1  != H.end())
                {
                    it1->second += n;
                }
                else
                {
                    H[len-1-(len-1)/2] = n;
                }
                
                K -= n;
            }
            else
            {
                K = 0;
            }

            it = H.begin();
        }

        int len = it->first;
        cout << "Case #" << kk << ": " << len-1-(len-1)/2 << " " << (len-1)/2 << endl;
    }
    
}
