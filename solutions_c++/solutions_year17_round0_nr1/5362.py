#include <bits/stdc++.h>

using namespace std;


void flipArray(bool check[], int j, int k){
    for(int i = j; i < j+k; i++){
        check[i] = !check[i];
    }
}

int main()
{
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);

    int T;
    string s;
    int k;
    bool check[1000] = {true};

    cin >> T;

    for(int i = 0; i < T; i++){
        cin >> s >> k;
        int sum = 0;

        for(int j = 0; j < s.length(); j++){
            if(s[j] == '+'){
                check[j] = true;
            } else {
                check[j] = false;
            }
        }

        for(int j = 0; j < s.length() - k + 1; j++){
            if(check[j] == true){
                continue;
            } else {
                flipArray(check,j,k);
                sum++;
            }
        }
        bool isAllHappy = true;



        for(int j = s.length() - k + 1; j < s.length(); j++){
            isAllHappy = isAllHappy && check[j];
        }

        if(isAllHappy){
            cout << "Case #" << i+1 << ": " << sum << endl;
        } else {
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        }
    }

    return 0;
}
