#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
using namespace std;

int main(){
    int T;
  //  freopen("B-small-attempt3.in","r",stdin);
    cin>>T;
  //  cout << T<<endl;
    char numbers[100][20];
    int length[100];
    int errorpoint[100];
    int minuspoint;
    int flag;
    for(int i=0;i<T;i++){
        cin>>numbers[i];
        length[i]=strlen(numbers[i]);
    }
   for(int i=0;i<T;i++){//find the error
        flag=0;
        errorpoint[i]=0;
        minuspoint=0;
        if(length[i]==1)
            continue;
        else{
            for(int j=1;j<length[i];j++){
                if(numbers[i][j]<numbers[i][j-1]){
                    errorpoint[i]=j;
             //       flag=1;
                    break;
                }
            }
            if(errorpoint[i]!=0){
                for(int j=errorpoint[i];j<length[i];j++)
                    numbers[i][j]='9';
                numbers[i][errorpoint[i]-1]--;
                if(numbers[i][errorpoint[i]-1]<'0'){
                    numbers[i][errorpoint[i]-1]='9';
                    for(int k=errorpoint[i]-2;k>=0&&numbers[i][k]=='0';k--){
                        numbers[i][k]='9';
                        minuspoint=k;
                    }
                    numbers[i][minuspoint]--;
                }
                for(int j=errorpoint[i];j>0;j--){
                    if(numbers[i][j]<numbers[i][j-1]||numbers[i][j-1]=='0'){
                        numbers[i][j]='9';
                        numbers[i][j-1]-=1;
                    }
                }
            }
        }
    }
    int nonzero;
    for(int i=0;i<T;i++){
        nonzero=0;
        cout<<"Case #"<<i+1<<": ";
        for(int j=0;j<length[i];j++){
            if(numbers[i][j]>'0')
                    break;
            nonzero+=1;
        }
        for(int j=nonzero;j<length[i];j++)
            cout<<numbers[i][j];
        cout<<endl;
    }
    return 0;
}
