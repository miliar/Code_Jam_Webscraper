#include<bits/stdc++.h>
using namespace std;



 
 int main()
  {
   int t;
     int c=0;
     cin>>t;
     while(t--)
      {
        c++;
       int n,m;
         cin>>n>>m;
         char a[n][m];
         for(int i=0;i<n;i++){
             string s;
             cin>>s;
             for(int j=0;j<m;j++){
                 a[i][j]=s[j];
             }
             
         }
       /*  int x1[26]=999;
         int x2[26]=-1;
         int y1[26]=999;
         int y2[26]=-1;
         for(int i=0;i<n;i++){
             for(int j=0;j<n;j++){
                 int al=a[i][j]-'a';
                 if(i<x1[al]) x1[al]=i;
                 if(i>x2[al]) x2[al]=i;
                 if(j<y1[al]) y1[al]=j;
                 if(j>y2[al]) y2[al]=j;
                 
             }
         }*/
       //  r<pair<pair<int,int>,pair<int,int>>> vpp;
         for(int i=0;i<m;i++){
             for(int j=1;j<n;j++){
                 if(a[j][i]=='?' && a[j-1][i]!='?'){
                     a[j][i]=a[j-1][i];
                    // cout<<j<<" "<<i<<endl;
                     //cout<<a[j-1][i]<<" "<<a[j][i]<<endl;
                 }
            //     cout<<j<<" "<<i<<endl;
              //       cout<<a[j-1][i]<<" "<<a[j][i]<<endl;
             }
         }
         for(int i=0;i<m;i++){
              for(int j=n-2;j>=0;j--){
                if(a[j][i]=='?' && a[j+1][i]!='?'){
                     a[j][i]=a[j+1][i];
                     
                 }  
                   // cout<<j<<" "<<i<<endl;
                    //cout<<a[j+1][i]<<" "<<a[j][i]<<endl;
                  
                //  cout<<a[i][j];
              }
              //cout<<endl;
          }
         for(int i=0;i<n;i++){
             for(int j=1;j<m;j++){
                 if(a[i][j]=='?' && a[i][j-1]!='?'){
                     a[i][j]=a[i][j-1];
                 }
             }
         }
          for(int i=0;i<n;i++){
             for(int j=m-2;j>=0;j--){
                 if(a[i][j]=='?' && a[i][j+1]!='?'){
                     a[i][j]=a[i][j+1];
                 }
             }
         }
         
         cout<<"Case #"<<c<<":"<<endl;
          for(int i=0;i<n;i++){
              for(int j=0;j<m;j++){
                  
                  
                  cout<<a[i][j];
              }
              cout<<endl;
          }
         
         
   }
  }
