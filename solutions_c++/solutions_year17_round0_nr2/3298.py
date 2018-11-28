#include <bits/stdc++.h>

using namespace std;

char arr[20];

bool dp[20][10][2];
vector <int> ans;
vector <int> curr;

int solve(int i,int last,bool lesss) {
    if(ans.size() != 0)
        return true;
    if(i == strlen(arr)) {
        ans = curr;
        return true;
    }

    if(dp[i][last][lesss])
        return true;

    if(lesss) {
        for(int j = 9;j>=last;j--) {
            curr.push_back(j);
            solve(i+1,j,1);
            curr.pop_back();
            if(ans.size() != 0)
                break;
        }
    } else {
        for(int j = arr[i]-'0';j>=last;j--) {
            curr.push_back(j);
            solve(i+1,j,j<arr[i]-'0'?1:0);
            curr.pop_back();
            if(ans.size() != 0)
                break;
        }
    }

    return dp[i][last][lesss] = true;
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1;i<=t;i++) {
        if(i != 1) {
            printf("\n");
            memset(dp,false,sizeof dp);
            ans.clear();
            curr.clear();
        }
        scanf("%s",arr);
        solve(0,0,0);
        printf("Case #%d: ",i);
        int j = 0;
        for(;j<ans.size();j++) {
            if(ans[j] != 0)
                break;
        }
        for(;j<ans.size();j++)
            printf("%d",ans[j]);
    }
    return 0;
}
