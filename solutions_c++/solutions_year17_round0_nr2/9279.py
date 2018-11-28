#include <iostream>
#include <string>

using namespace std;

int main()
{
    int N;
    char ans[20];

    cin >> N;

    for(int k = 1; k <= N; k++){
        string str;
        cin >> str;
        ans[str.length() - 1] = str[str.length() - 1];
        for(int i = str.length() - 2; i >= 0 ; i--){
            if(str[i] > str[i + 1]){
                str[i]--;
                for(int j = i + 1; j < str.length(); j++){
                    ans[j] = '9';
                }
            }
            ans[i] = str[i];
        }
        cout << "Case #" << k << ": ";
        for(int i = 0; i < str.length(); i++){
            if(ans[i] != '0' || i == str.length() - 1)
                cout << ans[i];
        }
        cout << endl;
    }

    return 0;
}
