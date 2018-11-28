#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

void trans(char Nstr[], int N[]);
void printN(int N[], int len);
void printNrev(int N[], int len);
void solve(int N[], int len);
void nine(int N[], int len);
int main(){

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    char Nstr[2000]={0};
    int N[2000]={0};
    int cnt=0;
    scanf("%d%*c", &T);
    while(cnt < T)
    {
        scanf("%s", Nstr);
        trans(Nstr,N);
        solve(N, strlen(Nstr));
        printf("Case #%d: ", cnt+1);
        printNrev(N, strlen(Nstr));
        cnt++;
    }
    return 0;
}

void trans(char Nstr[], int N[])
{
    int len = strlen(Nstr);
    for(int i=0; i<len; i++)
    {
        N[len-1-i] = Nstr[i]-'0';
    }
}

void printN(int N[], int len)
{
    for(int i=0; i<len; i++)
    {
        printf("%d", N[i]);
    }
    printf("\n");
}

void printNrev(int N[], int len)
{
    for(int i=len-1; i>=0; i--)
    {
        if(N[i]==0 && i==len-1)
        {
            continue;
        }
        printf("%d", N[i]);
    }
    printf("\n");
}

void solve(int N[], int len)
{
    bool check = false;
    while(!check)
    {
        check = true;
        for(int i=0; i<len-1; i++)
        {
            if(N[i] < N[i+1])
            {
                check = false;
                nine(N, len);
                break;
            }
        }
    }
}

void nine(int N[], int len)
{
    for(int i=0; i<len-1; i++)
    {
        if(N[i]<N[i+1])
        {
            N[i+1] = N[i+1] - 1;
            for(int j=0; j<i+1; j++)
            {
                N[j] = 9;
            }
            break;
        }
    }
}
