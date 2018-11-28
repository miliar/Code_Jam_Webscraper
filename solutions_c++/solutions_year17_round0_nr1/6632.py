#include<iostream>
#include<vector>
#include<cstdio>
#define pb push_back
#define tr(c,i) for(typeof((c).begin() )i = (c).begin(); i != (c).end(); i++)
#define mod 1000000007
#define ii  pair<int,int>

using namespace std;
typedef long long ll;



using namespace std;




int main()
{
    int i,tst,t,j,k,sm,ans,n;
    char s[1010];
freopen("/Users/mohittyagi/Downloads/A-large.in", "r", stdin);
freopen("/Users/mohittyagi/Downloads/AOutput-LARGE-attempt0.txt", "w", stdout);
scanf("%d",&t);
for(tst=1;tst<=t;tst++)
{
     scanf("%s %d",s,&k);
     //cin>>n>>s;
     //printf("MMmmmm");
     int length = strlen(s);
     int sum[1010];
     for(i=0;i<=length;i++) {
    	 sum[i]=0;
     }
     if(s[0]!='+'){
        sum[0] = 1;
     }
     int numberOfTurns = 0,flag=0;

     for(i=1;s[i]!='\0';i++)
     {

    	 //printf("%d\n",sum[i]);
    	 if (i-k>=0)
        {
            numberOfTurns = sum[i-1]-sum[i-k];
        } else {
            numberOfTurns = sum[i-1];
        }

        if(numberOfTurns%2==0){
            if(s[i]=='+'){
                sum[i] = sum[i-1];
            } else if(i+k>length) {
                flag = 1;
                break;
            } else {
                sum[i] = sum[i-1] + 1;
            }
        } else {
            if(s[i]=='-'){
                sum[i] = sum[i-1];
            } else if(i+k>length) {
                flag = 1;
                break;
            } else {
                sum[i] = sum[i-1] + 1;
            }
        }


     }
     if(flag)
        printf("Case #%d: %s\n",tst,"IMPOSSIBLE");
     else
        printf("Case #%d: %d\n",tst,sum[length-1]);
}




    return 0;
}
