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

freopen("/Users/mohittyagi/Downloads/B-large.in", "r", stdin);
freopen("/Users/mohittyagi/Downloads/BBOutput-LARGE-practice.txt", "w", stdout);
scanf("%d",&t);
for(tst=1;tst<=t;tst++)
{
     int a[20],b[20],flag;


     i=0;
     ll rmdr,tmp;
    ll rm10;
    ll dvsr;
    ll quot;
    cin>>rmdr   ;
    tmp=rmdr;// read in number
    while(tmp!=0)  {
    	int digit = tmp%10;
    	b[i++]=digit;
    	tmp=tmp/10;
    }

    for(k=i-1,j=0;k>=0;k--,j++){
    	a[j]=b[k];
    }

int flagt[20];
for(k=0;k<i;k++){
	flagt[k]=0;
}
    printf("\n");
    while(1)
        {
            for(k=0;(k+1)<i;k++){
        flag=1;

        if(flagt[k])
        	break;
        if(a[k+1]<a[k] && flagt[k]==0) {
            a[k+1]=9;
            if(a[k]!=0){
                a[k] = a[k]-1;
            }
            flagt[k]=flagt[k+1]=1;

            flag=0;
            break;
        }
        if(flag==0)
            break;

    }
    if(flag)
        break;
}
    //printf("\n");

     //cin>>n>>s;

for(k=0;k<i;k++){
    if(a[k]==9){

        while(k<i){
            a[++k]=9;
        }
    }
}



        printf("Case #%d: ",tst);
     for(k=0;k<i;k++){
        if(a[k]>0){
            printf("%d", a[k]);
        }
     }
     printf("\n");
}




    return 0;
}
