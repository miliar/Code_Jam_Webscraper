#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <cmath>
#include <climits>
#include <vector>
#include <queue>
#include <cstring>
#include <iterator>
#include <list>
#include <set>
#include <map>
#include <bitset>

using namespace std;

#define MEMSET(x,v) memset(x,v,sizeof(x))
template<class A, class B> inline bool mina(A &x, B y) {return (x > y)?(x=y,1):0;}
template<class A, class B> inline bool maxa(A &x, B y) {return (x < y)?(x=y,1):0;}
typedef long long int LL;

        int N;
        int R, O, Y, G, B, V;
        int newB;
        int newR;
        int newY;

        int maxAmt, maxPairAmt;
        int other1, other2;
        int other1Pair, other2Pair;
        char maxChar, maxPairChar;
        char other1Char, other2Char;
        char other1PairChar, other2PairChar;

void myprint(char c) {
    if(c == maxChar) {
        while(maxPairAmt > 0) {
            printf("%c%c", maxChar, maxPairChar);
            maxPairAmt--;
        }
    }
    else if(c == other1Char) {
        while(other1Pair > 0) {
            printf("%c%c", other1Char, other1PairChar);
            other1Pair--;
        }
    }
    else {
        while(other2Pair > 0) {
            printf("%c%c", other2Char, other2PairChar);
            other2Pair--;
        }
    }
    printf("%c", c);
}
void fail() {
    printf("IMPOSSIBLE\n");
}
int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d: ", t);

        scanf("%d", &N);

        scanf("%d %d %d %d %d %d", &R, &O, &Y, &G, &B, &V);

        if(O > B) {
            fail(); continue;
        }
        if(G > R) {
            fail(); continue;
        }
        if(V > Y) {
            fail(); continue;
        }

        if(O > 0 && O == B) {
            if(O*2 == N) {
                for(int i = 0; i < O; i++) printf("OB");
                printf("\n");
            }
            else fail();
            continue;
        }
        if(G > 0 && G == R) { 
            if(G*2 == N) {
                for(int i = 0; i < G; i++) printf("GR");
                printf("\n");
            }
            else fail();
            continue;
        }
        if(V > 0 && V == Y) {
            if(V*2 == N) {
                for(int i = 0; i < V; i++) printf("VY");
                printf("\n");
            }
            else fail();
            continue;
        }

        newB = B-O;
        newR = R-G;
        newY = Y-V;

        if(newB > newR+newY) {
            fail(); continue;
        }
        if(newR > newB+newY) {
            fail(); continue;
        }
        if(newY > newB+newR) {
            fail(); continue;
        }

        maxAmt = max(max(newB,newR),newY);
        if(newB == maxAmt) {
            maxChar = 'B';
            maxPairAmt = O; maxPairChar = 'O';
            other1 = newR; other1Char = 'R';
            other1Pair = G; other1PairChar = 'G';
            other2 = newY; other2Char = 'Y';
            other2Pair = V; other2PairChar = 'V';
        }
        else if(newR == maxAmt) {
            maxChar = 'R';
            maxPairAmt = G; maxPairChar = 'G';
            other1 = newB; other1Char = 'B';
            other1Pair = O; other1PairChar = 'O';
            other2 = newY; other2Char = 'Y';
            other2Pair = V; other2PairChar = 'V';
        }
        else if(newY == maxAmt) {
            maxChar = 'Y';
            maxPairAmt = V; maxPairChar = 'V';
            other1 = newR; other1Char = 'R';
            other1Pair = G; other1PairChar = 'G';
            other2 = newB; other2Char = 'B';
            other2Pair = O; other2PairChar = 'O';
        }

        while(maxAmt > other1 && maxAmt > other2) {
            myprint(maxChar);
            myprint(other1Char);
            myprint(maxChar);
            myprint(other2Char);
            maxAmt -= 2;
            other1--;
            other2--;
        }
        while(other1 > other2) {
            myprint(maxChar);
            myprint(other1Char);
            maxAmt--;
            other1--;
        }
        while(other2 > other1) {
            myprint(maxChar);
            myprint(other2Char);
            maxAmt--;
            other2--;
        }
        while(maxAmt > 0) {
            myprint(maxChar);
            myprint(other1Char);
            myprint(other2Char);
            maxAmt--;
            other1--;
            other2--;
        }
        printf("\n");
    }
}
