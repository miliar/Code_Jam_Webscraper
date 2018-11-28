#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <queue>
using namespace std;

int main() {
	priority_queue<unsigned long long int> p;
	
    int t = 5, i = 0, j = 0;
    unsigned long long int n, k, temp = 0;
    char s[30];

    scanf("%d", &t);

    for (i = 0; i < t; i++) {
        scanf("%llu %llu", &n, &k);
        p.push(n);
		
        for (j = 0; j < k-1; j++) {
            temp = p.top();
            p.pop();
            temp--;
            p.push(temp/2);
            p.push(temp-temp/2);
            
        }
        
        temp = p.top();
        temp--;
        
       	printf("Case #%d: %llu %llu\n", i + 1, temp-temp/2, temp/2);
       	
       	p = priority_queue <unsigned long long int>();
    }
    return 0;
}
