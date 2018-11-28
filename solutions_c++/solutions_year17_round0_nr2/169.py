#include <bits/stdc++.h>

using namespace std;

int main(void){
    freopen("testin.txt","r",stdin);
    freopen("testout.txt", "w", stdout);
    int tt;
    char num[20];
    cin >> tt;
    
    for(int t=1; t<=tt; t++){
        cin >> num;
        int n = strlen(num);
        //printf("%s,%d\n",num, n);
        
        int arr[20];
        for(int i=0;i<n;i++){
            arr[i]=num[i]-'0';
        }
        int lastup=0;
        int lastnum=arr[0];
        for(int i=1;i<n;i++){
            if(arr[i]>lastnum){
                lastup=i;
                lastnum=arr[i];
            }else if(arr[i]<lastnum){
                arr[lastup]--;
                for(int j=lastup+1;j<n;j++){
                    arr[j]=9;
                }
                break;
            }else{
                
            }
        }
        
        printf("Case #%d: ", t);
        if(arr[0]>0){
            printf("%d",arr[0]);
        }
        for(int i=1;i<n;i++){
            printf("%d",arr[i]);
        }
        printf("\n");
        
    }
    
    return 0;
}
