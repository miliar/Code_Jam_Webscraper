#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

#define x first
#define y second
#define NMAX 1005

int T, nr, k, v[NMAX];
char s[NMAX];

int main (){
    
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        scanf("%s", s);
        nr = strlen(s);
        scanf("%d\n", &k);
        
        printf("Case #%d: ", t);
        
        for(int i = 0; i < nr; i++)
            v[i + 1] = (s[i] == '+' ? 1 : 0);
            
        int answer = 0;
        
        for(int i = 1; i <= nr - k + 1; i++) {
            if(!v[i]){
                answer++;
                for(int j = i; j < i + k; j++)
                    v[j] = 1 - v[j];
            }
        }
        
        int sum = 0;
        for(int i = 1; i <= nr; i++)
            sum += v[i];
        if(sum == nr)
            printf("%d\n", answer);
        else
            printf("IMPOSSIBLE\n");
    }
    
    return 0;
}


