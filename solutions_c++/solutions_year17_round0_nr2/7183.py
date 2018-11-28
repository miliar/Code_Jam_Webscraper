#include<bits/stdc++.h>

using namespace std;

int main()
{
    unsigned long long int n,t;int k;
        
    FILE *fp = fopen("output.txt" , "w+");
    cin>>k;int i,j=0;
    for(i=0;i<k;i++){
        cin>>n;int ct=0,p=-1,fl=0;unsigned long long int q=0;
        t=n;
        while(t>0)
            {
            ct++;
            t=t/10;
            
        }if(ct==1)
            {
           // cout<<n<<endl;
            fprintf(fp , "Case #%d: %lld\n" , i+1 , n);
        }
        else{
        int a[ct];t=n;j=ct-1;
        while(t>0)
            {
            a[j]=t%10;
            j--;
            t=t/10;
            
        }
        for(j=0;j<ct-1;j++)
            {
            if(a[j]>a[j+1])
                {
                p=j;fl=1;break;
            }
        }if(fl==1){
        for(j=p+1;j<ct;j++)
            {
            a[j]=9;
        }if((a[p]==a[0])&&(p!=0)){
            for(j=p;j>0;j--)
                a[j]=9;
            a[j]--;
        }
            else{
            a[p]--;
        for(j=p-1;j>=0;j--)
            {
            if(a[j]>a[j+1])
                a[j]--;
        }}}
        for(j=0;j<ct;j++){
            q=q*10+a[j];
        }fprintf(fp , "Case #%d: %lld\n" , i+1 , q);}
       // cout<<endl;
        }return 0;}      //fprintf(fp , "Case #%d: %s\n" , I , str);
                
