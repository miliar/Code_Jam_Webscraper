#include<bits/stdc++.h>
#define F first
#define S second
#define N 25
using namespace std;
typedef pair<int,int> P;
typedef pair<P,P> P1;

int r,c;
string s[N];
map<char,P1> memo; // P(ymin, ymax) P(xmin, xmax)

bool check(){
  bool res=true;
  for(int i=0;i<r;i++)
    for(int j=0;j<c;j++)
      if(s[i][j]=='?')res=false;
  return res;
}

void solve(){

  while(!check()){

    map<char,P1>::iterator ite=memo.begin();

    while(ite!=memo.end()){
      
      int ymin=(*ite).S.F.F,ymax=(*ite).S.F.S;
      int xmin=(*ite).S.S.F,xmax=(*ite).S.S.S;
      
      

      int flag=1;

      for(int i=xmin;i<=xmax;i++){ // 0
	int ny=ymin-1,nx=i;
	
	if(ny<0||s[ny][nx]!='?'){
	  flag=0;
	  break;
	}
	
      }
      
      if(flag){
	for(int i=xmin;i<=xmax;i++)
	  s[ymin-1][i]=(*ite).F;
	(*ite).S.F.F--;
	ymin--;
      }

      flag=1;

      for(int i=xmin;i<=xmax;i++){ // 2
	int ny=ymax+1,nx=i;
	
	if(r<=ny||s[ny][nx]!='?'){
	  flag=0;
	  break;
	}
	
      }
      
      if(flag){
	for(int i=xmin;i<=xmax;i++)
	  s[ymax+1][i]=(*ite).F;
	(*ite).S.F.S++;
	ymax++;
      }

      flag=1;

      for(int i=ymin;i<=ymax;i++){ // 1
	int ny=i,nx=xmax+1;
	
	if(c<=nx||s[ny][nx]!='?'){
	  flag=0;
	  break;
	}
	
      }
      
      if(flag){
	for(int i=ymin;i<=ymax;i++)
	  s[i][xmax+1]=(*ite).F;
	(*ite).S.S.S++;
	xmax++;
      }

      flag=1;

      for(int i=ymin;i<=ymax;i++){ // 3
	int ny=i,nx=xmin-1;
	
	if(nx<0||s[ny][nx]!='?'){
	  flag=0;
	  break;
	}
	
      }
      
      if(flag){
	for(int i=ymin;i<=ymax;i++)
	  s[i][xmin-1]=(*ite).F;
	(*ite).S.S.F--;
	xmin--;
      }

      ite++;
    }
    
  }
  
}

int main(){
  
  int t;
  cin>>t;
  
  for(int T=1;T<=t;T++){
    
    cin>>r>>c;
    
    for(int i=0;i<r;i++){
      cin>>s[i];
      
      for(int j=0;j<c;j++){
	if(s[i][j]=='?')continue;
	
	if(!memo.count(s[i][j]))memo[s[i][j]]=P1(P(i,i),P(j,j));
	else{
	  memo[s[i][j]].F.F=min(memo[s[i][j]].F.F,i);
	  memo[s[i][j]].F.S=max(memo[s[i][j]].F.S,i);
	  memo[s[i][j]].S.F=min(memo[s[i][j]].S.F,j);
	  memo[s[i][j]].S.S=max(memo[s[i][j]].S.S,j);
	}
	
      }
      
    }
    
    map<char,P1>::iterator ite=memo.begin();

    while(ite!=memo.end()){
      
      int ymin=(*ite).S.F.F,ymax=(*ite).S.F.S;
      int xmin=(*ite).S.S.F,xmax=(*ite).S.S.S;
      
      for(int i=ymin;i<=ymax;i++)
	for(int j=xmin;j<=xmax;j++) s[i][j]=(*ite).F;

      ite++;
    }
    
    solve();

    cout<<"Case #"<<T<<":"<<endl;
    for(int i=0;i<r;i++)cout<<s[i]<<endl;
    
    memo.clear();
  }
  
  return 0;
}
