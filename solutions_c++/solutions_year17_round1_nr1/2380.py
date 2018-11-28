#include <bits/stdc++.h>
#define endl '\n';
using namespace std;
typedef long long int LL;


char a[50][50];

int main()
{
  ios_base::sync_with_stdio(false);cin.tie(0);

  //freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

  int tc;cin>>tc;for(int t=1;t<=tc;t++)
  {    
     cout<<"Case #"<<t<<":\n";
     
     int r,c;
     cin>>r>>c;

     for(int i=1;i<=r;i++)
     {
     	for(int j=1;j<=c;j++)
     	{
     		cin>>a[i][j];
     	}
     }
    
    for(int j=1;j<=c;j++)
    {
    	for(int i=1;i<=r;i++)
    	{
           if(a[i][j]!='?')
           {
           	 int f=i-1;
           	 while((f>=1)&&(a[f][j]=='?')){
           	 	a[f][j]=a[i][j];
           	 	f--;
           	 }
             
             f=i+1;
             while((f<=r)&&(a[f][j]=='?')){
                 a[f][j]=a[i][j];
                 f++;
             }
           }
    	}
    }

    for(int j=1;j<=c;j++)
     {
     	 if(a[1][j]!='?'){
     	 	int f=j-1;
     	 	while((f>=1)&&(a[1][f]=='?')){
                for(int g=1;g<=r;g++)a[g][f]=a[g][j];
     	 		f--;
     	 	}

     	 	f=j+1;

     	 	while((f<=c)&&(a[1][f]=='?')){
     	 		for(int g=1;g<=r;g++)a[g][f]=a[g][j];
     	 		f++;
     	 	}
     	 }
     }

     for(int i=1;i<=r;i++)
     {
     	for(int j=1;j<=c;j++)
     	{
     		cout<<a[i][j];
     	}
     	cout<<endl;
     }

  }
          
  return 0;
}