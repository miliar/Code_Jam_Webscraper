#include <bits/stdc++.h>
using namespace std;

int T;
char pancakes[1100];

int occurences(){
    int tot = 0;
    for(int i=0;pancakes[i];i++){
        if(pancakes[i] == '-'){
            tot++;
        }
    }
    return tot;
}

int main()
{

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> T;
    for(int c=1;c<=T;c++)
    {
        int amount=0,K,fullLen;

        scanf("%s %d",pancakes,&K);
        for(fullLen=0;pancakes[fullLen];fullLen++);

        for(int i=0;i<=fullLen-K+1;i++)
        {
            if(occurences() == 0){
                break;
            }
            if(pancakes[i] == '-')
            {
                amount++;
                for(int x=0;x<K;x++)
                {
                    if(pancakes[i+x] == '-'){
                        pancakes[i+x] = '+';
                    }else{
                        pancakes[i+x] = '-';
                    }
                }
            }
        }

        if(occurences() != 0){
            cout << "Case #" << c << ": IMPOSSIBLE" << endl;
        }else{
            cout << "Case #" << c << ": " << amount << endl;
        }
    }
}
