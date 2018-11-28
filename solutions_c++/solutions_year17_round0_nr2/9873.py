#include <iostream>

using namespace std;

int T, c;
int A[18];
long long N;

void makerest9(int k)
{
    for (int i = 0; i < k; i++)
        A[i]=9;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for (int i =1; i < T+1; i++)
    {
        scanf ("%d", &N);
        while (N!=0)
        {
            A[c]= N%10;
            N = N/10;
            c++;
        }
        for (int k = 0; k < c-1; k++)
        {
            if (A[k]<A[k+1])
            {
                A[k]=9;
                makerest9(k);
                A[k+1]-=1;
            }
        }
        if (A[c-1]==0)
            c--;
        printf("Case #%d: ", i);
        for (int j = c-1; j >= 0; j--)
            printf("%d", A[j]);
        printf("\n");
        c=0;
    }
    return 0;
}
