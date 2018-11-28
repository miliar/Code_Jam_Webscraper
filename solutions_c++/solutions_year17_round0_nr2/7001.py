#include<bits/stdc++.h>
using namespace std;
string str;

int n, t, cs = 1;

int main()
{

    freopen("inputtidy.txt", "r", stdin);
    freopen("outputtidy.txt", "w", stdout);

    cin >> t;

    while(t--){
        cin >> str;

        int fnd = -1;

        for(int i = 0; i < str.size() - 1; i++){

            if(str[i] > str[i + 1]){

                fnd = i;
                break;

            }

        }

//        cout << fnd << endl;

        if(fnd == -1){
            cout << "Case #" << cs++ << ": " << str << endl;
            continue;
        }



        while(fnd >= 0){


            if(fnd == 0){
                str[fnd]--;
                break;
            }

            if(str[fnd] != '0') str[fnd]--;
//            cout << str[fnd] << ' ' << str[fnd - 1] << endl;
            if(str[fnd] >= str[fnd - 1]) break;
            fnd--;

        }

        for(int i = fnd + 1; i < str.size(); i++) str[i] = '9';

        cout << "Case #" << cs++ << ": " ;

        bool flg = false;

        for(int i = 0; i < str.size(); i++){
            if(flg){
                printf("%c", str[i]);
            }
            else{
                if(str[i] > '0') {
                    printf("%c", str[i]);
                    flg = true;
                }

            }
        }
        cout << endl;

    }

    return 0;
}
