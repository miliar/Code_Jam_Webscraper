#include <iostream>
#include <climits>
#include <vector>
using namespace std;

void proceed(int n, int k)
{
    vector<bool> state;
    state.resize(n);

    int min;
    int max;
    for(int i = 0; i < k; ++i)
    {
        min = INT_MIN;
        max = INT_MAX;

        int left = 0;
        int pos = -1;
        for(int j = 0; j < n; ++j)
        {
            if(state[j]) 
            {
                left = 0;
                continue;
            }

            int right = 0;
            for(int k = j + 1; k < n; ++k)
            {
                if(state[k])
                {
                    break;
                }
                right += 1;
            }

            int min_val = ::min(left, right);
            int max_val = ::max(left, right);

            //cout << "j = " << j << endl;
            //cout << "left = " << left << endl;
            //cout << "right = " << right << endl;
            //cout << "min = " << min << endl;
            //cout << "my min = " << min_val << endl;
            if(min < min_val || (min == min_val && max < max_val))
            {
                min = min_val;
                max = max_val;
                pos = j;
                //cout << "position " << pos << endl;
                //cout << "Left = " << left << endl;
                //cout << "right = " << right << endl;
            }

            left += 1;
        }

        state[pos] = true;

        //for(auto b : state)
        //{
        //    cout << (b ? '1' : '0');
        //}
        //cout << endl;
    }
    cout << max << " " << min << endl;
}

int main(int argc, char *argv[])
{
    int t;
    cin >> t;

    for(int i = 0; i < t; ++i)
    {
        int n, k;
        cin >> n >> k;

        cout << "Case #" << i + 1 << ": ";
        proceed(n, k);
    }
}
