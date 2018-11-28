#include<stdio.h>
#include<inttypes.h>
#include<math.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <functional>
#include <queue>
#include <vector>
#include <iostream>


int main(){
    FILE* f = fopen("bstallinut.txt", "r");
    FILE* fo = fopen("bstalloutput.txt", "w");
    int t = 0;
    fscanf(f, "%d", &t);
    int count = 1;
    while(t--){
        int x = 1;
        int y = 1;
        fscanf(f, "%d", &x);
        fscanf(f, "%d", &y);
        std::priority_queue<int> q;
        q.push(x);
        while(y>0){
            x = q.top();
            q.pop();       
            y--;
            q.push(x/2);
            q.push(x/2 - (1 == x%2 ? 0 : 1));
                // printf("x: %d, x1: %d, x2: %d\n", x, x/2, x/2 - (x%2 ? 0 : 1));
            if(y == 0){
                int r1 = q.top();
                q.pop();
                int r2 = q.top();
                q.pop();
                printf("Case #%d: %d %d\n", count++, x/2, x/2 - (x%2 ? 0 : 1));
            }
        }
        // delete(q);
        // front = 0;
        // rear = -1;
    }
    fclose(f);
    fclose(fo);
}