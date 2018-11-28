#include <bits/stdc++.h>

using namespace std;


void printarr(int arr[], int size){
    for(int i=0;i<size;i++){
        printf("%d,",arr[i]);
    }
    printf("\n");
}

bool bpm(bool bpGraph[205][205], int M, int N, int u, bool seen[], int matchR[])
{
    // Try every job one by one
    for (int v = 0; v < N; v++)
    {
        // If applicant u is interested in job v and v is
        // not visited
        if (bpGraph[u][v] && !seen[v])
        {
            seen[v] = true; // Mark v as visited
 
            // If job 'v' is not assigned to an applicant OR
            // previously assigned applicant for job v (which is matchR[v]) 
            // has an alternate job available. 
            // Since v is marked as visited in the above line, matchR[v] 
            // in the following recursive call will not get job 'v' again
            if (matchR[v] < 0 || bpm(bpGraph, M, N, matchR[v], seen, matchR))
            {
                matchR[v] = u;
                return true;
            }
        }
    }
    return false;
}
 
// Returns maximum number of matching from M to N
int* maxBPM(bool bpGraph[205][205], int M, int N)
{
    // An array to keep track of the applicants assigned to
    // jobs. The value of matchR[i] is the applicant number
    // assigned to job i, the value -1 indicates nobody is
    // assigned.
    static int matchR[205];
 
    // Initially all jobs are available
    memset(matchR, -1, sizeof(matchR));
 
    int result = 0; // Count of jobs assigned to applicants
    for (int u = 0; u < M; u++)
    {
        // Mark all jobs as not seen for next applicant.
        bool seen[N];
        memset(seen, 0, sizeof(seen));
 
        // Find if the applicant 'u' can get a job
        if (bpm(bpGraph, M, N, u, seen, matchR))
            result++;
    }
    return matchR;
}

void printgrid(int grid[105][105], int size){
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            printf("%d",grid[i][j]);
        }
        printf("\n");
    }
}

int gridr[105][105];
int gridb[105][105];
int addgrid[105][105];

int main(void){
    freopen("testin.txt","r",stdin);
    freopen("testout.txt", "w", stdout);
    int tt;
    int n,m;
    cin >> tt;
    
    for(int t=1; t<=tt; t++){
        cin >> n;
        cin >> m;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                gridr[i][j]=0;
                gridb[i][j]=0;
                addgrid[i][j]=0;
            }
        }
        char ch[10];
        int r,c;
        int score=0;
        for(int i=0;i<m;i++){
            cin >> ch;
            cin >> r;
            cin >> c;
            if(ch[0]=='x' || ch[0]=='o'){
                gridr[r-1][c-1]=1;
                score++;
            }
            if(ch[0]=='+' || ch[0]=='o'){
                gridb[r-1][c-1]=2;
                score++;
            }
        }
        
        int counter=0;
        int missingr[105];
        int missingc[105];
        for(int i=0;i<n;i++){
            int ismissing=1;
            for(int j=0;j<n;j++){
                if(gridr[i][j]==1){
                    ismissing=0;
                    break;
                }
            }
            if(ismissing){
                missingr[counter]=i;
                counter++;
            }
        }
        counter=0;
        for(int i=0;i<n;i++){
            int ismissing=1;
            for(int j=0;j<n;j++){
                if(gridr[j][i]==1){
                    ismissing=0;
                    break;
                }
            }
            if(ismissing){
                missingc[counter]=i;
                counter++;
            }
        }
        
        score+=counter;
        for(int i=0;i<counter;i++){
            addgrid[missingr[i]][missingc[i]]+=1;
        }
        
        int diagdown[205];
        int diagup[205];
        int diagdownsize=0,diagupsize=0;
        for(int i=0;i<n;i++){
            int isempty=1;
            for(int j=0;j<i+1;j++){
                //printf("%d %d\n",i,j);
                if(gridb[n-1-i+j][j]==2){
                    isempty=0;
                    break;
                }
            }
            if(isempty){
                diagdown[diagdownsize]=i;
                diagdownsize++;
            }
        }
        for(int i=1;i<n;i++){
            int isempty=1;
            for(int j=i;j<n;j++){
                if(gridb[j-i][j]==2){
                    isempty=0;
                    break;
                }
            }
            if(isempty){
                diagdown[diagdownsize]=i+n-1;
                diagdownsize++;
            }
        }
        for(int i=0;i<n;i++){
            int isempty=1;
            for(int j=0;j<i+1;j++){
                if(gridb[i-j][j]==2){
                    isempty=0;
                    break;
                }
            }
            if(isempty){
                diagup[diagupsize]=i;
                diagupsize++;
            }
        }
        for(int i=1;i<n;i++){
            int isempty=1;
            for(int j=i;j<n;j++){
                if(gridb[n-1+i-j][j]==2){
                    isempty=0;
                    break;
                }
            }
            if(isempty){
                diagup[diagupsize]=i+n-1;
                diagupsize++;
            }
        }
        
        bool bpg[205][205];
        int gm=diagdownsize;
        int gn=diagupsize;
        //printarr(diagdown, gm);
        //printarr(diagup, gn);
        for(int i=0;i<gm;i++){
            for(int j=0;j<gn;j++){
                int ii=diagdown[i];
                int jj=diagup[j];
                if((ii+jj+1-n)%2!=0){
                    bpg[i][j]=false;
                }else{
                    int rr=(jj+n-1-ii)/2;
                    int cc=(jj+ii+1-n)/2;
                    if(0<=rr && rr<n && 0<=cc && cc<n){
                        bpg[i][j]=true;
                    }else{
                        bpg[i][j]=false;
                    }
                }
            }
        }
        /*
        for(int i=0;i<gm;i++){
            for(int j=0;j<gn;j++){
                if(bpg[i][j]) printf("1");
                else printf("0");
            }
            printf("\n");
        }*/
        
        int* matching=maxBPM(bpg, gm, gn);
        
        for(int j=0;j<gn;j++){
            int i=*(matching+j);
            if(i>=0){
                int ii=diagdown[i];
                int jj=diagup[j];
                int rr=(jj+n-1-ii)/2;
                int cc=(jj+ii+1-n)/2;
                score++;
                addgrid[rr][cc]+=2;
                //printf("%d,%d|%d,%d\n",ii,jj,rr,cc);
            }
        }
        
        //printgrid(gridr, n);
        //printgrid(gridb, n);
        //printgrid(addgrid, n);
        /*for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                printf("%d",gridr[i][j]+gridb[i][j]+addgrid[i][j]);
            }
            printf("\n");
        }*/
        
        char toaddch[305];
        int toaddr[305];
        int toaddc[305];
        int toaddnum=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(addgrid[i][j]>0){
                    int toadd=addgrid[i][j]+gridr[i][j]+gridb[i][j];
                    if(toadd==1) toaddch[toaddnum]='x';
                    else if(toadd==2) toaddch[toaddnum]='+';
                    else toaddch[toaddnum]='o';
                    toaddr[toaddnum]=i;
                    toaddc[toaddnum]=j;
                    toaddnum++;
                }
            }
        }
        
        printf("Case #%d: %d %d\n", t, score, toaddnum);
        for(int i=0;i<toaddnum;i++){
            printf("%c %d %d\n",toaddch[i],toaddr[i]+1,toaddc[i]+1);
        }
        
    }
    
    return 0;
}
