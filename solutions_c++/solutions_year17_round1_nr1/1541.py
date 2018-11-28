#include<bits/stdc++.h>
using namespace std;
#define FILE freopen("input.in", "rt", stdin),freopen("output.txt", "wt", stdout);
int main(){
    FILE
    int t,u=0;
    cin>>t;
    while(t--){
          u++;
          int n,m,i,j,k,x,y,z,l,r;
          cin>>n>>m;

          char a[n+1][m+1];

          for(i=0;i<n;i++){
              cin>>a[i];
          }

          set<char> s;

          for(i=0;i<n;i++){
              for(j=0;j<m;j++){
                    if(a[i][j]!='?' && (s.find(a[i][j])==s.end())){
                          s.insert(a[i][j]);
                          for(x=j-1;x>=0;x--){
                                if(a[i][x]!='?')
                                break;
                          }
                          l=x+1;
                          for(x=j+1;x<m;x++){
                               if(a[i][x]!='?')
                               break;
                          }
                          r=x-1;
                          for(x=i;x>=0;x--){
                                k=0;
                                for(y=l;y<=r;y++){
                                     if(a[x][y]=='?' || (x==i && y==j))
                                     k++;
                                     else
                                     break;
                                }

                                if(k!=(r-l+1))
                                break;
                                else
                                for(y=l;y<=r;y++){
                                     a[x][y]=a[i][j];
                                }
                          }
                          for(x=i+1;x<n;x++){
                                k=0;
                                for(y=l;y<=r;y++){
                                	if(a[x][y]=='?' || (x==i && y==j))
                                     k++;
                                     else
                                     break;

                                }

                                if(k!=(r-l+1))
                                break;
                                else
                                for(y=l;y<=r;y++){
                                     a[x][y]=a[i][j];
                                }
                          }
                    }
              }
          }
          cout<<"Case #"<<u<<": \n";
          for(i=0;i<n;i++){
              cout<<a[i]<<endl;
          }
    }
}
