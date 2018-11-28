#include<bits/stdc++.h>
using namespace std;
#define x first
#define y second
typedef long long int LL;
int main(){
    int t, C=0;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        int a,aa,b,bb,c,cc;
        scanf("%d%d%d%d%d%d",&a,&aa,&b,&bb,&c,&cc);
        vector<pair<int,char>> arr;
        arr.push_back({a, 'R'});
        arr.push_back({b, 'Y'});
        arr.push_back({c, 'B'});
        sort(arr.begin(),arr.end());
        if(arr[2].x>arr[1].x+arr[0].x){
            printf("Case #%d: IMPOSSIBLE\n",++C);
            continue;
        }

        printf("Case #%d: ",++C);
        int cnt = arr[1].x+arr[0].x-arr[2].x;
        for(int i=0;i<cnt;i++){
            for(int j=2;j>=0;j--) putchar(arr[j].y);
        }
        for(int i=0;i<3;i++) arr[i].x-=cnt;
        for(int i=0;i<arr[2].x;i++){
            putchar(arr[2].y);
            if(arr[1].x){
                arr[1].x--;
                putchar(arr[1].y);
            }
            else{
                putchar(arr[0].y);
            }
        }
        puts("");
    }
}
