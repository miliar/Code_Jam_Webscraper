#include <iostream>
#include <bitset>
#include <string>
#include <cstdio>

using namespace std;

#define MAXN 1000 + 3

bitset<MAXN> pancakes;

int main(){
    int t;
    cin >> t;
    for (int ncase = 1; ncase <= t; ncase++){
        string str_in;
        int k, moves = 0;
        cin >> str_in >> k;
        for (int i = 0; i < str_in.size(); i++) pancakes[i] = (str_in[i]=='+' ? 1:0);
        //for (int i = 0; i < str_in.size(); i++) cout << pancakes[i];
        //cout << endl;
        for (int i = 0; i <= str_in.size()-k; i++){
            if (!pancakes[i]){
                moves++;
                for (int j = 0; j < k; j++) {
                    pancakes.flip(j+i);
                }
            }
            //for (int i = 0; i < str_in.size(); i++) cout << pancakes[i]; cout << endl;         
        }
        bool possible = true;
        for (int i = 0; i < str_in.size(); i++)
            if (!pancakes[i]){possible = false; break;}
        printf("Case #%d: ", ncase);
        if (possible) printf("%d", moves);
        else printf("IMPOSSIBLE");
        if (t-ncase) printf("\n");
    }
}