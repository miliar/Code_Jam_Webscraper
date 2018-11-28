#include<bits/stdc++.h>
#define N 200005
#define ll long long
#define llu unsigned long long int
#define pare pair<int,int>
#define mod 1000000007

int ct=0,cases;
llu n,tmp;
llu A[1005];
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


int main(){
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    scanf("%d",&cases);
    while(cases--){
        ct++;
        memset(A,0,sizeof A);
        int i,j,k=0;


        scanf("%llu",&n);
        llu tmp1= n;
            tmp = tmp1;
            //cout<<tmp<<endl;

            k =0;
            while(tmp != 0){
                llu rem = tmp%10;
                A[k] = rem;
                k++;
                tmp = tmp / 10;
            }
            llu index = 0,fl =0;
            for(i=1;i<k;i++){

                if(A[i] > A[i-1] ){
                    fl = 1;
                    A[i] = A[i] - 1;
                    index = i-1;
                }

            }
            printf("Case #%d: ",ct);

             if(fl == 1){
                for(i=0;i<=index;i++){
                    A[i] = 9;
                }
             }
                for(i=k-1;i>=0;i--){
                    if(A[i] != 0)printf("%llu",A[i]);
                }
                printf("\n");

        //printf("Case #%d: %llu",ct,res);
    }

}
