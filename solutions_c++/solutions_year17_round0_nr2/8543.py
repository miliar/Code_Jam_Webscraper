#include <bits/stdc++.h>
using namespace std;
int t,tc,n;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(tc++<t){
        vector<int> arr;
        char str[20];
        scanf("%s",str);
        n=strlen(str);

        for(int x=0;x<n;x++){
            arr.push_back(str[x]-'0');
        }
        bool flag=false;

        for(int x=n-1;x>0;x--){
            if(arr[x]<arr[x-1]){
                arr[x]=9;
                arr[x-1]--;
            }
        }
        printf("Case #%d: ",tc);
        for(int x=0;x<n;x++){
            if(x==0&&arr[x]==0)
                continue;
            if(arr[x]==9)
                flag=true;
            if(flag)
                printf("9");
            else
                printf("%d",arr[x]);
        }
        printf("\n");
    }

}
