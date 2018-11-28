#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char **argv)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T=0;
    long long n, k, a, b, newX, newY, newCntX, newCntY;
	long long x, y, cntX, cntY;
    long long intS, intF;
    long long intVal;
    bool printed;
    
    scanf("%d",&T);
	
	for (int t=1;t<=T;t++) {
        scanf("%lld%lld",&n,&k);
        
        intS = intF = 1;
        
        x = n; cntX = 1;
        y = cntY = 0;
        intVal = 1;
        printed = false;
        
        while (k > intF) {
            intS += intVal;
            intVal*=2;
            intF += intVal;
            
            if (intF > n) {
                printf("Case #%d: 0 0\n",t);
                printed = true;
                break;
            }
            
            newCntX = 0;
            newCntY = 0;
            
            a = x/2; b = (x-1)/2;
            if (a==b) {
                newX = a;
                newCntX += cntX*2;
            } else {
                newX = a;
                newCntX += cntX;
                newY = b;
                newCntY += cntX;
            }
            
            a = y/2; b = (y-1)/2;
            if (a==b) {
                newCntY += cntY*2;
            } else {
                newY = b;
                newCntX += cntY;
                newCntY += cntY;
            }
            
            x = newX; y = newY;
            cntX = newCntX; cntY = newCntY;
            
            //printf("We are in interval %lld-%lld and we have %lld-%lld and %lld-%lld\n",intS,intF,x,cntX,y,cntY);
        }
        
        if (!printed) {
            if (k<intS+cntX) {
                printf("Case #%d: %lld %lld\n",t,x/2,(x-1)/2);
            } else {
                printf("Case #%d: %lld %lld\n",t,y/2,(y-1)/2);
            }
        }
    }
}