#include <iostream>
#include <iomanip>

using namespace std;


int main(){
    FILE *in=fopen("input.txt", "r");
    FILE *out=fopen("output.txt","w");

    int tt;
    fscanf(in,"%d",&tt);

    char str[30][30];

    for(int tc=1;tc<=tt;tc++){
        int n,m;
        fscanf(in,"%d %d",&n,&m);
        for(int i=0;i<n;i++){
            fscanf(in,"%s",str[i]);
        }
        for(int i=0;i<n;i++){
            char c = '?';
            for(int j=0;j<m;j++){
                if(str[i][j] != '?'){
                    c = str[i][j];
                }
                else str[i][j] = c;
            }

            for(int j=m-1;j>=0;j--){
                if(str[i][j] != '?'){
                    c = str[i][j];
                }
                else str[i][j] = c;
            }
            if(c == '?' && i!=0){
                for(int j=0;j<m;j++){
                    str[i][j] = str[i-1][j];
                }
            }
        }
        for(int i=n-1;i>=0;i--){
            char c = '?';
            for(int j=0;j<m;j++){
                if(str[i][j] != '?'){
                    c = str[i][j];
                }
                else str[i][j] = c;
            }

            for(int j=m-1;j>=0;j--){
                if(str[i][j] != '?'){
                    c = str[i][j];
                }
                else str[i][j] = c;
            }
            if(c == '?' && i!=n-1){
                for(int j=0;j<m;j++){
                    str[i][j] = str[i+1][j];
                }
            }
        }
        fprintf(out,"Case #%d:\n",tc);
        for(int i=0;i<n;i++){
            fprintf(out,"%s\n",str[i]);
        }
    }
}
