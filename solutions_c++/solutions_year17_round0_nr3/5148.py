/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: kevin
 *
 * Created on April 7, 2017, 10:54 PM
 */

#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <map>
#include <algorithm>

using namespace std;
int findMin(int stalls, int people);
int getMin(int big, int small);


int main(int argc, char** argv) {
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);
    int num;
    cin >> num;
    for(int i = 0; i < num; i++){
        int stalls = 0;
        int people = 0;
        cin>>stalls>>people;
        int ans = findMin(stalls, people);
        if(ans % 2 == 0){
            ans = ans/10;
            cout<<"Case #" <<i + 1<<": "<<ans<<" "<<ans<<endl;
        }
        else{
            ans = (ans-1)/10;
            cout<<"Case #" <<i + 1<<": "<<ans + 1<<" "<<ans<<endl;
        }
    }
    return 0;
}
    

int findMin(int stalls, int people){
    if(people == 1){
        if(stalls % 2 == 0){
            return (stalls/2 - 1) * 10 + 1;
        }
        return (stalls/2) * 10;
    }
    if(stalls %2 == 0){
        if(people %2 == 0){
            if(people/2 - 1 > 0){
                return getMin(findMin(stalls/2 - 1, people/2 - 1), findMin(stalls/2, people/2));
            }
            return findMin(stalls/2, people/2);
        }
        return getMin(findMin(stalls/2 - 1, people/2), findMin(stalls/2, people/2));
    }
    if(people %2 == 0){
        if(people/2 - 1 > 0){
            return getMin(findMin(stalls/2, people/2 - 1), findMin(stalls/2, people/2));
        }
        return findMin(stalls/2, people/2);
    }
    return getMin(findMin(stalls/2, people/2), findMin(stalls/2, people/2));
}

int getMin(int n, int p){
    if(n < p){
        return n;
    }
    return p;
}