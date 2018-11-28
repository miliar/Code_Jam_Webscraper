#include <fstream>
#include <deque>
#include <map>

using namespace std;

int main()
{
    ifstream ifs("C-large.in");
    ofstream ofs("C-large.out");

    int T;
    ifs >> T;

    for(int i=0; i<T; i++)
    {
        unsigned long long N, K;
        ifs >> N >> K;

        deque<pair<unsigned long long, unsigned long long>> stalls;
        stalls.push_front({N, 1});
        while(true)
        {
            auto back = stalls[stalls.size()-1];
            if(K <= back.second) break;

            K -= back.second;
            auto& front = stalls[0];
            if(back.first%2 == 0)
            {
                if(back.first/2 == front.first)
                {
                    front.second += back.second;
                    stalls.push_front({back.first/2-1, back.second});
                }
                else
                {
                    stalls.push_front({back.first/2, back.second});
                    stalls.push_front({back.first/2-1, back.second});
                }
            }
            else
            {
                if(back.first/2 == front.first)
                {
                    front.second += back.second*2;
                }
                else
                {
                    stalls.push_front({back.first/2, back.second*2});
                }
            }
            stalls.pop_back();
        }

        auto back = stalls[stalls.size()-1];
        unsigned long long min = (back.first-1)/2;
        unsigned long long max = back.first/2;

        ofs << "Case #" << i+1 << ": " << max << " " << min << endl;

    }
}
