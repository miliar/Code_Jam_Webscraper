#include<bits/stdc++.h>
using namespace std;
int main()
{
    FILE *fp, *fc;
    int t;
    ifstream fin("B-small-attempt3.in");
    ofstream fout("out.txt");
    fin>>t;
    for(int cas=1;cas<=t;cas++){
        int n, a[8];
        fin>>n;
        for(int i=0;i<6;i++){
            fin>>a[i];
        }
        int r = a[0], y = a[2], b = a[4], mc = -1, c;
        if(r > mc){
            mc = r;
            c = 0;
        }
        if(y > mc){
            mc = y;
            c = 2;
        }
        if(b > mc){
            mc = b;
            c = 4;
        }
        char res[4*n];
        for(int i=0;i<4*n;i++)
            res[i] = 'a';
        fout<<"Case #"<<cas<<": ";
        if(c == 0){
            if(mc > b+y)
                fout<<"IMPOSSIBLE";
            else{
                int j=0;
                for(int i=0;i<mc;i++){
                    res[j] = 'R';
                    j+=3;
                }
                j=1;
                for(int i=0;i<y;i++){
                    res[j] = 'Y';
                    j+=3;
                }
                if(y < mc){
                    mc = mc-y;
                    for(;mc>0;mc--){
                        res[j] = 'B';
                        j+=3;
                        b--;
                    }
                }
                j = 2;
                if(b){
                    for(int i=0;i<b;i++){
                        res[j] = 'B';
                        j+=3;
                    }
                }
                for(int i=0;i<4*n;i++){
                if(res[i] != 'a')
                    fout<<res[i];
            }
            }
        }
        else if(c==2){
            if(mc > b+r)
                fout<<"IMPOSSIBLE";
            else{
                int j=0;
                for(int i=0;i<mc;i++){
                    res[j] = 'Y';
                    j+=3;
                }
                j=1;
                for(int i=0;i<r;i++){
                    res[j] = 'R';
                    j+=3;
                }
                if(r < mc){
                    mc = mc-r;
                    for(;mc>0;mc--){
                        res[j] = 'B';
                        j+=3;
                        b--;
                    }
                }
                j = 2;
                if(b){
                    for(int i=0;i<b;i++){
                        res[j] = 'B';
                        j+=3;
                    }
                }
                for(int i=0;i<4*n;i++){
                if(res[i] != 'a')
                    fout<<res[i];
            }
            }

        }
        else if(c==4){
            if(mc > y+r)
                fout<<"IMPOSSIBLE";
            else{
                int j=0;
                for(int i=0;i<mc;i++){
                    res[j] = 'B';
                    j+=3;
                }
                j=1;
                for(int i=0;i<r;i++){
                    res[j] = 'R';
                    j+=3;
                }
                if(r < mc){
                    mc = mc-r;
                    for(;mc>0;mc--){
                        res[j] = 'Y';
                        j+=3;
                        y--;
                    }
                }
                j = 2;
                if(y){
                    for(int i=0;i<y;i++){
                        res[j] = 'Y';
                        j+=3;
                    }
                }
            }
            for(int i=0;i<4*n;i++){
                if(res[i] != 'a')
                    fout<<res[i];
            }
        }
        fout<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}

