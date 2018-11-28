//
//  main.cpp
//  2017_CodeJam
//
//  Created by mjbox on 2017. 4. 7..
//  Copyright © 2017년 mjbox. All rights reserved.
//
#include <stdio.h>
#include <iostream>
#include <math.h>
#define SUBMIT
#define MAX(a,b) (a) > (b) ? (a) : (b)
#define MIN(a,b) (a) < (b) ? (a) : (b)

using namespace std;
struct DATA {
    double a;
    double b;
    double get() {return a+b;};
};
DATA Data[1000];
int N, K;

void quickSort(DATA arr[], int left, int right) {
    int i = left, j = right;
    double tmp;
    double pivot = arr[(left + right) / 2].b;
    
    /* partition */
    while (i <= j) {
        while (arr[i].b > pivot)
            i++;
        while (arr[j].b < pivot)
            j--;
        if (i <= j) {
            tmp = arr[i].a;
            arr[i].a = arr[j].a;
            arr[j].a = tmp;
            tmp = arr[i].b;
            arr[i].b = arr[j].b;
            arr[j].b = tmp;
            
            i++;
            j--;
        }
    };
    
    /* recursion */
    if (left < j)
        quickSort(arr, left, j);
    if (i < right)
        quickSort(arr, i, right);
}

double cache[1000][1000];

double check(int i, int k) {
    if(k >= K || i >= N) return 0;
    if(cache[i][k] != 0) return cache[i][k];
    
    double value = k == 0 ? Data[i].get() : Data[i].a;
    double a = check(i+1, k+1) + value;
    double b = check(i+1, k);
    cache[i][k] = a > b? a : b;
    return cache[i][k];
}

int main(){
#ifdef SUBMIT
    FILE *fp = fopen("/Users/mjbox/Desktop/1/output.txt", "w");
#endif
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        
        cin >> N >> K;
        double result = 0;
        for(int n = 0; n < N; n++) {
            double R, H;
            cin >> R >> H;
            Data[n].a = 2.0 * M_PI * R * H;
            Data[n].b = M_PI * R * R;
            for(int i = 0; i < K; i++) {
                cache[n][i] = 0;
            }
        }
        quickSort(Data, 0, N-1);
        
        result = check(0, 0);
        
#ifdef SUBMIT
        fprintf(fp, "Case #%d: %.9lf\n", t+1, result);
#else
        printf("\n%d, %.9lf\n", t, result);

#endif
    }
    
#ifdef SUBMIT
    fclose(fp);
#endif
    return 0;
}
