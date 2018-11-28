 #include <bits/stdc++.h>

#define lp(i,n) for(int i=0; i<n; i++)

#define ll long long
#define pb push_back
#define  mp make_pair
#define pii pair<int,int>
#define ff first
#define ss second
#define nl "\n"

#define EPS 1e-8
#define OO 100000000

#define on(i,n) i=i|(1<<n)
#define off(i,n) i=i& (~(1<<n))

using namespace std;
int n;

int dp[5][5][1000+5][1000+5];
bool solve(int first, int last,int idx, int R, int Y, int B){
    if(dp[first][last][R][Y]!=-1){
        return dp[first][last][R][Y];
    }
    if(idx==n-1){
        if(R==1 && (first==0|| last==0) ){
            return false;
        }



        if(Y==1 && (first==1|| last==1) ){
            return false;
        }

        if(B==1 && (first==2|| last==2) ){
            return false;
        }
        return dp[first][last][R][Y]= true;
    }

    if(idx==0){
        bool ans=false;
        if(Y!=0)
    ans|=solve(1,1,idx+1,R,Y-1,B);
        if(B!=0)
    ans|=solve(2,2,idx+1,R,Y,B-1);
    if(R!=0)
    ans|=solve(0,0,idx+1,R-1,Y,B);
    return dp[first][last][R][Y]=ans;
    }

            bool ans=false;
        if(Y!=0 &&last!=1)
    ans|=solve(first,1,idx+1,R,Y-1,B);
        if(B!=0 && last!=2)
    ans|=solve(first,2,idx+1,R,Y,B-1);
    if(R!=0 && last!=0)
    ans|=solve(first,0,idx+1,R-1,Y,B);
    return dp[first][last][R][Y]=ans;



}

void print_path(int first, int last,int idx, int R, int Y, int B){

if(idx==n-1){

        if(R==1 && (first!=0&& last!=0) ){
            cout<<"R";

            return;
        }
                if(Y==1 && (first!=1&& last!=1)){
            cout<<"Y";
            return;
        }
                if(B==1 && (first!=2&& last!=2)){
            cout<<"B";
            return;
        }

    }


    if(idx==0){
        bool ans=false;
        if(Y!=0 && dp[1][1][R][Y-1] ){
            cout<<"Y";
            print_path(1,1,idx+1,R,Y-1,B);
            return;
        }
                if(B!=0 && dp[2][2][R][Y] ){
            cout<<"B";
            print_path(2,2,idx+1,R,Y,B-1);
            return;
        }
                if(R!=0 && dp[0][0][R-1][Y]){
            cout<<"R";
            print_path(0,0,idx+1,R-1,Y,B);
            return;
        }

    }


        bool ans=false;
        if(Y!=0 && dp[first][1][R][Y-1] &&last!=1){
            cout<<"Y";
            print_path(first,1,idx+1,R,Y-1,B);
            return;
        }
        if(B!=0 && dp[first][2][R][Y] &&last!=2){
            cout<<"B";
            print_path(first,2,idx+1,R,Y,B-1);
            return;
        }
        if(R!=0 && dp[first][0][R-1][Y] &&last!=0){
            cout<<"R";
            print_path(first,0,idx+1,R-1,Y,B);
            return;
        }








}

int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    lp(cs,t){
        int r,y,b;
        int o,g,v;
        cin>>n;
        memset(dp,-1,sizeof dp);

        printf("Case #%d: ",cs+1);
        cin>>r>>o>>y>>g>>b>>v;
        if(solve(0,0,0,r,y,b)){
            print_path(0,0,0,r,y,b);
            cout<<endl;
        }else{
            cout<<"IMPOSSIBLE"<<endl;
        }
    }




}
