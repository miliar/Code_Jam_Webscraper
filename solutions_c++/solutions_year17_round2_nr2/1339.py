#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int ring[1005];

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: ",t);
        int  n, R, O, Y, G, B, V;

        cin>> n>> R>> O>> Y>> G>> B>> V;

        int c[4] ={0};
        c[1] = R;
        c[2] = Y;
        c[3] = B;

        int ch = 0;

        for(int i=1; i<=3; i++)
        	if(c[i] > c[ch])
        		ch = i;

        c[ch]--;
        ring[1] = ch;

        int l = 2;
        while(l<n)
        {
            ch = 0;
            for(int i=1; i<=3; i++)
                if(i != ring[l-1] && c[i] > c[ch])
                    ch = i;
            if(ch == 0)
                break;
            c[ch]--;
            ring[l++] = ch;
        }
        if(l<n)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        for(int i=1; i<=3; i++)
            if(c[i])
                ch = i;

        ring[n] = ch;
        int temp;

        if(ring[n] != ring[n-1] && ring[n]!= ring[1])
            goto Lab;

        temp = ring[n];
        ring[n] = ring[n-1];
        ring[n-1] = temp;

        if(ring[n] != ring[n-1] && ring[n]!= ring[1] &&
            ring[n-1] != ring[n-2])
            goto Lab;

        printf("IMPOSSIBLE\n");
        continue;


        Lab:printf("");
        char col[4] = {'A', 'R', 'Y', 'B'};

        for(int i=1; i<=n; i++)
        	printf("%c", *(col + ring[i]) );
        printf("\n");
    }
    return 0;
}
