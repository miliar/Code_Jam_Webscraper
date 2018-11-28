#include <iostream>
#include <stdio.h>
#include <math.h>
#include <fstream>
using namespace std;

int N_array[4];

void toArray(int number, int n){
    for(int i=0; i<n; ++i, number/=10){
        N_array[i] = number % 10;
    }
}

int isSorted(int a[4], int n){
    int k=0;

    if(n==1){
        k = 0;
    }
    else{
        for(int i=0; i<n-1; i++){
        if(a[i]<a[i+1])
            k++;
        }
    }

    if(k==0)
        return 1;
    else
        return 0;
}

int mainTask(int N){
    int n = log10(N) + 1;

    toArray(N, n);

    return isSorted(N_array, n);
}

int main(){
    ifstream inputFile("D:\\B-small-attempt2.in");
    ofstream outputFile("D:\\B-small-attempt2.out");

    int T, N, i, output, result;

    inputFile>>T;

    for(i=0; i<T; i++){
        inputFile>>N;

        while(true){
            output = mainTask(N);

            if(output == 1){
                result = N;
                break;
            }

            N--;
        }

        outputFile<<"Case #"<<i+1<<": "<<result<<endl;
    }

    return 0;
}

