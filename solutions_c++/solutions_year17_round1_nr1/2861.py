#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("A-small-attempt2.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int cases;
    scanf("%d", &cases);
    int caseno = 0;
    while(cases--){
        int r, c;
        scanf("%d %d", &r, &c);
        string str[r];
        vector<char> V;
        int flag = 0;
        for(int i=0; i<r; i++){
            cin >> str[i];
            char ch = 'a';
            for(int j=0; j<str[i].length(); j++){
                if(str[i][j] != '?'){
                    ch = str[i][j];
                    continue;
                }
                else if(ch != 'a'){
                    str[i][j] = ch;
                }
            }
        }
        for(int i=0; i<r; i++){
            char ch = 'a';
            for(int j=str[i].length()-1; j>=0; j--){
                if(str[i][j] != '?'){
                    ch = str[i][j];
                    continue;
                }
                else if(ch != 'a'){
                    str[i][j] = ch;
                }
            }
        }
        for(int i=0; i<r; i++){
            if(str[i][0] == '?'){
                if(i != 0) str[i] = str[i-1];
                else str[i] = str[i+1];
            }
        }
        for(int i=r-1; i>=0; i--){
            if(str[i][0] == '?'){
                if(i != r-1) str[i] = str[i+1];
                else str[i] = str[i-1];
            }
        }
        //cout << ch << endl;
        printf("Case #%d:\n", ++caseno);
        for(int i=0; i<r; i++){
            for(int j=0; j<str[i].length(); j++){
                cout << str[i][j];
            }
            printf("\n");
        }
    }
}
