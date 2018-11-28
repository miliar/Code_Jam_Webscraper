#include <string>
#include <queue>
#include <iostream>
#include <fstream>
#include <map>

using namespace std;

typedef unsigned long long UINT64;


int main()
{
    ifstream fin("C:\\Compete\\FB2016\\C-large.in");

    ofstream fout("C:\\Compete\\FB2016\\output.txt");

    int T;  fin >> T;
    for (int i = 0; i < T; i++)
    {
        unsigned long long N, K;
        fin >> N >> K;

        map<UINT64, UINT64> bucket;
        map<UINT64, UINT64>::iterator iter;
        bucket[N] = 1;

        UINT64 size = 1;

        UINT64 nextkey = N;

        UINT64 small;
        UINT64 large;
        while (true)
        {
            small = nextkey / 2;
            if (nextkey % 2 == 0 && small > 0)
                small = small - 1;
            large = nextkey / 2;

            if (K > size)
            {
                K = K - size;
            }
            else
            {
                break;
            }

            if (bucket.find(small) != bucket.end())
            {
                bucket[small] += size;
            }
            else
            {
                bucket[small] = size;
            }
            if (bucket.find(large) != bucket.end())
            {
                bucket[large] += size;
            }
            else
            {
                bucket[large] = size;
            }
            
            iter = bucket.lower_bound(nextkey);
            iter--;
            nextkey = iter->first;
            size = bucket[nextkey];
        }

        bucket.clear();
        fout << "Case #" << i + 1 << ": " << large << " " << small << endl;
    }
    return 0;
}