#include<bits/stdc++.h>
int main(){
    int t; scanf("%d",&t);
    char ch[1001]; int n; int pos[1001],neg[1001];
    for(int i=0;i<t;i++){
        scanf("%s",ch);
        scanf("%d",&n);
        int j=0;
        while(ch[j]!='\0'){
            if(ch[j]=='+') {pos[j]=1; neg[j]=0;}
            else if(ch[j]=='-') {pos[j]=0; neg[j]=1;}
            j++;
        }
        int len=j;
        int flag=0; int counter=0; int rem=n; std::string counte;
        for(int j=0;j<len;j++){
           if(pos[j]==0){
            counter++;
            if(j+n-1<len){
                for(int k=0;k<n;k++){
                        if(pos[j+k]==1) pos[j+k]=0; else if(pos[j+k]==0) pos[j+k]=1;
                    }
            }
            else {counte="IMPOSSIBLE"; j=len;}
           }
        }
        //printf("Case #%d:%d\n",i+1,counter);
        if(counte=="IMPOSSIBLE") std::cout<<"Case #"<<i+1<<": "<<counte<<"\n";
        else std::cout<<"Case #"<<i+1<<": "<<counter<<"\n";
    }
}
