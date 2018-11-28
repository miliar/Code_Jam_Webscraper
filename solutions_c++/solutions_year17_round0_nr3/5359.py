//
//  main.cpp
//  CodeJam
//
//  Created by Gavriel Hirsch on 3/9/17.
//  Copyright © 2017 Gavriel Hirsch. All rights reserved.
//

#include <iostream>
#include <stdint.h>
#include <math.h>
#include <vector>
using namespace std;

/*
void pancake_output(){
    int cases, k;
    string s;
    cin >> cases;
    int flips, len;
    int solvable;
    for(int i = 0; i < cases; i++){
        cin >> s >> k;
        len = (int) s.length();
        solvable = 1;
        flips = 0;
        cout << "Case #" << i+1 << ": ";
        for(int j = 0; j < len - k + 1; j++){
            if(s[j] == '-'){
                flips++;
                for(int l = 1; l < k; l++){
                    if(s[j + l] == '-')
                        s[j + l] = '+';
                    else
                        s[j + l] = '-';
                }
            }
        }
        for(int j = len - k + 1; j < len; j++){
            if(s[j] == '-')
                solvable = 0;
        }
        if(solvable)
            cout << flips << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}

uint64_t tidy(uint64_t n){
    int digits = 0;
    uint64_t m = n;
    while(m){
        m /= 10;
        digits++;
    }
    m = n;
    int lower = n % 10;
    int curr;
    for(int i = 1; i < digits; i++){
        m /= 10;
        curr = m % 10;
        if(curr > lower){
            n /= pow(10, i);
            n *= pow(10, i);
            n -= 1;
            m = m - 1;
        }
        lower = m % 10;
    }
    return n;
}

void tidy_output(){
    int cases;
    uint64_t n;
    cin >> cases;
    for(int i = 0; i < cases; i++){
        cin >> n;
        cout << "Case #" << i+1 << ": " << tidy(n) << endl;
    }
}
*/

struct Link{
    int size;
    Link* next;
};

/*
Link* prevMax(Link* node){
    Link* best = node;
    Link* prevBest = NULL;
    Link* prev = node;
    Link* curr;
    int bestval = best->size;
    while((curr = prev->next)){
        if(curr->size > bestval){
            prevBest = prev;
            best = curr;
            bestval = curr->size;
        }
        prev = curr;
    }
    
    return prevBest;
}
*/

Link* add(Link* segments, int val){
    Link* x = new Link;
    x->size = val;
    x->next = NULL;
    if(val == segments->size){
        x->next = segments;
        return x;
    }
    Link* prev = segments;
    Link* curr;
    while((curr = prev->next)){
        if(val >= curr->size){
            prev->next = x;
            x->next = curr;
            return segments;
        }
        prev = curr;
    }
    prev->next = x;
    return segments;
}
 
void unallocate(Link* node){
    Link* prev = node;
    Link* curr;
    while(prev){
        curr = prev->next;
        delete prev;
        prev = curr;
    }
}

/*
void stalls(int n, int k){
    Link* segments = new Link;
    segments->size = n;
    segments->next = NULL;
    Link* old;
    int bestsize;
    for(int i = k; i > 1; i--){
        bestsize = segments->size;
        old = segments;
        segments = segments->next;
        delete old;
        
        if(segments)
            segments = add(segments, bestsize/2);
        else{
            segments = new Link;
            segments->size = bestsize/2;
            segments->next = NULL;
        }
        segments = add(segments, (bestsize - 1)/2);
    }
    bestsize = segments->size;
    cout << bestsize/2 << " " << (bestsize - 1)/2 << endl;
    unallocate(segments);
}


void stalls(int n, int k){
    Link* segments = new Link;
    segments->size = n;
    segments->next = NULL;
    Link* best;
    Link* adder;
    Link* prev = NULL;
    int bestval = 0;
    for(int i = k; i > 1; i--){
        prev = prevMax(segments);
        if(prev){
            best = prev->next;
            prev->next = best->next;
        }
        else{
            best = segments;
            segments = segments->next;
        }
        bestval = best->size;
        delete best;
        if(bestval > 1){
            adder = new Link;
            adder->size = bestval/2;
            adder->next = segments;
            segments = adder;
        }
        if(bestval > 2){
            adder = new Link;
            adder->size = (bestval - 1)/2;
            adder->next = segments;
            segments = adder;
        }
    }
    prev = prevMax(segments);
    if(prev)
        best = prev->next;
    else
        best = segments;
    bestval = best->size;
    cout << bestval/2 << " " << (bestval - 1)/2 << endl;
    unallocate(segments);
}
 */

struct Pair{
    int size;
    int number;
};

void stalls(int n, int k){
    Pair x[2];
    int num;
    int n1, n2;
    if(k == 1){
        cout << n/2 << " " << (n-1)/2 << endl;
        return;
    }
    x[0].size = n/2;
    x[1].size = n/2 - 1;
    if(n % 2 == 0){
        x[0].number = 1;
        x[1].number = 1;
        if(k == 2){
            cout << x[0].size/2 << " " << (x[0].size - 1)/2 << endl;
            return;
        }
        if(k == 3){
            cout << x[1].size/2 << " " << (x[1].size - 1)/2 << endl;
            return;
        }
    }
    else{
        x[0].number = 2;
        x[1].number = 0;
        if(k == 2 || k == 3){
            cout << x[0].size/2 << " " << (x[0].size - 1)/2 << endl;
            return;
        }
    }
    num = 2;
    k -= 3;
    while(k > 0){
        n1 = 0;
        n2 = 0;
        if(x[0].size % 2 == 0){
            n1 = x[0].number;
            n2 = x[0].number + 2*x[1].number;
        }
        else{
            n1 = 2*x[0].number + x[1].number;
            n2 = x[1].number;
        }
        x[0].size /= 2;
        x[1].size = x[0].size - 1;
        x[0].number = n1;
        x[1].number = n2;
        num *= 2;
        k -= num;
    }
    if(k - x[0].number + num < 1){
        cout << x[0].size/2 << " " << (x[0].size - 1)/2 << endl;
        return;
    }
    cout << x[1].size/2 << " " << (x[1].size - 1)/2 << endl;
    return;
}

void stalls_output(){
    int cases;
    int n, k;
    cin >> cases;
    for(int i = 0; i < cases; i++){
        cin >> n >> k;
        cout << "Case #" << i+1 << ": ";
        stalls(n,k);
    }
}

int main(int argc, const char * argv[]) {
    stalls_output();
}
