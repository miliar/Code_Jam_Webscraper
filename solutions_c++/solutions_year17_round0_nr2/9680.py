#include<fstream>
#include<string.h>
using namespace std;

int main() {
    int n,flag,started;
    ifstream fi("fileinaaa.txt",ios::in);
    ofstream fo("fileoutaaa.txt",ios::out);
    char x[20];
    fi>>n;
    for (int i=0; i<n; i++) {
        fi>>x;flag=1;
        while(flag){
            flag=0;
            for(int j=0; j<strlen(x)-1; j++) if(x[j]>x[j+1]) flag=1;
            if (flag) {
                x[strlen(x)-1]=x[strlen(x)-1]=='0'?'9':x[strlen(x)-1]-1;
                for(int k=strlen(x)-2; k>=0; k--) {
                    if(x[k+1]=='9') x[k]=x[k]=='0'?'9':x[k]-1;
                    else break;
                }
            }
            else{
                started=0;
                fo<<"case #"<<i+1<<": ";
                for(int q=0;q<strlen(x);q++){
                    if(!started){
                        if(x[q]!='0'){
                            fo<<x[q];started=1;
                        }
                    }
                    else fo<<x[q];
                }
                fo<<"\n";
            }

        }
    }
}
