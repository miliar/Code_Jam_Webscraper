#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <array>

#define PI 3.14159265358979323846

using namespace std;

typedef struct{
    int H;
    int R;
}Pancake;

int n;
int size;


long double calculate_area(int R){
    return PI * R * R;
}

long double calculate_H(int R, int H){
    return 2 * PI * R * H;
}
/*
long double part(int size, vector<Pancake> panc, int next, vector<Pancake> pancakes){
    if(size < n)
        return part(pancakes[next]);

    long double count = 0;

    for(int i = 0; i < size; i++)
        count += calculate_H(panc[i].R, panc.H) + calculate_area(panc.R);

    return count;
}
*/

bool acompare(Pancake p1, Pancake p2){
    return calculate_H(p1.R, p1.H) > calculate_H(p2.R, p2.H);
}

bool aux_compare(Pancake p1, Pancake p2){
    return calculate_area(p1.R) > calculate_area(p2.R);
}

long double calculate(Pancake pancakes[]){
    sort(pancakes, pancakes+n, acompare);

    long double count = 0;

    for(int i = 0; i < size; i++)
        count += calculate_H(pancakes[i].R, pancakes[i].H);

    sort(pancakes, pancakes + size, aux_compare);
    count += calculate_area(pancakes[0].R);

    sort(pancakes, pancakes + n, aux_compare);
    long double count2 = calculate_area(pancakes[0].R);

    sort(pancakes + 1, pancakes+n, acompare);
    for(int i = 0; i < size; i++)
        count2+= calculate_H(pancakes[i].R, pancakes[i].H);

    if(count > count2)
        return count;
    return count2;
}

int main(){
    int T;

    scanf("%d", &T);

    for(int i = 1; i <= T; i++){
        Pancake pancakes[1000000];
        scanf("%d", &n);
        scanf("%d", &size);

        for(int j = 0; j < n; j++){
            Pancake test;
            scanf("%d %d", &pancakes[j].R, &pancakes[j].H);

        }

        long double max = calculate(pancakes);

        printf("Case #%d: %.9llf\n", i,max);
    }

    return 0;
}
