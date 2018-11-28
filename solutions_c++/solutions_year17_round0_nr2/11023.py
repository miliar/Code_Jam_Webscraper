//
//  main.cpp
//  Tidy Number
//
//  Created by Ahmed Sarafudheen on 08/04/17.
//  Copyright © 2017 virtus-it. All rights reserved.
//

#include <iostream>

int findIndex(int arr[20],int size);
int makeArray(long int n , int arr[] , int size);
int intLength(long int i);
bool isTidy (int arr[],int size);
void reduceValue(int arr[],int size, int index);
long int mergeArray (int arr[],int size );
int tidyProcess();
using namespace std;
int main(int argc, const char * argv[]) {
    
    long int Value = 999;
    int len = intLength(Value);
    int array[20] ;
    makeArray(Value, array, len);
    if (!isTidy(array, len)) {
        int index = findIndex(array, len);
        reduceValue(array, len, index);
        for (int i = 0; i < len ; i ++) {
            cout << array[i];
        }
        cout << " Reduced Number  \n";
        long int Val = mergeArray(array, len);
        cout << Val -1 << "  final answer \n";
    } else {
        
        cout << Value << " Number Aready TIDY \n";
    }
    return 0;
}

long int mergeArray(int arr[], int size){
    
    long int number = 0;
    for (int i = 0;i < size ;i++){
        
        number = (number * 10) + arr[i];
    }
    return  number;
}

void reduceValue(int arr[],int size , int index ) {
    for (int i = index + 1 ; i < size ; i ++) {
        
        arr[i] = 0;
    }
}

int findIndex(int arr[],int size) {
    
    int index = 0 ;
    
    for (int i = size -1 ; i >= 0 ; i--) {
        
        if (arr[i] <= arr[i - 1]) {
            index = i - 1;
        }
    }
    
    return index ;
}

bool isTidy(int arr[], int size) {
    
    for (int i = size -1; i >= 0; i --) {
        if (arr[i] < arr[i-1]) {
            
            return false;
        }
    }
    
    return true;
}


int makeArray(long int n, int arr[], int size) {
    
    for (int i = size - 1; i >= 0; i--) {
        
        arr[i] = n % 10;
         n = n/10;
    }
    return 0;
}

int intLength(long int i) {
    int l=0;
    for(;i;i/=10) l++;
    return l==0 ? 1 : l;
}


