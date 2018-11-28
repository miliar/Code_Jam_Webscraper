#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ll;

int main (){
    int T;
    scanf("%d" ,&T);
    for (int t=1;t<=T;t++){
        int r,c;
        scanf("%d %d", &r, &c);
        vector < int > num(r,0);
        vector < string > out(r,"");
        bool st = false;
        for(int i=0;i<r;i++){
            char in[30];
            scanf("%s", in);
            char last = '?';
            for(int y=0;y<c;y++){
                if(in[y]!='?'){
                    if(num[i]++==0){
                        last = in[y];   
                    }
                }
            }
            
            if(num[i]>0){
                for(int y=0;y<c;y++){
                    if(in[y]!='?'){
                        last = in[y];
                    }
                    out[i].push_back(last);
                }
                if(st==false){
                    for(int z=0;z<i;z++){
                        out[z]=out[i];
                    }
                    st=true;
                }
                //cerr << "ok"<<y <<endl;
            }else{
                if(st){
                    num[i]=1;
                    out[i]=out[i-1];
                }
            }
        }
        printf("Case #%d:\n", t);
        for(int i=0;i<r;i++){
            printf("%s\n", out[i].c_str());
        }
    }
    

    return 0;
}