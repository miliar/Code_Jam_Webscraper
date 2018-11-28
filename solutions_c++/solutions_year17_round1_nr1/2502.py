#include <bits/stdc++.h> 
using namespace std;
#define ll long long int
#define gearchange() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
#define MOD 1000000007LL

int main(){
  gearchange();
  int t;
  cin>>t;
  for (int i = 1; i <=t; ++i)
  {
     int n,m;
     cin>>n>>m;
     vector< string > vec;
     for (int j = 0; j <n; ++j)
     {
       string s;
       cin>>s;
       vec.push_back(s);
     }

      for (int j = 0; j <m; j++)
      {
        char a;
        int k=0;
        int x=0;
         while(k<n-1){
           while(k<n){ if(vec[k][j]=='?'){k++;}else{ break; } }
           if(k<n){
              a= vec[k][j];
              while(x<n){
               if(vec[x][j]=='?'|| vec[x][j]==a){
                vec[x][j]=a;
                x++;
               }
               else{
                 break;
               }
              }
             k=x;
           }
           else{
            break;
           }
          }
      }    
       for (int j = 0; j <n; j++)
      {
        char a;
        int k=0;
        int x=0;
         while(k<m){
             while(k<m and (vec[j][k]=='?')){k++;}
             if(k<m){ a= vec[j][k]; }
             else{ break; }
             while(x<m and (vec[j][x]=='?' or vec[j][x]==a)){ vec[j][x]=a; x++; }
             k=x;
         }
         
      }    


       cout<<"Case #"<<i<<":"<<endl;
       for (int j = 0; j <n; j++)
      {
        cout<<vec[j]<<endl;
      }
       }
        return 0; 
  }