//
//  main.cpp
//  ROH
//
//  Created by Akashdeep Saluja on 20/03/16.
//  Copyright (c) 2016 Akashdeep Saluja. All rights reserved.
//

#include <iostream>
#include<math.h>
#include <string.h>
#include<map>
#include<set>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;

#define mod 1000000007
#define init int i,j,k,l, test, m, n





int main(){
    init;
    scanf("%d", &test);
    bool a[1003][1003];
    while (test--) {
        scanf("%d %d", &n, &m);
        k = n;
        j = (k/2)*((k/2)-1);
        if (j > m || (n == 5 && m==5)) {
            for (i = 0; i < m; i++) {
                scanf("%d %d", &k, &l);
            }
            printf("NO\n");
            continue;
        }
        
        for (i = 0; i <= n; i++) {
            for (k = 0; k<=n; k++) {
                a[i][k] = 1;
            }
        }
        for (i = 0; i < m; i++) {
            scanf("%d %d", &k, &l);
            a[k][l] = 0;
            a[l][k] = 0;
        }
        bool no = false;
        //taken complement of the graph
        for (i = 1; i <= n; i++) {
            for (j = i+1; j <= n; j++) {
                if (a[i][j]) {
                    for (k = j+1; k <= n; k++) {
                        if(a[i][k] && a[j][k]){
                            no = true;
                            break;
                        }
                    }

                }
                if(no)
                    break;
               
            }
            if(no)
                break;
            
        }
        if(no)
            printf("NO\n");
        else printf("YES\n");
        
    }
}