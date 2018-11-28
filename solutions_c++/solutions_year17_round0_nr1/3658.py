#include<iostream>

using namespace std;

int main()
{
    int T, K;
    string S;
    cin >> T;
    for(int i = 0; i < T; ++i)
    {
        int idx = 0;
        int ans = 0;
        bool impossible = false;
        cin >> S >> K;
        while(idx <= S.size() - K)
        {
            if(S[idx] == '-')
            {
                for(int j = 0; j < K; ++j) S[idx + j] = (S[idx + j] == '-') ? '+' : '-';
                ans++;
            }
            idx++;
        }
        for(int j = 0; j < K; ++j)
        {
            if(S[idx + j] == '-')
            {
                impossible = true;
                break;
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if(impossible) cout << "IMPOSSIBLE";
        else cout << ans;
        cout << endl;
    }
    return 0;
}
