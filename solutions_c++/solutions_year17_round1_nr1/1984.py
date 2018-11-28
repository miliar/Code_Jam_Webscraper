#include<cmath>
#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<algorithm>
 
using namespace std;

const int N = 100001;
 
int main(int argc, const char * argv[]) {
    int t;
    scanf("%d",&t);
    for(int a = 0; a < t; a++){
        int r,c;
        scanf("%d %d",&r,&c);
        string matrix[r];
        for(int i = 0; i < r; i++)
            cin>>matrix[i];
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++)
                if(matrix[i][j] != '?')
                    for(int z = 0; z < c && (matrix[i][z] == '?' || matrix[i][z] == matrix[i][j] || z < j); z++)
                        if(z < j && matrix[i][z] == '?')
                            matrix[i][z] = matrix[i][j];
                        else if(z > j && matrix[i][z] == '?')
                            matrix[i][z] = matrix[i][j];
 
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++)
                if(matrix[i][j] != '?')
                    for(int z = 0; z < r && (matrix[z][j] == '?' || matrix[z][j] == matrix[i][j] || z < i); z++)
                        if(z < i && matrix[z][j] == '?')
                            matrix[z][j] = matrix[i][j];
                        else if(z > i && matrix[z][j] == '?')
                            matrix[z][j] = matrix[i][j];
 
        cout<<"Case #"<<a+1<<": "<<endl;
        for(int i = 0; i < r;i++){
            cout<<matrix[i]<<endl;
        }
    }
    return 0;
}