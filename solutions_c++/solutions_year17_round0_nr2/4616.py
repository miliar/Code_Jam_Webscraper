#include <bits/stdc++.h>

using namespace std;

bool check(long long a){
    int last = 9;
    bool ok=true;
    while(a){
        if(last<a%10){
            ok=false;
            break;
        }
        last = a%10;
        a/=10;
    }
    return ok;
}
int cyfry[30];

bool ca(){
    for(int i=1;i<30;i++){
        if(cyfry[i]==-1)break;
        if(cyfry[i]<cyfry[i-1])return false;
    }
    return true;
}
void read(long long a){
    int dl = 0;
    long long aa = a;
    while(aa){
        dl++;
        aa/=10;
    }
    for(int i=0;i<30;i++){
        if(i>=dl)cyfry[i]=-1;
        else{
            cyfry[dl-1-i]=a%10;
            a/=10;
        }
    }
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t=0;t<T;t++){
        long long in, out=0;
        scanf("%lld", &in);
        read(in);
        if(ca()){
            out = in;
        }
        else{
            int i;
            for(i=1;i<30;i++){
                if(cyfry[i]<cyfry[i-1])break;
            }
            for(int y=i-1;y>=0;y--){
                if(y==0){
                    out = --cyfry[0];
                   
                    for(int z=1;z<30;z++){
                        if(cyfry[z]==-1)break;
                        out = out*10+9;
                    }
                }else{
                    if(cyfry[y-1]<cyfry[y]){
                        for(int z=0;z<30;z++){
                            if(z<y){
                                out = out*10+cyfry[z];
                            }
                            if(z==y){
                                out = out*10+cyfry[z]-1;
                            }
                            if(z>y){
                                if(cyfry[z]==-1)break;
                                out = out*10+9;
                            }
                        }
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %lld\n",t+1,out);
    }

    return 0;
}