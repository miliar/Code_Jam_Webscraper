#include <bits/stdc++.h>
using namespace std;
int num[20], N;
bool cnt(int n, bool y)
{
    bool g = 1;
    int i, j;
    if(n < 0) return 1;
    if(y) {i = num[n]; j = num[n+1];}
    else {i = 9;j = 0;g = 0;}
    for(; i >= j ; i--)
    {
        num[n] = i;
        if(cnt(n-1, g)) return 1;
        g = 0;
    }
    return 0;
}
int main()
{
    int T;
    bool y = 1;
    long long n;
    scanf("%d", &T);
    //ofstream fout("output.txt");
    for(int i = 1 ; i <= T ; i++)
    {
        scanf("%lld", &n);
        N = 0;
        while(n)
        {
            num[N++] = n%10;
            n /= 10;
        }
        y = 1;
        for(int i = num[N-1] ; i > -1 ; i--)
        {
            num[N-1] = i;
            if(cnt(N-2, y)) break;
            y = 0;
        }
        y = 1;
        printf("Case #%d: ", i);
        //fout << "Case #" << i << ": ";
        for(int i = N-1 ; i > -1 ; i--)
        {
            if(num[i]) y = 0;
            if(!y || !i) {printf("%d", num[i]);}//fout << num[i];}
        }
        printf("\n");
        //fout <<endl;
    }
    return 0;
}
