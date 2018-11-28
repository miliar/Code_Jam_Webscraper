#include <iostream>

using namespace std;

bool flip( string &pancakes, int pos, int n)
{
    if( pos + n > pancakes.size())
        return false;
    
    for( int i = pos; i < pos + n ; i++ ) {
        if (pancakes[i] == '-')
            pancakes[i] = '+';
        else pancakes[i] = '-';
    }
    return true;
}

void solve(string &pancakes, int n)
{
    bool possible = true;
    int count = 0, i;
    for( i = 0 ; i < pancakes.size();i++){
        if(pancakes[i]=='-'){
            possible = flip( pancakes, i, n);
            if( possible )
                count++;
            else{
                printf("IMPOSSIBLE\n");
                return;
            }
        }
    }
    printf("%d\n", count);
}

int main(int argc, const char * argv[]) {
    int T, n;
    char str[1000];
    string pancakes;
    scanf("%d", &T);
    for(int i=0; i < T ; i++){
        scanf("%s %d", str, &n);
        pancakes = str;
        printf("Case #%d: ", i+1);
        solve(pancakes, n);
    }
    return 0;
}
