#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    string N;
    for(int i = 1; i <= T; ++i){
        cin >> N;
        int tmp = 0;
        bool qq = false;
        for(int j = 0; j < N.size() - 1; ++j){
            if(N[j] < N[j + 1] && !qq) tmp = j + 1;
            if(N[j] > N[j + 1]) qq = true;
        } 
        cout << "Case #" << i << ": ";
        if(qq){
            for(int j = 0; j < tmp; ++j) cout << N[j];
            N[tmp]--;
            if(N[tmp] != '0') cout << N[tmp];
            for(int j = tmp + 1; j < N.size(); ++j) cout << 9;
            cout << endl;
        } else {
            cout << N << endl;
        }
    }
}
