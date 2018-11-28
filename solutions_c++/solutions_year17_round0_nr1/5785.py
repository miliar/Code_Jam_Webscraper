#include <cstdio>
#include <cstring>
using namespace std;
void flip(char *str, int k){

    for(int i = 0;i < k; i++){
        if(str[i] == '-')
            str[i] = '+';
        else
            str[i] = '-';
    }
}
bool isOk(char *str, int k){
    int i, j;
    i = strlen(str) - 1;
    j = i - k;
    while(i >= j){
        if(str[i] == '-')
            return false;
        i--;
    }
    return true;
}
int main()
{
    int i,j,nr,len,k,t;
    char str[1010];
    freopen("ex1.in","r",stdin);
    freopen("ex1.out","w",stdout);
    scanf("%d",&t);
    j = 1;
    while(j <= t){
        scanf("%s%d", str, &k);
        nr = 0;
        i = 0;
        len = strlen(str);
        while(i <= len - k){

        while(i <= len - k && str[i] == '+')
            i++;

        if(i <= len - k){
            flip(str + i, k);
            nr++;
        }

        }
        if(isOk(str, k))
            printf("Case #%d: %d\n",j,nr);
        else
            printf("Case #%d: IMPOSSIBLE\n",j);

        j++;
    }
    return 0;
}
