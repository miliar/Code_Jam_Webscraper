#include <bits/stdc++.h>

using namespace std;
char arr[1005];
char temp[1005];
int k;

int left() {
    int ans = 0;
    for(int i = 0;i<=strlen(arr)-k;i++) {
        if(arr[i] == '+')
            continue;
        ans++;
        for(int j = 0;j<k;j++) {
            if(arr[i+j] == '+')
                arr[i+j] = '-';
            else
                arr[i+j] = '+';
        }
    }
    for(int i = strlen(arr)-k+1;i<strlen(arr);i++)
        if(arr[i] == '-')
            return 1E9;

    return ans;
}

int right() {
    int ans = 0;
    for(int i = strlen(temp)-1;i>=k-1;i--) {
        if(temp[i] == '+')
            continue;
        ans++;
        for(int j = 0;j<k;j++) {
            if(temp[i-j] == '+')
                temp[i-j] = '-';
            else
                temp[i-j] = '+';
        }
    }
    for(int i = k-2;i>=0;i--)
        if(temp[i] == '-')
            return 1E9;

    return ans;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1;i<=t;i++) {
        if(i != 1)
            printf("\n");
        scanf("%s %d",arr,&k);
        for(int j = 0;j<strlen(arr);j++)
            temp[j] = arr[j];
        int ans = left();
        ans = min(ans,right());
        if(ans > strlen(arr))
            printf("Case #%d: IMPOSSIBLE",i);
        else
            printf("Case #%d: %d",i,ans);

    }
    return 0;
}
