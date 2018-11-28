#include <bits/stdc++.h>
using namespace std;
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("ALarge.out","w",stdout);
  int t;
  cin>>t;
  for(int i1=1;i1<=t;i1++){
  	int r,c;
  	cin>>r>>c;
  	char a[r][c];
  	for(int i=0;i<r;i++){
  		for(int j=0;j<c;j++){
  			cin>>a[i][j];
  		}
  	}
    int c1=0,flag1=0;
    char b[r][c];
    char ch;
    int d[r];
    for(int i=0;i<r;i++){
    	c1=0,flag1=0;
    	ch=' ';
    	for(int j=0;j<c;j++){
    	if(a[i][j]>=65&&a[i][j]<=90){
    		ch=a[i][j];
    		flag1=1;
    		break;
    	}
      }
      for(int j=0;j<c;j++){
      	if((a[i][j]=='?'||a[i][j]==ch)&&flag1==1){
      		b[i][j]=ch;
      		c1++;
      	}else if(flag1==1){
      		ch=a[i][j];
      		b[i][j]=ch;
      		c1++;
      	} 
      }
      int k=i;
      d[i]=c1;
      while(k>0&&d[k-1]==0&&d[k]==c){
      	for(int j=0;j<c;j++){
      		b[k-1][j]=b[k][j];
      	}
      	--k;
      	d[k]=c;
      	//cout<<k<<" "<<d[k]<<endl;
      }
      if(c1==0&&i>0&&d[i-1]==c){
      	for(int j=0;j<c;j++){
      		b[i][j]=b[i-1][j];
      	}
      	d[i]=c;
      }
      
     // cout<<d[i]<<endl;
    }
    cout<<"Case #"<<i1<<":"<<endl;
    for(int i=0;i<r;i++){
    	for(int j=0;j<c;j++){
    		cout<<b[i][j];
    		b[i][j]=' ';
    	}
    	cout<<endl;
    }
    
  	
  }
	return 0;
}

