#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;
int main(){

    int t,cnt,i,len,k,j;
    char s[1001];
    scanf("%d",&t);
    for(j=1;j<=t;j++){
        scanf("%s %d",s,&k);
        //scanf("%d",k);
        len=strlen(s);
        //printf("s = %s\n",s);
        //printf("len = %d\n",len);
        //printf("k = %d\n",k);
        cnt=0;
        for(i=0;i+k<len;i++){
            if(s[i] == '-'){
                for(int p=0;p<k;p++){
                    s[i+p] = (s[i+p] == '-' ? '+' : '-');
                }
                cnt++;
            }
        }
        int flag=1;
        for(i =len-k+1;i<len;i++){
            //printf("Inside loop");
            if(s[i] != s[i-1]){
                //printf("Inside loop and if");
                cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
                flag=0;
                break;
            }
        }
        if(flag){
            //printf("%d",cnt);
            if(s[len-1]=='-')
                cnt++;
            cout<<"Case #"<<j<<": "<<cnt<<endl;

        //return count+"";
        }
    }

    return 0;
}

