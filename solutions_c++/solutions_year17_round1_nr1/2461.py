#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <list>
#include <cmath>
#include <string>

using namespace std;
typedef long long lli;

int main(){
    ofstream aout ( "a_out.txt" );
//    ofstream aout ( "a_out.txt" );
    lli t;
    cin>>t;
//    vector<bool> a
    lli cnt=1;
    while(t--)
    {
        lli r,c;
        cin>>r>>c;
        char cake[r+1][c+1];
        for(int i =1 ; i<=r;i++){
            for(int j = 1; j<=c;j++){
                cin>>cake[i][j];
            }
        }
//        for(int i =1 ; i<=r;i++){
//            for(int j = 1; j<=c;j++){
//                cout<<cake[i][j];
//            }
//            cout<<endl;
//        }
        for(int j =1 ; j<=c;j++)
        {
            for(int i = 1; i<=r;i++)
            {
                if(cake[i][j]=='?')
                {

                }
                else
                {
                    for(int k=i-1; k>=1;k--)
                    {
                        if(cake[k][j]=='?')
                            cake[k][j]=cake[i][j];
                        else
                            break;
                    }
                }
            }
            if(cake[r][j]=='?'){
                for(int k =r-1 ; k>=1;k--)
                {
                    if(cake[k][j]!='?')
                    {
                        for(int l=k+1;l<=r;l++)
                        {
                            if(cake[l][j]=='?')
                                cake[l][j]=cake[k][j];
                            else
                                break;
                        }
                        break;
                    }
                }
            }
        }
//        for(int i =1 ; i<=r;i++){
//            for(int j = 1; j<=c;j++){
//                cout<<cake[i][j];
//            }
//            cout<<endl;
//        }
        for(int i =1;i<=r;i++)
        {
            for(int j = 1;j<=c;j++)
            {
                if(cake[i][j]=='?')
                {

                }
                else
                {
                    for(int k=j-1; k>=1;k--)
                    {
                        if(cake[i][k]=='?')
                            cake[i][k]=cake[i][j];
                        else
                            break;
                    }
                }
            }
            if(cake[i][c]=='?'){
                for(int k =c-1 ; k>=1;k--)
                {
                    if(cake[i][k]!='?')
                    {
                        for(int l=k+1;l<=c;l++)
                        {
                            if(cake[i][l]=='?')
                                cake[i][l]=cake[i][k];
                            else
                                break;
                        }
                        break;
                    }
                }
            }
        }
        cout<<"Case #"<<cnt<<":\n";
        aout<<"Case #"<<cnt<<":\n";
        for(int i =1 ; i<=r;i++){
            for(int j = 1; j<=c;j++){
                cout<<cake[i][j];
                aout<<cake[i][j];
            }
            cout<<endl;
            aout<<endl;
        }
        cnt++;
    }
}
/*
1
4 3
FCE
?AB
??D
???
*/
