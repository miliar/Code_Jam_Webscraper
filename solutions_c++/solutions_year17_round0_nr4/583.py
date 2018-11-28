#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <stack>

using namespace std;

#define MAX_N 100
#define MAX_2N 200

int dfs(int sum, int n, char mxa[MAX_N][MAX_N], int a_up[MAX_2N], int a_down[MAX_2N], char modifiy[MAX_N][MAX_N], vector<pair<int,int>> &status, vector<map<string,int>> &mem){
    if(sum==n*2-1) return 0;
    string a_down_str;
    for(int i=0;i<n*2-1;i++){
        if(a_down[i]==0) a_down_str+='0';
        else a_down_str+='1';
    }
    if(mem[sum].find(a_down_str)!=mem[sum].end()){
        return mem[sum][a_down_str];
    }

    int i=sum,j=0;
    int max=-1, max_i=-1, max_j=-1;
    
    vector<pair<int,int>> returned_status, max_status;
    
    int res=dfs(sum+1,n,mxa,a_up,a_down,modifiy,returned_status,mem);
    if(max<res){max=res-1;status=returned_status;}
    
//    cout<<sum<<": ";
    while(i>=0){
        if(i<n && j<n){
//            cout<<"("<<i<<","<<j<<")";
            if(a_down[i+n-j-1]==0){
                mxa[i][j]='+';
                a_down[i+n-j-1]++;
                a_up[sum]++;
                modifiy[i][j]++;
                
                res=dfs(sum+1,n,mxa,a_up,a_down,modifiy,returned_status,mem);
                pair<int,int> p(i,j);
                returned_status.push_back(p);
                if(max<res){max=res; max_i=i; max_j=j;status=returned_status;}
                
                mxa[i][j]='.';
                a_down[i+n-j-1]--;
                a_up[sum]--;
                modifiy[i][j]--;
            }
        }
        i--;
        j++;
    }
//    cout<<endl;
//    cout<<sum<<" "<<max+1<<" "<<max_i<<" "<<max_j<<endl;
    mem[sum][a_down_str]=max+1;
    if(max_i!=-1){
//        mxa[max_i][max_j]='+';
//        a_down[max_i+n-max_j-1]++;
//        a_up[sum]++;
//        modifiy[max_i][max_j]++;
        return max+1;
    }else{
        return max+1;
    }
}


