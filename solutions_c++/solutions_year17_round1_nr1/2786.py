#include<bits/stdc++.h>
#include<algorithm>
#include<string>
using namespace std;

int main()
{
    
        
    FILE *fp = fopen("output.txt" , "w+");
    int T;cin >> T;
    for(int I = 1;I <= T;I++)
    {
        int r,c,i,j,k,ct=0,p,q=0;
        cin>>r>>c;char a[r][c];
        for(i=0;i<r;i++)
            for(j=0;j<c;j++)
            {
            cin>>a[i][j];
            if(a[i][j]!='?')
            	ct++;
            
        }p=(r*c)/ct;
        for(i=0;i<r;i++)
         {   for(j=0;j<c;j++)
            {q=0;
            if(a[i][j]!='?')
                {
                for(k=j-1;k>=0;k--){
                    
                    if(a[i][k]=='?'){
                        a[i][k]=a[i][j];
                        }
                }
                
                
                for(k=j+1;k<c;k++){
                    
                    if(a[i][k]=='?'){
                        a[i][k]=a[i][j];
                        }
                }
                
            }
                       }}ct=0;q=0;
          fprintf(fp,"Case #%d:\n",I);
          for(i=0;i<r;i++){
               for(j=0;j<c;j++){
                       fprintf(fp,"%c",a[i][j]);
               }
              fprintf(fp,"\n");}
       //printf(fp , "Case #%d: %d\n" , I , count);
    }
}

