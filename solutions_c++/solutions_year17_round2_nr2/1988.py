#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<math.h>

using namespace std;

#define x first
#define y second
#define NMAX 1005
#define INF 1000000002

int n, red, yellow, blue, green, violet, orange, nr, t;
char answer[NMAX];

void solveOrange() {
    for(int i = 1; i <= orange; i++)
        printf("OB");
}

void solveGreen() {        
    for(int i = 1; i <= green; i++)
        printf("GR");
}

void solveViolet() {        
    for(int i = 1; i <= violet; i++)
        printf("VY");
}

int main (){
    
    scanf("%d",&t);
    for(int test = 1; test <= t; test++) {
        scanf("%d%d%d%d%d%d%d",&n,&red,&orange,&yellow,&green,&blue,&violet);
        
        if(orange + blue == n) {
            printf("Case #%d: ", test);
            if(orange != blue) {
                printf("IMPOSSIBLE\n");
            }
            else
                solveOrange();
            continue;
        }
        
        if(violet + yellow == n) {
            printf("Case #%d: ", test);
            if(yellow != violet) {
                printf("IMPOSSIBLE\n");
            }
            else
                solveViolet();
            continue;
        }
        
        if(red + green == n) {
            printf("Case #%d: ", test);
            if(red != green) {
                printf("IMPOSSIBLE\n");
            }
            else
                solveGreen();
            continue;
        }

        if((orange && orange >= blue) || (green && green >= red) || (violet && violet >= yellow)) {
            printf("Case #%d: IMPOSSIBLE\n", test);
            continue;
        }
        red -= green;
        yellow -= violet;
        blue -= orange;
        if(red > yellow + blue || yellow > red + blue || blue > yellow + red) {
            printf("Case #%d: IMPOSSIBLE\n", test);
            continue;
        }
        
        //printf("%d %d %d\n", red, yellow, blue);
        int nr = 0;
        if(red) {
            answer[++nr] = 'R';
            red--;
            red = -red;
        }
        else if(yellow) {
            answer[++nr] = 'Y';
            yellow--;
            yellow = -yellow;
        }
        while(red || yellow || blue) {
            if(red >= yellow && red >= blue) {
                answer[++nr] = 'R';
                red--;
            } else if(yellow >= red && yellow >= blue) {
                answer[++nr] = 'Y';
                yellow--;
            } else if(blue >= red && blue >= yellow) {
                answer[++nr] = 'B';
                blue--;
            }
            red = abs(red);
            blue = abs(blue);
            yellow = abs(yellow);
            if(answer[nr] == 'R')
                red = -red;
            else if(answer[nr] == 'B')
                blue = -blue;
            else if(answer[nr] == 'Y')
                yellow = -yellow;
            //printf("%d %d %d\n", red, yellow, blue);
            //break;
        }
        printf("Case #%d: ", test);
        
        int checkOrange = 0, checkGreen = 0, checkViolet = 0;
        for(int i = 1; i <= nr; i++) {
            printf("%c", answer[i]);
            if(answer[i] == 'R' && !checkGreen) 
                solveGreen();
            if(answer[i] == 'B' && !checkOrange) 
                solveOrange();
            if(answer[i] == 'Y' && !checkViolet) 
                solveViolet();
        }
        printf("\n");
    }
    
    return 0;
}