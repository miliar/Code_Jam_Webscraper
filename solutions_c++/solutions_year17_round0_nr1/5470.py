#include <bits/stdc++.h>


using namespace std;


void Flip(string &word,int x,int y){

    for(int i = x; i < y; ++i){
        if(word[i] == '+'){
            word[i] = '-';
        }else{
            word[i] = '+';
        }
    }
}

void Solve(int numbercase){

    string word;
    int k;
    cin >> word >> k;
    int answer = 0;
    for(int i = 0; i + k <= word.size(); ++i){
            if(word[i] == '-'){
                answer++;
                Flip(word , i , i + k);
            }
    }
    int bads = count(word.begin() , word.end() , '-');
    if(bads == 0){
            printf("Case #%d: %d\n",numbercase , answer);
    }else{
            printf("Case #%d: IMPOSSIBLE\n",numbercase);
    }

}


int main(){

    freopen("A-large.in","r",stdin);
    freopen("output.c","w",stdout);


    int tc;
    cin >> tc;
    for(int numbercase = 1; numbercase <= tc; numbercase++){
        Solve(numbercase);
    }



    return 0;
}