int main(void){
    if(false){
        int n=6;
        int i=7-n+1, j=n-1;
        while(true){
            cout<<i<<", "<<j<<endl;
            //find next
            if(i==n-1 && j==n-1){
                break;
            }
            if(j==n-1){
                j=i;
                i=n-1;
            }else{
                i=j+1;
                j=n-1;
            }
        }
    }

    int T;
//    char dump;
    FILE *fin=fopen("/Users/enyaning/Downloads/D-small-attempt1.in.txt","r");
//    FILE *fin=stdin;
    fscanf(fin,"%d",&T);
    for(int I=1;I<=T;I++){
        int n,k;
        fscanf(fin,"%d %d", &n,&k);
        char mxa[MAX_N][MAX_N]={0}, mxx[MAX_N][MAX_N]={0};
        char modifiy[MAX_N][MAX_N]={0};
        while(k--){
            char str[3], ch;
            int x,y;
            fscanf(fin,"%s %d %d",str,&x,&y);
            ch=str[0];
            x--; y--;
//            printf("%c %d %d\n",ch,x,y);
            
            if(ch=='+'){
                mxa[x][y]='+';
            }
            if(ch=='x'){
                mxx[x][y]='x';
            }
            if(ch=='o'){
                mxa[x][y]='+';
                mxx[x][y]='x';
            }
        }
        
        /***********************************
                    x
        ***********************************/
        int x_col[MAX_N]={0};
        int x_row[MAX_N]={0};
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(mxx[i][j]=='x') x_row[i]+=1;
                if(mxx[j][i]=='x') x_col[i]+=1;
            }
        }
        for(int i=0;i<n;i++){
            if(x_row[i]==0){
                int j;
                for(j=0;j<n;j++){
                    if(x_col[j]==0){
                        mxx[i][j]='x';
                        modifiy[i][j]+=1;
                        x_col[j]+=1;
                        x_row[i]+=1;
                        break;
                    }
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(mxx[i][j]==0) mxx[i][j]='.';
            }
        }
        
        /***********************************
                    y
        ***********************************/
        int a_up[MAX_2N]={0};
        int a_down[MAX_2N]={0};
        
        for(int sum=0;sum<n*2-1;sum++){
            //check if exist '+'
            int i=sum,j=0;
            while(i>=0){
                if(i<n && j<n){
                    if(mxa[i][j]=='+') a_up[sum]++;
                }
                i--;
                j++;
            }
        }
        for(int sum=0;sum<n*2-1;sum++){
            //check if exist '+'
            int i=0,j=n-sum-1;
            while(i<n){
                if(i<n && j>=0){
                    if(mxa[i][j]=='+') a_down[sum]++;
                }
                i++;
                j++;
            }
        }
        
        for(int sum=0;sum<n*2-1;sum++) if(a_up[sum]==0){
            if(sum<n-1){
                int i=sum,j=0;
                while(i>=0){
                    if(j<n){
                        if(a_down[i+n-j-1]==0){
                            mxa[i][j]='+';
                            modifiy[i][j]+=1;
                            a_down[i+n-j-1]++;
                            a_up[sum]++;
                            
                            break;
                        }
                    }
                    i--;
                    j++;
                }
            }else{
                int i=sum-n+1, j=n-1;
                while(true){
                    if(a_down[i+n-j-1]==0){
                        mxa[i][j]='+';
                        modifiy[i][j]+=1;
                        a_down[i+n-j-1]++;
                        a_up[sum]++;
                        
                        break;
                    }
                    
                    //find next
                    if(i==n-1 && j==n-1){
                        break;
                    }
                    if(j==n-1){
                        j=i;
                        i=n-1;
                    }else{
                        i=j+1;
                        j=n-1;
                    }
                }
            }
        }
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(mxa[i][j]==0) mxa[i][j]='.';
            }
        }
//        
//        
//        
//        /*for(int sum=0;sum<n*2-1;sum++) if(a_up[sum]==0){
//            int i=sum,j=0;
//            while(i>=0){
//                if(i<n){
//                    if(a_down[i+n-j-1]==0){
//                        mxa[i][j]='+';
//                        modifiy[i][j]+=1;
//                        a_down[i+n-j-1]++;
//                        a_up[sum]++;
//                        
//                        break;
//                    }
//                }
//                i--;
//                j++;
//            }
//        }*/
//        
//        for(int i=0;i<n;i++){
//            for(int j=0;j<n;j++){
//                if(mxa[i][j]==0) mxa[i][j]='.';
//            }
//        }
//        
//        vector<pair<int,int>> status;
//        vector<map<string,int>> mem(n*2-1,map<string,int>());
//        dfs(0,n,mxa,a_up,a_down,modifiy,status,mem);
//        for(pair<int,int> p : status){
////            cout<<"("<<p.first<<","<<p.second<<")"<<endl;
//            mxa[p.first][p.second]='+';
//            modifiy[p.first][p.second]++;
//        }
//        
        
        /***********************************
                finally
        ***********************************/
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
//                printf("%c ", mxa[i][j]);
            }
//            printf("\n");
        }
        
        int score=0;
        int ms=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(mxa[i][j]=='+') score+=1;
                if(mxx[i][j]=='x') score+=1;
                if(modifiy[i][j]!=0) ms+=1;
            }
        }
        
        printf("Case #%d: %d %d\n", I, score, ms);
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(modifiy[i][j]!=0){
                    char ch='.';
                    if(mxa[i][j]=='+' && mxx[i][j]=='x') ch='o';
                    else if(mxa[i][j]=='+') ch='+';
                    else if(mxx[i][j]=='x') ch='x';
                    if(ch!='.')
                        printf("%c %d %d\n", ch, i+1, j+1);
                }
            }
        }
        
        
        
    }
}

/*

3
---+-++- 3
+++++ 4
-+-+- 4
 
*/
