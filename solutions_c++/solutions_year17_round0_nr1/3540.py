#include<cstdio>
#include<string.h>
using namespace std;

char arr[1005];
int k;

int main(void){
    FILE *of=fopen("output.txt","w+");
    FILE *f=fopen("input.txt","r");
    int t;fscanf(f,"%d",&t);
    for(int T=1;T<=t;T++){
        fscanf(f,"%s %d",arr,&k);
        int len=(int)strlen(arr);
        int first=0,cnt=0;
        while(1){
            while(arr[first]=='+')
                first++;
            if(first>len-k)
                break;
            for(int i=first;i<first+k;i++){
                if(arr[i]=='+')
                    arr[i]='-';
                else if(arr[i]=='-')
                    arr[i]='+';
            }
            cnt++;
        }
        int success=1;
        for(int i=0;i<len;i++)
            if(arr[i]=='-'){
                success=0;break;
            }
        if(success)
            fprintf(of,"Case #%d: %d\n",T,cnt);
        else
            fprintf(of,"Case #%d: IMPOSSIBLE\n",T);
    }
    return 0;
}
