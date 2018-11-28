#include <iostream>
#include <stdio.h>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <queue>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;

    cin >> t;

    string n;
    for (int i = 0; i < t; i++)
    {
        cin >> n;

        vector<int> num (n.length());

        for (int j = 0; j < num.size(); j++){
            num[j] = n[j] - '0';
        }

        while (true) {

            bool valid = true;

            for (int j = 0; j < num.size() - 1 && valid; j++){

                if(num[j] > num[j + 1]){
                    num[j]--;
                    for(int b = j + 1; b < num.size(); b++){
                        num[b] = 9;
                    }
                    valid = false;
                }
            }

            if (valid) break;
        }

        int b = 0;
        cout <<"Case #"<< (i + 1) <<": ";
        for (int j = 0; j < num.size(); j++){
            b += num[j];

            if (b > 0){
                cout << num[j];
            }
        }


        cout << '\n';

    }

    return 0;
}
