#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<queue>
#include<stack>
#include<math.h>
#include<vector>
#include<algorithm>
#include<iostream>

using namespace std;

const int MAX_N = 100005;
const int MAX_M = 5005;
const int inf = 1000000007;
const int mod = 1000000007;

char buf[30][30];
int has_x[30];
int n,m;


int main()
{
    int kase=1;
    //freopen("test.txt","r",stdin);
    int T;
    cin>>T;
    while(T--){
       cin>>n>>m;
       memset(has_x,0,sizeof(has_x));
       for(int i=0;i<n;i++){
            int num1=0;
            for(int j=0;j<m;j++){
                cin>>buf[i][j];
                if(buf[i][j]!='?')num1++;
            }
       }

       int x=-1;
       for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(buf[i][j]!='?'){
                for(int k=i+1;k<n;k++){
                    if(buf[k][j]!='?'){break;}
                    else buf[k][j]=buf[i][j];
                }
                for(int k=i-1;k>=0;k--){
                    if(buf[k][j]!='?'){break;}
                    else buf[k][j]=buf[i][j];
                }
            }
        }
       }
       for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(buf[i][j]!='?'){
                for(int k=j+1;k<m;k++){
                    if(buf[i][k]!='?'){break;}
                    else buf[i][k]=buf[i][j];
                }
                for(int k=j-1;k>=0;k--){
                    if(buf[i][k]!='?'){break;}
                    else buf[i][k]=buf[i][j];
                }
            }
        }
       }
       printf("Case #%d:\n",kase++);
       for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cout<<buf[i][j];
        }cout<<endl;
       }
    }
    return 0;
}


