#include<bits/stdc++.h>
#define N 200005
#define ll long long
#define llu unsigned long long int
#define pare pair<int,int>
#define mod 1000000007

int ct=0,cases,cut;

using namespace std;

///dir array for Queen int dxq[10] = {-1,-1,-1,1,1,1,0,0};
///dir array for Queen int dyq[10] = {-1,0,1,-1,0,1,-1,1};
///dir array for knight int dxk[10] = {-2,-2,-1,-1,1,1,2,2};
///dir array for knight int dyk[10] = {1,-1,-2,2,-2,2,-1,1};
/*int leap(int year){
   	if( year%4 == 0 && year%100 == !0 )
            return 1;
	else if (year%100 == 0 && year%400 == 0)
            return 1;
	else
        return 0;
}*/
char S[1005];
int main(){
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    scanf("%d",&cases);
    while(cases--){
         ct++;
        scanf("%s %d",S,&cut);
        //cout<<S<<endl;
        int i,j,k,res = 0;
        int len = strlen(S);
        for(i=0;i<len;i++){
            if(S[i] == '-' && len - i >= cut){
                   // cout<<"dhukse "<<i<<endl;
                    res++;
                int right = i + cut;
                for(j=i;j<right;j++){
                    if(S[j] == '+'){
                        S[j] = '-';
                    }
                    else{
                        S[j] = '+';
                    }
                }
            }
        }
        int fl = 0;
        for(i=0;i<len;i++){
            if(S[i] != '+'){
                fl = 1;
                break;
            }
        }
        if(fl == 0){
            printf("Case #%d: %d\n",ct,res);
        }
        else{
            printf("Case #%d: IMPOSSIBLE\n",ct);
        }
    }

}
