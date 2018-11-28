/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C/C++.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
int T,R,C;
char grid[100][100];
int ori[100][100];

void fill(int ii, int jj){
    //goto each cell
    //for(int ii=i;ii<len;ii++){
        //for(int jj=j;jj<len;jj++){
            //if it is char
            if(!ori[ii][jj]) return;
            char curC = grid[ii][jj];
            if(grid[ii][jj]!='?' && grid[ii][jj]!='#'){
                int a=ii,b=ii;
                //find longest column on one side
                a = ii-1;
                while(a>=0 && grid[a][jj]=='?'){
                    grid[a][jj]=curC;
                    a--;
                }
                //other side
                b = ii+1;
                while(b<R && grid[b][jj]=='?'){
                    grid[b][jj]=curC;
                    b++;
                }
                //check next columns
                int c = jj+1,s;
                while(c<C){
                    for(s=a+1;s<b;s++){
                        if(grid[s][c]!='?')
                            break;
                    }

                    if(s==b){
                        for(s=a+1;s<b;s++){
                            grid[s][c]=curC;
                        }
                        c++;
                    }else
                        break;
                }
                //check previous columns
                c = jj-1;
                while(c>=0){
                    for(s=a+1;s<b;s++){
                        if(grid[s][c]!='?')
                            break;
                    }

                    if(s==b){
                        for(s=a+1;s<b;s++){
                            grid[s][c]=curC;
                        }
                        c--;
                    }else
                        break;
                }
            }
      //  }
    //}
}
void solve(){

    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            ori[i][j]=0;
        }
    }

    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            if(grid[i][j]!='?')
                ori[i][j]=1;
        }
    }

    for(int i=0;i<C;i++){
        for(int j=0;j<R;j++){
            fill(j,i);
        }
    }
}
int main()
{
//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
    scanf("%d", &T);
    for(int i=0; i<T;i++){
        scanf("%d %d",&R,&C);
        for(int j=0;j<R;j++){
            scanf("%s",grid[j]);
        }

        solve();

        printf("Case #%d:\n",i+1);
        for(int a=0;a<R;a++){
            printf("%s\n",grid[a]);
        }
    }

    return 0;
}


