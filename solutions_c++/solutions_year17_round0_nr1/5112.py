#include<iostream>
#include<stdio.h>
using namespace std;

bool pancakes[1000];
bool pancakes2[1000];
char temp;
int flipper, j =0, num1 = 0, num2 = 0 ;


int flip(int startingIndex){
    for (int i = startingIndex; i< startingIndex + flipper; i++){
        pancakes[i] = !pancakes[i];
    }
}

bool alltrue(int starting, int ending){
    for (int i = starting; i<ending; i++){
        if (pancakes[i]!=true) return false;
    }
    return true;

}

int main (){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int testcase;
    scanf("%d ", &testcase);

    for (int i = 0; i< testcase; i++){
        char temp;
        j = 0;
        for(;;){
            scanf("%c", &temp);
            if (temp == '+') {pancakes[j] = pancakes2[j] = true; }
            else if (temp == '-') {pancakes[j] = pancakes2[j] = false; }
            else break;
            j++;
        }
        //cout << "j= " << j << endl;

        //now j has number of pancakes

        scanf("%d ", &flipper);
        //cout << flipper << endl;
        num1 = num2 =0;
        int k;
        for (k = 0; k<= j - flipper; k++){
            if (pancakes[k]== false){
                //cout << "flipping " << k << endl;
                flip(k);
                num1++;
            }
        }
        if (alltrue(k, j) == false) num1 = -1;

        //cout << "-----\n";
        for (int k = 0; k<j; k++){
            pancakes[k] = pancakes2[k];
        }
        for (k = j - 1; k>=flipper - 1; k--){
            if (pancakes[k]== false){
                //cout << "flipping " << k << endl;
                flip(k-flipper+1);
                num2++;
            }
        }
        if (alltrue(0, flipper-1) == false) num2 = -1;



        //printf("%d\n", flipper);
        int res = min(num1, num2);
        if (res!= -1) printf("Case #%d: %d", i+1, res);
        else printf("Case #%d: IMPOSSIBLE", i+1);

        if (i!=testcase-1)printf("\n");
    }

    return 0;
}
