#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("txt.in", "r", stdin);
    freopen("txt.out", "w", stdout);

    int t, k;
    string ord;

    cin >> t;
    for(int z = 1; z <= t; ++z) {
        bool flag = false;
        cin >> ord >> k;

        int num = 0;
        for(int i = 0; i < ord.length(); ++i) {
            if(ord[i] == '-') {
                num++;
                if(i + k - 1 > ord.length() - 1) {
                    cout << "Case #" << z << ": " <<"IMPOSSIBLE" << "\n";
                    flag = true;
                    break;
                }
                for(int j = i; j < i + k; ++j) {
                    if(ord[j] == '-') ord[j] = '+';
                    else              ord[j] = '-';
                }
            }
        }

        if(flag == false)
            cout << "Case #" << z << ": " << num << "\n";
    }

    return 0;
}
