#include <iostream>
#include <fstream>
using namespace std;

int main() {
    fstream infile, outfile;
    infile.open("infile.txt", ios::in);
    outfile.open("outfile.txt", ios::out);
    int t,z=0;
    infile>>t;
    while(z<t){
        int r,c,counter=0;
        infile>>r>>c;
        char arr[r][c];
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                infile>>arr[i][j];
                if(arr[i][j]=='?'){
                    counter++;
                }
            }
        }
        int flag,x;
        if(counter==0){}
        else{
            char temp;
            for(int i=0;i<r;i++){
                flag=1;
                x=1;
                for(int j=0;j<c;j++){
                    if(arr[i][j]!='?'){
                        temp=arr[i][j];
                        flag=0;
                        x=0;
                    }
                    if(flag==0){
                        for(int k=0;k<c;k++){
                            if(k==j){}
                            else if(arr[i][k]=='?')
                                arr[i][k]=temp;
                            else{
                                flag=1;
                                temp=arr[i][k];
                            }
                        }
                    }
                }
                if(x==1 && i!=0){
                    for(int j=0;j<c;j++){
                        arr[i][j]=arr[i-1][j];
                    }
                }
            }
            for(int i=r-1;i>=0;i--){
                flag=1;
                for(int j=0;j<c;j++){
                    if(arr[i][j]=='?'){
                        flag=0;
                        break;
                    }
                }
                if(flag==0){
                    for(int j=0;j<c;j++){
                        arr[i][j]=arr[i+1][j];
                    }
                }
            }
        }
        z++;
        outfile<<"Case #"<<z<<":\n";
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                outfile<<arr[i][j];
            }
            outfile<<"\n";
        }
    }
    infile.close();
    outfile.close();
    return 0;
}