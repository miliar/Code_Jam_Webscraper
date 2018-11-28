#include<iostream>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        cout << "Case #" << i+1 << ": ";
        int N, K;
        cin >> N >> K;
        int place_left, place_right;
        vector<bool> stalls(N, false);
        while(K > 0)
        {
            place_left = 0;
            place_right = 0;
            int cur_st;
            for(int i = 0; i < N; i++)
            {
                int temp_left = 0, temp_right = 0;
                if(stalls[i])
                    continue;
                int cur = i - 1;
                while(cur >= 0 && not(stalls[cur]))
                {
                    temp_left++;
                    cur--;
                }
                cur = i + 1;
                while(cur < N && not(stalls[cur]))
                {
                    temp_right++;
                    cur++;
                }
                if((min(temp_left, temp_right) > min(place_left, place_right))||((min(temp_left, temp_right) == min(place_left, place_right))&&(max(temp_left, temp_right) > max(place_left, place_right))))
                {
                    place_left = temp_left;
                    place_right = temp_right;
                    cur_st = i;
                }
            }
            stalls[cur_st] = true;
            K--;
        }
        cout << max(place_left, place_right) << " " << min(place_left, place_right) << endl;
    }
}
