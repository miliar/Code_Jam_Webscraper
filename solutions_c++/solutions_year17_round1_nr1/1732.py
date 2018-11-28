#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>

using namespace std;
int t,r,c;
char arr[30][30];
ofstream answer;

int main()
{
    answer.open("answer.txt");
    scanf("%d",&t);
    for (int i=0;i<t;i++){
        scanf("%d%d",&r,&c);
        for (int j=0;j<r;j++){
            for (int k=0;k<c;k++){
                cin >> arr[j][k];
            }
        }
        for (int w=0;w<625;w++){
            for (int j=0;j<r;j++){
                for (int k=0;k<c;k++){
                    if (arr[j][k]=='?'){
                        if (k-1>=0 && arr[j][k-1]!='?') arr[j][k]=arr[j][k-1];
                        else if (k+1<=c-1 && arr[j][k+1]!='?') arr[j][k]=arr[j][k+1];
                        //cout << arr[j][k];
                    }
                }
            }
        }
        for (int w=0;w<625;w++){
            for (int j=0;j<r;j++){
                for (int k=0;k<c;k++){
                    if (arr[j][k]=='?'){
                        if (j-1>=0 && arr[j-1][k]!='?') arr[j][k]=arr[j-1][k];
                        else if (j+1<=r-1 && arr[j+1][k]!='?') arr[j][k]=arr[j+1][k];
                    }
                }
            }
        }
        answer << "Case #"<<i+1<<":"<< endl;
        for (int j=0;j<r;j++){
            for (int k=0;k<c;k++){
                answer << arr[j][k];
            }
            answer << endl;
        }
    }
    return 0;
}
