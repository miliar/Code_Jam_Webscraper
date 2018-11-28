#include<iostream>

using namespace std;

int main()
{
    int T;
    string N;
    cin >> T;
    for(int i = 1; i <= T; ++i)
    {
        int last_modified;
        cin >> N;
        last_modified = N.size();
        if(N.size() == 1) cout << "Case #" << i << ": " << N << endl;
        else
        {
            int idx = 0;
            for(int j = N.size() - 2; j >= 0; --j)
            {
                if(N[j] > N[j + 1])
                {
                    N[j]--;
                    last_modified = j;
                }
            }
            if(last_modified != N.size()) for(int j = last_modified + 1; j < N.size(); ++j) N[j] = '9';
            while(N[idx] == '0') idx++;
            cout << "Case #" << i << ": ";
            for(int j = idx; j < N.size(); ++j) cout << N[j];
            cout << endl;
        }
    }
    return 0;
}
