    #include <bits/stdc++.h>

using namespace std;

int main(){
    long long i,j,k,l,m,n,test,t;
    string s;
    cin >> test;
    for (t = 0; t < test; t++){
        cin >> n;
        cout << "Case #" << t + 1 << ": ";
        cout.flush();
        vector <int> digits;
        int d = 0;
        while (n > 0){
            digits.push_back(n % 10);
            n /= 10;
            d++;
        }
        reverse(digits.begin(), digits.end());
        int last_inc = -1;
        for (i = 1; i < d; i++){
            if (digits[i] < digits[i - 1]){
                break;
            } else
            if (digits[i] > digits[i - 1]){
                last_inc = i;
            }
        }

        if (i == d){
            for (i = 0; i < d; i++){
                cout << digits[i];
            }
            cout << endl;
        } else
        {
            if (last_inc > 0){
                for (i = 0; i < last_inc; i++){
                    cout << digits[i];
                }
                cout << digits[last_inc] - 1;
                for (i = last_inc + 1; i < d; i++){
                    cout << 9;
                }
                cout << endl;
            } else
            {
                if (digits[0] > 1){
                    cout << digits[0] - 1;
                }
                for (i = 1; i < d; i++){
                    cout << 9;
                }
                cout << endl;
            }
        }
    }
    return 0;
}
