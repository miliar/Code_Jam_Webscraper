
#include<bits/stdc++.h>
using namespace std;
struct st{
    int num;
    char cur;
}x[4];
bool stsort(st e1,st e2){
    return e1.num<e2.num;
}
int main(){
    FILE *fp1 = fopen("C:\\Users\\Hmc1994\\Downloads\\B-small-attempt1.in","r+");
    FILE *fp2 = fopen("C:\\Users\\Hmc1994\\Downloads\\ans.out","w+");
    int t;
    fscanf(fp1,"%d",&t);
    int tot=1;
    while(t--){
        int n;
        fscanf(fp1,"%d",&n);
        int r,g,b,o,v,y;
        fscanf(fp1,"%d%d%d%d%d%d",&r,&o,&y,&g,&b,&v);
        x[1].num=r;x[1].cur='R';
        x[2].num=b;x[2].cur='B';
        x[3].num=y;x[3].cur='Y';
        sort(x+1,x+1+3,stsort);
        string ans;
        if(x[1].num+x[2].num<x[3].num){
            ans="IMPOSSIBLE";
            cout<<ans<<endl;
            fprintf(fp2,"Case #%d: %s\n",tot++,ans.c_str());
            continue;
        }
        else{
            for(int i=1;i<=x[3].num;i++) ans+=x[3].cur;
            int pos,num;
            int ss=0;
            for(pos=0,num=1;num<=x[2].num;num++){
                ans.insert(pos,1,x[2].cur);
                ss++;
                pos+=2;
            }
            for(num=1;num<=x[1].num;num++){
                if(ss>=x[3].num) break;
                ans.insert(pos,1,x[1].cur);
                ss++;
                pos+=2;

            }
            for(pos=0;num<=x[1].num;num++){
                ans.insert(pos,1,x[1].cur);
                pos+=2;
            }
        }
        cout<<ans<<endl;
        fprintf(fp2,"Case #%d: %s\n",tot++,ans.c_str());
    }
}
